# Crypto Wallet Comparison

**Guiding question:** How can we improve the security rating of hardware wallets, and explain its criteria so that a beginner understands why they matter?

## Starting point

LIGHT UP tests 33 multi-coin and 11 Bitcoin-only devices in two separate series. Security is by far the largest category. In the published matrix it carries 60 of 100 points, built from twelve criteria:

| Criterion | Scoring | Max. points |
|---|---|---|
| Registered office | DACH, Luxembourg, Liechtenstein: full points · Europe: 6 · USA/Canada: 4 · other reputable: 2 · offshore: 0 | 8 |
| Year founded | Before 2016: full points · after 2024: 0 · in between: pro rata | 12 |
| Data retention | Under 1 month: 4 · 1–6 months: 2 · 6–12 months: 1 · over 12 months: 0 | 4 |
| Trustpilot | Points based on rating and number of reviews | 6 |
| Open source | Open-source software: 6 · open-source hardware: 6 | 12 |
| Secure element | EAL6+ or higher: full points · EAL5+: 4 · other chip: 2 · none: 0 | 5 |
| Two-factor authentication | Yes: full points · no: 0 | 2 |
| Multi-signature | Yes: full points · no: 0 | 2 |
| Passphrase | Yes: full points · no: 0 | 2 |
| Authenticity check | Yes: full points · no: 0 | 2 |
| All security-relevant input on the device | Yes: full points · no: 0 | 4 |
| Quantum-ready | Yes: full points · no: 0 | 1 |

Bitcoin-only devices are rated without the categories asset support and features, out of 80 points. The two series are not comparable with each other. [Full methodology and matrix (German)](https://lightupkryptos.de/so-testen-wir/)

## Your task

Work on two things. You can split the team.

**1. A better security rating.** 26 of the 60 security points go to company facts (office, age, reviews), and many technical features are a plain yes or no worth 2 points. Is that the right balance? Possible directions:

- Which features deserve more than a yes or no? A passphrase that is easy to set up protects more people than one hidden in an advanced menu.
- What does two-factor authentication mean for a hardware wallet, and is the criterion defined clearly enough to apply?
- What is missing? For example independent security audits, a public bug bounty, known vulnerabilities and how fast they were fixed, or how long a device receives firmware updates.
- Does a criterion apply to both series, or only to one?

**2. Explanations readers understand.** For the security criteria, write a short explanation that a beginner can follow: what the feature is, which attack or mistake it protects against, and what happens without it. Start with multi-signature, passphrase, two-factor authentication and the secure element.

Define every scoring rule before you look at any device. Apply it to two or three devices using public manufacturer documentation. A physical device is only needed if your claim depends on hands-on testing.

## What LIGHT UP gets out of it

A security rating with clearer criteria and better-argued weights, plus explanation texts LIGHT UP can use on the website and in videos. What LIGHT UP considers sound goes into the next version of the matrix, after the usual community poll.

## What to submit

Complete the [comparison submission](../templates/comparison.md):

1. The current and proposed security criteria side by side, with points per criterion.
2. Results for two or three devices, with sources and dates.
3. Explanation texts for at least four criteria, each under 120 words, tested on a peer from another team.
4. The outcome of a peer's attempt to reproduce one result using only your instructions.

[Schedule and voting](../README.md#schedule)
