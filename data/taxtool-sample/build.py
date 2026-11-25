"""Build the taxtool sample dataset and its expected result.

Reads prices.csv (daily volume-weighted average prices in EUR from the Kraken
public OHLC API), writes transactions.csv and expected-result.json, and prints
the expected result. Run: python3 build.py
"""

import csv
import json
from collections import defaultdict, deque
from datetime import datetime
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

HERE = Path(__file__).parent
SAT = Decimal("0.00000001")
CENT = Decimal("0.01")
TAX_YEAR = 2025
FREIGRENZE_23 = Decimal("1000")  # private sales, section 23 EStG, from 2024
FREIGRENZE_22 = Decimal("256")  # other income, section 22 no. 3 EStG
ACCOUNT = "Exchange A"

prices = {}
with open(HERE / "prices.csv") as f:
    for row in csv.DictReader(f):
        prices[(row["date_utc"], row["asset"])] = Decimal(row["vwap"])


def eur(x):
    return x.quantize(CENT, ROUND_HALF_UP)


def coin(x):
    return x.quantize(SAT, ROUND_HALF_UP)


def price(ts, asset):
    return prices[(ts[:10], asset)]


tx = []


def add(ts, kind, sent=("", ""), received=("", ""), value="", note=""):
    tx.append({
        "date_utc": ts, "account": ACCOUNT, "type": kind,
        "sent_amount": sent[0], "sent_asset": sent[1],
        "received_amount": received[0], "received_asset": received[1],
        "eur_value": value, "note": note,
    })


def buy(ts, asset, amount):
    cost = eur(amount * price(ts, asset))
    add(ts, "buy", (cost, "EUR"), (amount, asset), cost)


def sell(ts, asset, amount):
    proceeds = eur(amount * price(ts, asset))
    add(ts, "sell", (amount, asset), (proceeds, "EUR"), proceeds)


# Ten transactions on one exchange, no fees.
buy("2024-12-02T10:00:00Z", "BTC", Decimal("0.05"))
buy("2025-04-15T10:00:00Z", "BTC", Decimal("0.04"))
buy("2025-04-15T11:00:00Z", "ETH", Decimal("1.0"))
for d in ("2025-05-01", "2025-06-01", "2025-07-01"):
    amt = Decimal("0.003")
    add(f"{d}T00:00:00Z", "staking_reward", received=(amt, "ETH"), value=eur(amt * prices[(d, "ETH")]))
sell("2025-07-15T10:00:00Z", "BTC", Decimal("0.03"))
eth_out = Decimal("1.0")
swap_ts = "2025-08-15T10:00:00Z"
swap_value = eur(eth_out * price(swap_ts, "ETH"))
sol_in = coin(eth_out * price(swap_ts, "ETH") / price(swap_ts, "SOL"))
add(swap_ts, "swap", (eth_out, "ETH"), (sol_in, "SOL"), swap_value)
sell("2025-09-15T10:00:00Z", "SOL", sol_in)
sell("2025-12-15T10:00:00Z", "BTC", Decimal("0.05"))

tx.sort(key=lambda t: t["date_utc"])
for i, t in enumerate(tx, 1):
    t["id"] = f"T{i:02d}"
fields = ["id", "date_utc", "account", "type", "sent_amount", "sent_asset",
          "received_amount", "received_asset", "eur_value", "note"]
with open(HERE / "transactions.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for t in tx:
        w.writerow({k: str(t[k]) for k in fields})


def one_year_later(d):
    try:
        return d.replace(year=d.year + 1)
    except ValueError:  # 29 February
        return d.replace(year=d.year + 1, day=28)


# FIFO per asset. Everything sits in one account, so FIFO per wallet and
# FIFO across wallets are the same here.
lots = defaultdict(deque)  # asset -> deque of [acquired, amount, cost]
disposals, staking = [], []
for t in tx:
    d = datetime.fromisoformat(t["date_utc"].replace("Z", "+00:00")).date()
    if t["type"] == "buy":
        lots[t["received_asset"]].append([d, t["received_amount"], t["sent_amount"]])
    elif t["type"] == "staking_reward":
        lots[t["received_asset"]].append([d, t["received_amount"], t["eur_value"]])
        staking.append({"id": t["id"], "date": d.isoformat(), "eur": str(t["eur_value"])})
    else:  # sell or swap
        proceeds = t["eur_value"]
        if t["type"] == "swap":
            lots[t["received_asset"]].append([d, t["received_amount"], t["eur_value"]])
        amount, left, parts = t["sent_amount"], t["sent_amount"], []
        queue = lots[t["sent_asset"]]
        while left > 0:
            lot = queue[0]
            part = min(left, lot[1])
            cost = lot[2] * part / lot[1]
            p = proceeds * part / amount
            parts.append({"acquired": lot[0].isoformat(), "amount": str(part),
                          "cost_eur": str(eur(cost)), "proceeds_eur": str(eur(p)),
                          "gain_eur": str(eur(p - cost)),
                          "held_over_one_year": d > one_year_later(lot[0])})
            lot[1] -= part
            lot[2] -= cost
            left -= part
            if lot[1] == 0:
                queue.popleft()
        disposals.append({"id": t["id"], "date": d.isoformat(), "type": t["type"],
                          "asset": t["sent_asset"], "amount": str(amount), "lots": parts})

in_year = [x for x in disposals if x["date"].startswith(str(TAX_YEAR))]
taxable_gain = sum(Decimal(p["gain_eur"]) for x in in_year for p in x["lots"] if not p["held_over_one_year"])
tax_free_gain = sum(Decimal(p["gain_eur"]) for x in in_year for p in x["lots"] if p["held_over_one_year"])
staking_income = sum(Decimal(s["eur"]) for s in staking if s["date"].startswith(str(TAX_YEAR)))

result = {
    "tax_year": TAX_YEAR,
    "method": "FIFO, one account, no fees",
    "private_sales_section_23": {
        "gain_within_one_year_eur": str(taxable_gain),
        "gain_after_one_year_tax_free_eur": str(tax_free_gain),
        "freigrenze_eur": str(FREIGRENZE_23),
        "taxable_eur": str(taxable_gain if taxable_gain >= FREIGRENZE_23 else Decimal("0.00")),
    },
    "other_income_section_22_no_3": {
        "staking_income_eur": str(staking_income),
        "freigrenze_eur": str(FREIGRENZE_22),
        "taxable_eur": str(staking_income if staking_income >= FREIGRENZE_22 else Decimal("0.00")),
    },
    "disposals": disposals,
    "staking_rewards": staking,
}
(HERE / "expected-result.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({k: v for k, v in result.items() if k not in ("disposals", "staking_rewards")}, indent=2))
for x in disposals:
    print(x["id"], x["date"], x["type"], x["amount"], x["asset"])
    for p in x["lots"]:
        print("   ", p)
