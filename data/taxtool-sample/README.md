# Taxtool sample dataset

**Status: draft. The expected result has not yet been reviewed by a tax expert.**

A synthetic set of 29 crypto transactions for one person in Germany, with the expected result for the tax year 2025. All teams in the [taxtool track](../../tracks/03-taxtool.md) import the same file, so their results can be compared with each other and with the expected result. The transactions are invented; the market prices are real.

| File | Content |
|---|---|
| `transactions.csv` | The 29 transactions in a neutral format |
| `expected-result.json` | Expected result with every disposal and the lots it uses |
| `prices.csv` | Daily volume-weighted average prices in EUR from the Kraken public API, December 2024 to December 2025 |
| `build.py` | Builds the transactions and the expected result from `prices.csv`: `python3 build.py` |

## What happens in the dataset

- **Bitcoin on Börse A:** a purchase in December 2024, a savings plan of €50 every month in 2025, another purchase in April 2025, a sale in July 2025 and a sale in December 2025. Part of the December sale comes from coins held for more than one year.
- **Ether on Börse B:** a purchase in April 2025 and a transfer of 1.5 ETH to an own wallet, which then receives monthly staking rewards.
- **Swap:** the remaining 0.5 ETH on Börse B is swapped into Solana in August 2025, and the Solana is sold in September 2025.

## Expected result for 2025

| Item | Amount |
|---|---|
| Gains from private sales held one year or less (section 23 EStG) | €1,848.38 |
| Loss from sales held more than one year (not taxable, not deductible) | −€346.53 |
| Taxable private sales after the €1,000 Freigrenze | €1,848.38 |
| Staking income (section 22 no. 3 EStG) | €83.09 |
| Taxable staking income after the €256 Freigrenze | €0.00 |

| Disposal | Date | Gain within one year |
|---|---|---|
| T16: sale of 0.03 BTC | 15.07.2025 | €263.19 |
| T19: swap of 0.5 ETH into SOL | 15.08.2025 | €1,205.49 |
| T22: sale of 11.88350923 SOL | 15.09.2025 | €447.28 |
| T29: sale of 0.05 BTC, part held one year or less | 15.12.2025 | −€67.58 |

## Assumptions

- First in, first out (FIFO), as in the Federal Ministry of Finance (BMF) letter on crypto assets. FIFO per account and FIFO across all accounts give the same result for this dataset; `build.py` checks this.
- Coins held for more than one year are sold tax-free; losses on them are not deductible.
- A swap counts as a sale of the coin given away at its market value, which is also the acquisition cost of the coin received.
- Fees on purchases increase the acquisition cost; fees on sales reduce the proceeds.
- Staking rewards are income at their market value on receipt. They are below the €256 Freigrenze, so they are tax-free; a good report still shows them.
- The €1,000 Freigrenze for private sales applies to the net gain of the year. The gain is above it, so it is taxable in full.

## Simplifications

- All trading fees are paid in euros, the swap has no fee and the network fee for the transfer is set to zero. This avoids open questions about fees paid in crypto.
- Market values are daily averages. Tax tools value swaps and staking rewards with their own price data, often to the minute, so small differences on these items are expected. As a guide: a difference of more than 1% on a figure, or a different treatment (for example the tax-free part counted as taxable, or staking income missing), counts as an error.
- `transactions.csv` uses a neutral format. Each tool has its own import template, so the file has to be converted first. How easily that works is part of the test.

## Before the event

Have a tax expert review the expected result and the assumptions, then remove the draft note at the top.
