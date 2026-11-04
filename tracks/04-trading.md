# Crypto Trading Comparison

Which differences between derivatives platforms matter to users, and how can we measure them under comparable conditions?

## Starting point

LIGHT UP compares 23 platforms across eight categories. For liquidity, a reader needs to know which contract, trade size and time a figure represents. [Published methodology and matrices](https://lightupkryptos.de/so-testen-wir/)

## Inputs to prepare

For an order-book test, prepare timestamped snapshots from two or three public order books and the contract specifications. Use equivalent contracts and normalize units to the same order size.

## One possible pilot

Choose the same buy size and walk the ask levels until it is filled. Calculate the quantity-weighted average fill price, then compare it with the snapshot midpoint in basis points. Report trading fees separately. If visible depth is insufficient, mark the unfilled quantity. Describe the result as a simulated fill at the recorded time.

**Keeping it current.** How often would you sample to cover different market conditions? Estimate collection and review effort separately. Show how you would detect missing snapshots or changes to the interface.

**A question a newsroom could investigate.** For a fixed order size, how did estimated execution costs vary across the sampled venues and times?

## What to submit

Complete the [comparison submission](../templates/comparison.md). Show one before-and-after matrix entry, results for two or three products, the reader-facing view and the outcome of a peer’s attempt to reproduce one row. Include a maintenance plan and a source a journalist could cite. If you choose a different improvement, use the same deliverables.

[Schedule and voting](../README.md#schedule)
