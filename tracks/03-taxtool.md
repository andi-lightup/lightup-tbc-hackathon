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

The heaviest criterion, the quality of the tax report, is rated "good", "medium" or "poor". The prices are compared at four fixed points, although the tools price very differently: annual plans, transaction limits, per tax year, add-ons for DeFi or NFTs. A reader with 300 or 3,000 transactions a year cannot tell from four price points which tool is cheapest for them. Every criterion with its scoring rule: [full taxtool matrix](../matrices/taxtool.md).

## Test set: five tax tools

LIGHT UP has chosen five tools from its comparison for the hands-on test.

| Tool | Sign-up link |
|---|---|
| CoinTracking | https://cointracking.info/?ref=LIGHTUP |
| Blockpit | https://blockpit.cello.so/yr47XxGvXMr |
| Coinfox | https://coinfox.cello.so/HpRUP4z1Ebs |
| Divly | https://divly.com/?ref=mmvlmtc |
| Coinpanda | https://coinpanda.io/?ref=lightup |

**These are LIGHT UP affiliate links.** If you sign up or buy through one of them, LIGHT UP may receive a commission. Using them is optional; you can also open the tool's website directly. LIGHT UP enters partnerships only after a ranking is fixed, and commissions play no part in the ratings.

## Hands-on test

Test with the [taxtool sample dataset](../data/taxtool-sample/) instead of your own data: ten synthetic transactions on one exchange, with purchases, sales, a swap and staking rewards, and the expected result for 2025. All teams use the same file.

Sign up for the free version of two or three tools, import the file and note in the [hands-on test log](../templates/hands-on-test.md): how long the import takes, which errors appear, how easy the corrections are, and whether the result matches the expected one. Free versions usually let you import and review transactions, while the tax result or the report download often needs a paid plan. Note exactly what the free version shows; that is a finding for the costs category. Ask the LIGHT UP team about access to the full report.

Do not connect real exchange accounts or wallets and do not upload your own tax data. Your agent gets the public price pages and documentation; your impressions go into the prompt as text you write yourself.

## Your task

Each team takes one focus. Pick it at team formation; each focus goes to one team only.

| Team | Focus | What you do |
|---|---|---|
| Taxtool A | Costs and calculator | Define a data model for price plans (plan, price, billing period, transaction limit, what happens above it, included features, source and date). Collect the plans of the five tools, write a function that returns the cheapest suitable plan for a given number of transactions, and show the result. Propose how the cost criteria should change once a calculator exists. |
| Taxtool B | Tax report | Import the sample dataset into two or three tools and compare their result with the expected one. Propose a repeatable test that turns "good, medium, poor" for the tax report (20 points) into clear rules. |
| Taxtool C | Data import, usability and weights | Import the same file into every tool you can: what fails, how corrections work, how long it takes. Propose criteria for data import and usability, then review the weights as a whole: does the split match what matters to someone doing their first crypto tax return? |

Define every scoring rule before you look at any tool. Any display must stay neutral: it shows costs and ratings, it does not recommend a tool.

**Build option:** The cost calculator as a small React component (the LIGHT UP website runs on Next.js) or a clickable mock-up, or a checker that compares a tool's report with the expected result of the sample dataset.

## What LIGHT UP gets out of it

Revised criteria for costs, the tax report, data import and usability, results of several tools against the same sample dataset, and a data model, calculation and display concept for a cost calculator on the website. What LIGHT UP considers sound goes into the next version of the matrix, after the usual community poll.

## What to submit

Complete the [comparison submission](../templates/comparison.md):

1. The current and proposed criteria side by side, with points.
2. Results for two or three tools, with sources, dates and your hands-on test logs.
3. Your data as CSV or JSON, for example the price plans, with source and date.
4. Code, spreadsheet or mock-up, with three worked examples where it applies (for example 50, 800 and 5,000 transactions).
5. The outcome of a peer's attempt to reproduce one result using only your data and instructions.

[Schedule and voting](../README.md#schedule)
