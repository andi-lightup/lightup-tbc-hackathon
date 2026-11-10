# Crypto Taxtool Comparison

**Guiding question:** How can we improve the cost rating so that readers can find out which tool is cheapest for their number of transactions?

## Starting point

LIGHT UP compares 13 tools in seven categories. Costs carry 14 of 100 points:

| Criterion | Scoring | Max. points |
|---|---|---|
| Free version | Yes: 2 · no: 0 | 2 |
| Lifetime licence | Yes: 2 · no: 0 | 2 |
| Price for 100 transactions | Cheapest tool: 2.5 · most expensive: 0 · others: pro rata · not possible: 0 | 2.5 |
| Price for 1,000 transactions | as above | 2.5 |
| Price for 10,000 transactions | as above | 2.5 |
| Price for unlimited transactions | as above | 2.5 |

The tools price very differently: annual plans, transaction limits, per tax year, add-ons for DeFi or NFTs. A reader with 300 or 3,000 transactions a year cannot tell from four fixed price points which tool is cheapest for them. [Full methodology and matrix (German)](https://lightupkryptos.de/so-testen-wir/)

## Your task

Build the basis for a calculator on the LIGHT UP website: a reader enters their yearly number of transactions and sees what each tool would cost them, next to its LIGHT UP rating.

1. **Data model.** Define how a price plan is stored so that every tool fits: plan name, price, billing period, transaction limit, what happens above the limit, included features, source and date.
2. **Price data.** Collect the current public price plans for at least five tools into that model.
3. **Calculation.** Write a function that returns the cheapest suitable plan per tool for a given number of transactions. Decide how to handle edge cases: limits per tax year, features only in higher plans, prices in other currencies.
4. **Display.** Sketch or prototype how the result appears on the website. The site runs on Next.js, so a small React component is directly reusable, but a clickable mock-up is fine too.
5. **Scoring.** Propose whether the cost criteria should change once a calculator exists, for example by scoring the price ranges LIGHT UP viewers actually use.

The display must stay neutral: it shows costs and ratings, it does not recommend a tool.

## What LIGHT UP gets out of it

A dataset, a calculation and a display concept that LIGHT UP can build into the website, so readers get a cost comparison for their own situation instead of four fixed price points.

## What to submit

Complete the [comparison submission](../templates/comparison.md):

1. The data model and the price data as CSV or JSON, with source and date per plan.
2. The calculation as code or a spreadsheet, with three worked examples (for example 50, 800 and 5,000 transactions).
3. The mock-up or prototype.
4. A proposal for the cost criteria, with its effect on two or three tools.
5. The outcome of a peer's attempt to reproduce one result using only your data and instructions.

[Schedule and voting](../README.md#schedule)
