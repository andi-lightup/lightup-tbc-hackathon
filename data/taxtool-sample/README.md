# Taxtool sample dataset

Ten synthetic crypto transactions for one person in Germany, with the expected result for the tax year 2025. All teams in the [taxtool track](../../tracks/03-taxtool.md) import the same file, so their results can be compared with each other and with the expected result. The transactions are invented; the market prices are real. The dataset stays below the transaction limits of the tools' free versions.

| File | Content |
|---|---|
| `transactions.csv` | The ten transactions in a neutral format |
| `expected-result.json` | Expected result with every sale and the purchases it uses |
| `prices.csv` | Daily volume-weighted average prices in EUR from the Kraken public API, December 2024 to December 2025 |
| `build.py` | Builds the transactions and the expected result from `prices.csv`: `python3 build.py` |

## The transactions

Everything happens on one exchange, "Exchange A", without fees.

| ID | Date | What happens |
|---|---|---|
| T01 | 02.12.2024 | Buy 0.05 BTC for €4,565.80 |
| T02 | 15.04.2025 | Buy 0.04 BTC for €3,017.61 |
| T03 | 15.04.2025 | Buy 1.0 ETH for €1,436.42 |
| T04–T06 | 01.05., 01.06., 01.07.2025 | Staking rewards of 0.003 ETH each, worth €4.89, €6.64 and €6.18 |
| T07 | 15.07.2025 | Sell 0.03 BTC for €3,017.06 |
| T08 | 15.08.2025 | Swap 1.0 ETH into 23.76701845 SOL, worth €3,850.97 |
| T09 | 15.09.2025 | Sell all SOL for €4,757.44 |
| T10 | 15.12.2025 | Sell 0.05 BTC for €3,720.19 |

## What a free version can check

The free versions of most tools let you import and review transactions and show a portfolio, but not the tax result. Two checks work without paying:

1. **Every transaction is recognised correctly:** ten transactions, with the right type (buy, sell, swap, staking reward), amounts, dates and euro values.
2. **The holdings on 31.12.2025 match:**

| Asset | Amount | Cost basis |
|---|---|---|
| BTC | 0.01 | €754.40 (the rest of T02) |
| ETH | 0.009 | €17.71 (the three staking rewards) |
| SOL | 0 | €0.00 |

## Expected tax result for 2025

This needs a tool's paid tax report. It is the reference for a later full test and for designing the report test.

| Sale | Coins used (FIFO) | Gain | Taxable? |
|---|---|---|---|
| T07: 0.03 BTC | 0.03 from T01, held 7 months | €277.58 | Yes |
| T08: swap of 1.0 ETH | 1.0 from T03, held 4 months | €2,414.55 | Yes |
| T09: 23.767 SOL | all from T08, held 1 month | €906.47 | Yes |
| T10: 0.05 BTC | 0.02 from T01, held more than one year | −€338.24 | No, tax-free, the loss cannot be offset |
| T10: 0.05 BTC | 0.03 from T02, held 8 months | −€31.09 | Yes |

| Item | Amount |
|---|---|
| Gains from private sales held one year or less (section 23 EStG) | €3,567.51 |
| Above the €1,000 Freigrenze, so taxable in full | €3,567.51 |
| Staking income (section 22 no. 3 EStG) | €17.71 |
| Below the €256 Freigrenze, so tax-free | €0.00 |

## Rules applied

- First in, first out (FIFO), as in the Federal Ministry of Finance (BMF) letter on crypto assets of 6 March 2025. All coins sit in one account, so FIFO per wallet and across wallets give the same result.
- Coins held for more than one year are sold tax-free; losses on them cannot be offset.
- A swap counts as a sale of the coin given away at its market value, which is also the acquisition cost of the coin received.
- Staking rewards are income at their market value on receipt and become new coins with that acquisition cost.
- The €1,000 and €256 limits are Freigrenzen: below them nothing is taxable, from them everything is.

The rules were checked against the BMF letter and sections 22 and 23 EStG. This is a test dataset, not tax advice.

## Differences you may see

- Tax tools value swaps and staking rewards with their own prices, often to the minute, while this dataset uses daily averages. Small differences on T04–T06, T08 and T09 are expected. A difference of more than 1% on a figure, or a different treatment (for example T10's tax-free part counted as taxable, or the staking income missing), counts as an error.
- `transactions.csv` uses a neutral format. Each tool has its own import template, so the file has to be converted first. How easily that works is part of the test.
