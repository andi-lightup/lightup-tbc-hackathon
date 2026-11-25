# Crypto Wallet Comparison

**Guiding question:** What would a good software wallet comparison look like if we built it from scratch?

## Starting point

LIGHT UP tests 33 multi-coin and 11 Bitcoin-only hardware wallets. There is no comparison of software wallets yet, although many beginners start with an app on their phone, a desktop program or a browser extension.

The hardware wallet matrix shows how LIGHT UP rates today. Security carries 60 of 100 points, built from twelve criteria: registered office, year founded, data retention, Trustpilot, open-source software and hardware, secure element, two-factor authentication, multi-signature, passphrase, authenticity check, security-relevant input on the device and quantum readiness. 26 of the 60 security points go to company facts. Several criteria, such as the secure element or input on the device, do not apply to software wallets at all. [Full hardware wallet matrix](../matrices/hardware-wallet.md)

Use it as inspiration only. You may borrow from it or design a completely new matrix.

## Your task

Each team takes one focus. Pick it at team formation; each focus goes to one team only. Together the three teams produce a complete first version of the comparison.

| Team | Focus | What you do |
|---|---|---|
| Wallet A | Scope, provider list and weights | Decide which wallets belong in the comparison: self-custody only? Mobile, desktop and browser wallets in one series or several? Define inclusion rules (for example available in Germany, actively maintained, a minimum number of users), apply them and list the candidates with sources. Propose how the 100 points are split between categories. An agent can collect the public facts. |
| Wallet B | Security | Propose security criteria that fit software wallets, each with a scoring rule: for example open source, independent audits, how backup and recovery work, known vulnerabilities and how fast they were fixed. Write a short explanation for each criterion that a beginner can follow: what it is, what it protects against, what happens without it. |
| Wallet C | Usability, features and pilot | Propose criteria for usability, supported networks and coins, fees for sending and swapping, and support. Install three wallets and rate them: measure the time from download to the first receiving address and note how each wallet guides you through the backup. |

Define every scoring rule before you look at any wallet.

Test with new, empty wallets. Never type a seed phrase or private key into an agent, a chat, a screenshot or a shared document. Your agent collects public facts such as documentation, audits and app store data; your hands-on impressions go into the prompt as text you write yourself, using the [hands-on test log](../templates/hands-on-test.md).

**Build option:** An agent that collects the public facts for your provider list with source and date, or an interactive explainer that walks a beginner through the security features.

## What LIGHT UP gets out of it

A ready concept for a new software wallet comparison: scope, provider list, matrix with scoring rules and weights, a pilot on three wallets and explanation texts for the website and videos. What LIGHT UP considers sound goes to the community before the first ranking.

## What to submit

Complete the [comparison submission](../templates/comparison.md):

1. Scope and inclusion rules, with the resulting provider list and sources (Wallet A).
2. The criteria for your focus with scoring rules and points; Wallet A adds the split of the 100 points.
3. Results for three wallets, with sources, dates and your hands-on test logs (Wallet C).
4. Explanation texts for at least four criteria, each under 120 words, tested on a peer from another team (Wallet B).
5. The outcome of a peer's attempt to reproduce one result using only your instructions.

[Schedule and voting](../README.md#schedule)
