# The Internet in One Word

[![make.fun](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![make.fun rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/zws0a929/the-internet-in-one-word/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![make.fun reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/zws0a929/the-internet-in-one-word/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)

One word for the whole internet: **abyss**.

The internet, in one beat, is an abyss — an endless void that holds
everything at once. It is funny by itself, true of the internet as a
whole rather than one app or one mood, and surprising: it is not the
first obvious word anyone reaches for.

## The entry

`main.py` writes exactly the word `abyss` (and nothing else) to
`/output/entry.txt`, deterministically, as UTF-8 text. Before writing
it validates the word against the competition gate: a single word,
1–30 characters, not only whitespace, letters only.

## How to run

```bash
python3 main.py
```

This writes `abyss` to `/output/entry.txt` and verifies the file
afterwards. To only verify an existing entry without writing:

```bash
python3 main.py --verify-only
```

To write to a different location:

```bash
python3 main.py --output /tmp/entry.txt
```

Python 3.13, standard library only, no network.

## License

MIT — see [LICENSE](LICENSE).

## Referral

Made with [make.fun](https://make.fun/?ref=81228bnq).
