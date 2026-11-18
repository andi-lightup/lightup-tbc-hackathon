# Crypto Taxtool Comparison

**Guiding question:** How can we improve the crypto tax tool comparison as a whole, including how it rates prices?

## Starting point

LIGHT UP compares 13 tools. The matrix has seven categories and 100 points:

| Category | Criteria today | Points |
|---|---|---|
| Features | Quality of the tax report 20 · portfolio tracking 5 · reports for previous years 2 · individual tax advice 2 · WISO integration 2 | 31 |
| Security | Registered office 5 · year founded 5 · Trustpilot 5 | 15 |
| Costs | Free version 2 · lifetime licence 2 · price for 100, 1,000, 10,000 and unlimited transactions 2.5 each | 14 |
| Usability | User interface 5 · app and desktop 2 · German language 5 | 12 |
| Market coverage | Supported blockchains, exchanges and wallets 3 · coverage of the top 10 4 · NFT and DeFi support 3 | 10 |
| Data import | Import methods 5 · automatic sync and permanent API connection 2 · display of import errors 1 · manual corrections 2 | 10 |
| Customer support | Response time, quality and language | 8 |

The heaviest criterion, the quality of the tax report, is rated "good", "medium" or "poor". The prices are compared at four fixed points, although the tools price very differently: annual plans, transaction limits, per tax year, add-ons for DeFi or NFTs. A reader with 300 or 3,000 transactions a year cannot tell from four price points which tool is cheapest for them. [Full methodology and matrix (German)](https://lightupkryptos.de/so-testen-wir/)

## Hands-on test

Test with a shared sample dataset instead of your own data. LIGHT UP provides it before the event: synthetic transactions across several exchanges and a wallet, with purchases, sales, a swap and staking rewards, together with the expected taxable result. All teams use the same file.

Sign up for the free version or trial of two or three tools, import the file and note in the [hands-on test log](../templates/hands-on-test.md): time to the first report, import errors, how easy the corrections are, and whether the report matches the expected result. Do not connect real exchange accounts or wallets and do not upload your own tax data. Your agent gets the public price pages and documentation; your impressions go into the prompt as text you write yourself.

## Your task

Choose one or two categories as your team's focus and propose a better version, with scoring rules and points. The other teams in your track take other categories. Possible directions:

- **Costs and calculator:** Define a data model for price plans (plan, price, billing period, transaction limit, what happens above it, included features, source and date), collect the plans of at least five tools and write a function that returns the cheapest suitable plan for a given number of transactions. Then propose how the cost criteria should change once such a calculator exists.
- **Report quality:** Can the sample dataset with its known result turn "good, medium, poor" into a repeatable test?
- **Data import and market coverage:** Does the same file import cleanly everywhere? Are the exchanges and wallets German users actually use supported?
- **The weights as a whole:** Does the split between features, costs, usability and security match what matters to someone doing their first crypto tax return?

Define every scoring rule before you look at any tool. Any display must stay neutral: it shows costs and ratings, it does not recommend a tool.

**Build option:** The cost calculator as a small React component (the LIGHT UP website runs on Next.js) or a clickable mock-up, or a checker that compares a tool's report with the expected result of the sample dataset.

## What LIGHT UP gets out of it

Revised criteria for the categories the teams chose, results of several tools against the same sample dataset, and a data model, calculation and display concept for a cost calculator on the website. What LIGHT UP considers sound goes into the next version of the matrix, after the usual community poll.

## What to submit

Complete the [comparison submission](../templates/comparison.md):

1. The current and proposed criteria side by side, with points.
2. Results for two or three tools, with sources, dates and your hands-on test logs.
3. Your data as CSV or JSON, for example the price plans, with source and date.
4. Code, spreadsheet or mock-up, with three worked examples where it applies (for example 50, 800 and 5,000 transactions).
5. The outcome of a peer's attempt to reproduce one result using only your data and instructions.

[Schedule and voting](../README.md#schedule)
