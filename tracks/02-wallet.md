# Crypto Wallet Comparison

**Guiding question:** What would a good software wallet comparison look like if we built it from scratch?

## Starting point

LIGHT UP tests 33 multi-coin and 11 Bitcoin-only hardware wallets. There is no comparison of software wallets yet, although many beginners start with an app on their phone, a desktop program or a browser extension.

The hardware wallet matrix shows how LIGHT UP rates today. Security carries 60 of 100 points, built from twelve criteria: registered office, year founded, data retention, Trustpilot, open-source software and hardware, secure element, two-factor authentication, multi-signature, passphrase, authenticity check, security-relevant input on the device and quantum readiness. 26 of the 60 security points go to company facts. Several criteria, such as the secure element or input on the device, do not apply to software wallets at all. [Full methodology and matrix (German)](https://lightupkryptos.de/so-testen-wir/)

## Your task

Design the comparison. The teams in this track can each take one part, or each design a complete version and compete.

1. **Scope.** Which wallets belong in the comparison? Decide whether it covers self-custody wallets only, and how mobile, desktop and browser wallets are treated: one series or several.
2. **Provider list.** Define rules for which providers get in, for example self-custody, available in Germany, actively maintained, a minimum number of users. Apply them and list the candidates with sources.
3. **Categories, criteria and weights.** Propose a matrix with 100 points, with a scoring rule for every criterion. Possible directions: open source and independent audits, how the backup and recovery works, known vulnerabilities and how fast they were fixed, supported networks and coins, fees for sending and swapping, privacy, usability for beginners and support.
4. **Pilot.** Install three wallets and rate them with your matrix. Measure the time from download to your first receiving address and note how the wallet guides you through the backup.
5. **Explanations.** For your security criteria, write a short explanation a beginner can follow: what the feature is, which attack or mistake it protects against and what happens without it.

Define every scoring rule before you look at any wallet.

Test with new, empty wallets. Never type a seed phrase or private key into an agent, a chat, a screenshot or a shared document. Your agent collects public facts such as documentation, audits and app store data; your hands-on impressions go into the prompt as text you write yourself, using the [hands-on test log](../templates/hands-on-test.md).

**Build option:** An agent that collects the public facts for your provider list with source and date, or an interactive explainer that walks a beginner through the security features.

## What LIGHT UP gets out of it

A ready concept for a new software wallet comparison: scope, provider list, matrix with scoring rules and weights, a pilot on three wallets and explanation texts for the website and videos. What LIGHT UP considers sound goes to the community before the first ranking.

## What to submit

Complete the [comparison submission](../templates/comparison.md):

1. Scope and inclusion rules, with the resulting provider list and sources.
2. The matrix with categories, criteria, scoring rules and points.
3. Results for three wallets, with sources, dates and your hands-on test logs.
4. Explanation texts for at least four criteria, each under 120 words, tested on a peer from another team.
5. The outcome of a peer's attempt to reproduce one result using only your instructions.

[Schedule and voting](../README.md#schedule)
