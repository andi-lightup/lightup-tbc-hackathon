# Crypto Trading Comparison

**Guiding question:** How can we measure the trading costs and liquidity of crypto derivatives platforms reproducibly, and keep them current with a script?

## Starting point

LIGHT UP compares 23 platforms in eight categories. The matrix used in this workshop goes live on the LIGHT UP website before the event. Costs & transparency carry 21 % of the rating, liquidity 10 %:

| Category | Criterion | Scoring | Weight |
|---|---|---|---|
| Costs & transparency | Deposit fees | Up to €2.50: full points · from €20: 0 | 2 % |
| | Maker fee | 0 % or less: full points · from 0.05 %: 0 · in between: pro rata | 5 % |
| | Taker fee | Up to 0.03 %: full points · from 0.10 %: 0 · in between: pro rata | 9 % |
| | Withdrawal fees | Recorded, not scored | 0 % |
| | Funding level (daily average over 30 days) | Lowest: full points · highest: 0 · others: pro rata | 0 % |
| | Transparency | 1.25 points each for a public fee page, a public funding rate, disclosed liquidation rules and clearly stated deposit costs | 5 % |
| Liquidity | Slippage | Lowest deviation: full points · highest: 0 · others: pro rata | 10 % |

The taker fee weighs more than the maker fee. Slippage replaces trading volume as the liquidity measure. What the matrix does not yet define is how slippage is measured: for which contract, which order size, at what time and from how many samples. Funding is recorded but not yet scored. [Full methodology and matrix (German)](https://lightupkryptos.de/so-testen-wir/)

## Your task

Turn the cost and liquidity criteria into measurements anyone can repeat. Questions to work through:

- **Slippage:** For a fixed order size, walk the order book until the order is filled. Compare the average fill price with the midpoint in basis points, and report fees separately. Which contract and order sizes are fair across all platforms? How many snapshots at which times cover different market conditions? Mark any quantity the visible book cannot fill.
- **Spread:** Should the spread be shown separately, or is it covered by slippage measured from the midpoint?
- **Maker and taker:** Is the 9 : 5 ratio right? Are the thresholds (0.03 % and 0.10 % for takers, 0 % and 0.05 % for makers) sensible for today's market?
- **Funding:** Should the funding level count, and how do you compare it fairly when platforms settle at different intervals?

Then build a small script that collects the data from public sources, without API keys, for two or three platforms and the same contract (for example the BTC/USDT perpetual). It writes a dated CSV that LIGHT UP can rerun.

## What LIGHT UP gets out of it

A documented method for slippage and, if it proves sound, for funding, plus a script LIGHT UP can run regularly with manageable effort, so the website always shows current figures. What LIGHT UP considers sound goes into the next version of the matrix, after the usual community poll.

## What to submit

Complete the [comparison submission](../templates/comparison.md):

1. The measurement method: contract, order sizes, timing, number of samples and the scoring rule.
2. The script with a short README: inputs, how to run it, output columns.
3. A sample CSV for two or three platforms, with timestamps.
4. A maintenance plan: how often to sample, how long a run takes, how to notice missing data or a changed interface.
5. The outcome of a peer's attempt to rerun the script using only your instructions.

[Schedule and voting](../README.md#schedule)
