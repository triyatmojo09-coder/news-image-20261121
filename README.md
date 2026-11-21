[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/triyatmojo09-coder/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/triyatmojo09-coder/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# THE WORLD TODAY — Saturday, 21 November 2026

Entry for the make.fun competition **news-image-20261121**
("Sum up 21 November's world news in one image", $100 prize pool).

One newspaper-style front page that sums up the world news of
**Saturday 21 November 2026** in a single 1024×1024 image. The date is
printed large in the date bar under the masthead, the day's biggest
story leads the page, and five further panels cover the rest of the
day across regions and topics — all readable at a glance.

## The day's stories shown

1. **Lead — Russian missile hits Poland.** A Russian missile struck
   Polish territory during a strike on Ukraine; Warsaw sought NATO
   support, Danish Gripen jets were deployed, and PM Tusk responded.
   Illustrated with a simple Poland–Ukraine map and an impact starburst.
2. **Shenzhen summit ends.** Trump, Putin and Xi agreed to push UN
   reform, oil supply and nuclear risk-reduction dialogue; Trump then
   called European allies about Ukraine.
3. **ICJ: Myanmar genocide.** The International Court of Justice found
   Myanmar committed genocide against the Rohingya; Myanmar and China
   rejected the ruling.
4. **Tech stocks plunge.** Technology/AI shares fell sharply, led by
   Anthropic's drop. In a separate small note in the same panel,
   Anthropic's AI solved a major mathematics problem.
5. **Climate talks on edge.** UN climate negotiations entered a
   critical phase with no agreement in sight.
6. **IEA: no way back on energy.** The IEA said there is no return to
   the world before the Iran-war energy shock — the global energy map
   has changed permanently.

Stories were verified against press coverage published on
21 November 2026 before the front page was composed. Summaries are
kept short and faithful to the reporting, without exaggeration.

## How it runs

`main.py` (Python 3, standard library only, no network) validates
`entry.png` — PNG signature, at most 1 MiB, at most 1024×1024 pixels —
and copies it byte-for-byte to `/output/entry.png`
(or to `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set,
which is how it is tested locally). Two runs produce identical bytes.

```sh
python3 main.py                          # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `entry.png` — the finished front-page image (1024×1024, ~108 KiB).
- `main.py` — the entry program submitted to the competition.
- `make_frontpage.py` — build-only generator that drew `entry.png`
  with Pillow and the system DejaVu fonts; not used at run time.
- `LICENSE` — MIT license.
