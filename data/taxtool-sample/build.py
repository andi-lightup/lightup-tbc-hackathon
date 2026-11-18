"""Build the taxtool sample dataset and its expected result.

Reads prices.csv (daily volume-weighted average prices from the Kraken public
OHLC API), writes transactions.csv and expected-result.json, and prints the
expected result. Run: python3 build.py
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
FEE_RATE = Decimal("0.0025")  # trading fee in EUR on buys and sells

prices = {}
with open(HERE / "prices.csv") as f:
    for row in csv.DictReader(f):
        prices[(row["date_utc"], row["asset"])] = Decimal(row["vwap"])


def eur(x):
    return x.quantize(CENT, ROUND_HALF_UP)


def coin(x):
    return x.quantize(SAT, ROUND_HALF_UP)


tx = []


def add(ts, account, kind, sent=("", ""), received=("", ""), fee=("", ""), value="", note=""):
    tx.append({
        "id": f"T{len(tx) + 1:02d}",
        "date_utc": ts,
        "account": account,
        "type": kind,
        "sent_amount": sent[0], "sent_asset": sent[1],
        "received_amount": received[0], "received_asset": received[1],
        "fee_amount": fee[0], "fee_asset": fee[1],
        "eur_value": value,
        "note": note,
    })


def buy(ts, account, asset, amount, note=""):
    p = prices[(ts[:10], asset)]
    cost = eur(amount * p)
    add(ts, account, "buy", (cost, "EUR"), (amount, asset), (eur(cost * FEE_RATE), "EUR"), cost, note)


def buy_eur(ts, account, asset, cost, note=""):
    p = prices[(ts[:10], asset)]
    add(ts, account, "buy", (cost, "EUR"), (coin(cost / p), asset), (eur(cost * FEE_RATE), "EUR"), cost, note)


def sell(ts, account, asset, amount, note=""):
    p = prices[(ts[:10], asset)]
    gross = eur(amount * p)
    add(ts, account, "sell", (amount, asset), (gross, "EUR"), (eur(gross * FEE_RATE), "EUR"), gross, note)


# Bitcoin: one purchase in 2024, a monthly savings plan, one purchase in 2025,
# a sale within one year and a sale that is partly after one year.
buy("2024-12-02T10:15:00Z", "Börse A", "BTC", Decimal("0.05"))
for m in range(1, 13):
    buy_eur(f"2025-{m:02d}-05T09:00:00Z", "Börse A", "BTC", Decimal("50.00"), "Sparplan")
buy("2025-04-15T16:40:00Z", "Börse A", "BTC", Decimal("0.04"))
sell("2025-07-15T14:20:00Z", "Börse A", "BTC", Decimal("0.03"))
sell("2025-12-15T15:45:00Z", "Börse A", "BTC", Decimal("0.05"))

# Ether: purchase, transfer to an own wallet, monthly staking rewards there.
buy("2025-04-15T11:05:00Z", "Börse B", "ETH", Decimal("2.0"))
v = eur(Decimal("1.5") * prices[("2025-04-20", "ETH")])
add("2025-04-20T18:00:00Z", "Börse B", "transfer_out", (Decimal("1.5"), "ETH"), value=v, note="to own wallet; network fee set to 0")
add("2025-04-20T18:10:00Z", "Wallet", "transfer_in", received=(Decimal("1.5"), "ETH"), value=v, note="from Börse B")
for m in range(5, 13):
    d = f"2025-{m:02d}-01"
    amt = Decimal("0.00375")
    add(f"{d}T00:00:00Z", "Wallet", "staking_reward", received=(amt, "ETH"), value=eur(amt * prices[(d, "ETH")]))

# Swap of the ether left on the exchange into Solana, then sale of the Solana.
eth_out = Decimal("0.5")
swap_value = eur(eth_out * prices[("2025-08-15", "ETH")])
sol_in = coin(eth_out * prices[("2025-08-15", "ETH")] / prices[("2025-08-15", "SOL")])
add("2025-08-15T13:30:00Z", "Börse B", "swap", (eth_out, "ETH"), (sol_in, "SOL"), value=swap_value, note="no fee")
sell("2025-09-15T10:00:00Z", "Börse B", "SOL", sol_in)
tx.sort(key=lambda t: t["date_utc"])
for i, t in enumerate(tx, 1):
    t["id"] = f"T{i:02d}"

with open(HERE / "transactions.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(tx[0].keys()))
    w.writeheader()
    for t in tx:
        w.writerow({k: (str(v) if v != "" else "") for k, v in t.items()})


# FIFO calculation. scope="global": one queue per asset;
# scope="account": one queue per asset and account (transfers move lots).
def one_year_later(d):
    try:
        return d.replace(year=d.year + 1)
    except ValueError:  # 29 February
        return d.replace(year=d.year + 1, day=28)


def calculate(scope):
    lots = defaultdict(deque)  # key -> deque of [acq_date, amount, cost]
    disposals, staking = [], []

    def key(asset, account):
        return asset if scope == "global" else (asset, account)

    def take(k, amount):
        used, left = [], amount
        while left > 0:
            lot = lots[k][0]
            part = min(left, lot[1])
            cost = lot[2] * part / lot[1]
            used.append((lot[0], part, cost))
            lot[1] -= part
            lot[2] -= cost
            left -= part
            if lot[1] == 0:
                lots[k].popleft()
        return used

    for t in tx:
        d = datetime.fromisoformat(t["date_utc"].replace("Z", "+00:00")).date()
        kind = t["type"]
        if kind == "buy":
            lots[key(t["received_asset"], t["account"])].append(
                [d, t["received_amount"], t["sent_amount"] + t["fee_amount"]])
        elif kind == "staking_reward":
            lots[key(t["received_asset"], t["account"])].append([d, t["received_amount"], t["eur_value"]])
            staking.append((t["id"], d, t["eur_value"]))
        elif kind == "transfer_out" and scope == "account":
            in_transit = take(key(t["sent_asset"], t["account"]), t["sent_amount"])
        elif kind == "transfer_in" and scope == "account":
            # Moved lots keep their acquisition date; merge them back in date order.
            k = key(t["received_asset"], t["account"])
            merged = sorted(list(lots[k]) + [[a, p, c] for a, p, c in in_transit], key=lambda lot: lot[0])
            lots[k] = deque(merged)
        elif kind in ("sell", "swap"):
            if kind == "sell":
                proceeds = t["received_amount"] - t["fee_amount"]
            else:
                proceeds = t["eur_value"]
                lots[key(t["received_asset"], t["account"])].append([d, t["received_amount"], t["eur_value"]])
            amount = t["sent_amount"]
            parts = []
            for acq, part, cost in take(key(t["sent_asset"], t["account"]), amount):
                p = proceeds * part / amount
                taxable = d <= one_year_later(acq)
                parts.append({"acquired": acq.isoformat(), "amount": str(part), "cost_eur": str(eur(cost)),
                              "proceeds_eur": str(eur(p)), "gain_eur": str(eur(p - cost)),
                              "held_over_one_year": not taxable})
            disposals.append({"id": t["id"], "date": d.isoformat(), "type": kind,
                              "asset": t["sent_asset"], "amount": str(amount), "lots": parts})
    return disposals, staking


g_disp, g_stake = calculate("global")
a_disp, a_stake = calculate("account")
assert json.dumps(g_disp) == json.dumps(a_disp), "global and per-account FIFO differ"

taxable_gain = sum(Decimal(p["gain_eur"]) for x in g_disp if x["date"].startswith(str(TAX_YEAR))
                   for p in x["lots"] if not p["held_over_one_year"])
tax_free_gain = sum(Decimal(p["gain_eur"]) for x in g_disp if x["date"].startswith(str(TAX_YEAR))
                    for p in x["lots"] if p["held_over_one_year"])
staking_income = sum(v for _, d, v in g_stake if d.year == TAX_YEAR)

result = {
    "tax_year": TAX_YEAR,
    "method": "FIFO; global and per-account FIFO give the same result for this dataset",
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
    "disposals": g_disp,
}
(HERE / "expected-result.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "disposals"}, indent=2, ensure_ascii=False))
for x in g_disp:
    print(x["id"], x["date"], x["type"], x["amount"], x["asset"])
    for p in x["lots"]:
        print("   ", p)
