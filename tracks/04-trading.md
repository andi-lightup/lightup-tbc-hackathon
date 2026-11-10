# Crypto Trading Comparison

**Guiding question:** How can we measure the fees and liquidity of crypto derivatives platforms so that they reflect real trading costs, and keep them current with a script?

## Starting point

LIGHT UP compares 23 platforms in eight categories. Fees and liquidity together carry 34 of 100 points:

| Criterion | Scoring | Max. points |
|---|---|---|
| Futures trading fees (average of maker and taker fee) | Cheapest platform: full points · most expensive: 0 · others: pro rata | 22 |
| Average 24-hour trading volume over three days | Over USD 20 bn: full points · 10–20 bn: 10 · 5–10 bn: 8 · 1–5 bn: 6 · 0.5–1 bn: 4 · 100–500 m: 2 · under 100 m: 0 | 12 |

Both criteria are easy to collect, but they leave out what a trader actually pays. The fee criterion averages maker and taker fees, although many retail orders are market orders that pay the taker fee. Trading volume says little about whether a given order fills close to the quoted price, and reported volume can be inflated. Spread and slippage do not appear at all. [Full methodology and matrix (German)](https://lightupkryptos.de/so-testen-wir/)

## Your task

Propose better fee and liquidity criteria, and show that they can be measured with reasonable effort. Questions to work through:

- **Maker and taker:** Does the average make sense? Should the taker fee weigh more, and if so, why and by how much?
- **Spread:** How do you measure it comparably across platforms: which contract, which time, how many samples?
- **Slippage:** For a fixed order size, walk the order book until the order is filled. Compare the average fill price with the midpoint in basis points, and report fees separately. Mark any quantity the visible book cannot fill.
- **Volume or depth:** Should order-book depth replace or complement trading volume?

Then build a small script that collects the data from public sources, without API keys, for two or three platforms and the same contract (for example the BTC/USDT perpetual). It writes a dated CSV that LIGHT UP can rerun.

## What LIGHT UP gets out of it

Fee and liquidity criteria that reflect real trading costs, and a script LIGHT UP can run regularly with manageable effort, so the website always shows current figures. What LIGHT UP considers sound goes into the next version of the matrix, after the usual community poll.

## What to submit

Complete the [comparison submission](../templates/comparison.md):

1. The current and proposed criteria side by side, with scoring rules and points.
2. The script with a short README: inputs, how to run it, output columns.
3. A sample CSV for two or three platforms, with timestamps.
4. A maintenance plan: how often to sample, how long a run takes, how to notice missing data or a changed interface.
5. The outcome of a peer's attempt to rerun the script using only your instructions.

[Schedule and voting](../README.md#schedule)
