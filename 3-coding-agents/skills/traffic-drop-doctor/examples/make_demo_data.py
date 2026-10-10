#!/usr/bin/env python3
"""Generate a realistic, FICTIONAL Search Console export for the demo site trailpeak.example.

Planted causes (the analyzer should find all three):
  1. /deals/   accidentally noindexed by a deploy on 2026-09-06 → pages drop to zero impressions
  2. /reviews/ lose rankings in a (fictional, demo) core update rolling out 2026-09-03 → 2026-09-18
  3. /guides/  informational queries keep positions but lose CTR (AI Overviews appearing)
Brand traffic stays flat. Output: demo-export/ (compare CSVs) + Dates.csv + events.csv
"""
import csv
import os
import random
from datetime import date, timedelta

random.seed(7)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "demo-export")
os.makedirs(OUT, exist_ok=True)
SITE = "https://trailpeak.example"
AFTER = (date(2026, 9, 6), date(2026, 10, 3))
BEFORE = (date(2026, 8, 9), date(2026, 9, 5))
START = date(2025, 6, 1)

TOPICS = ["hiking boots", "tent", "sleeping bag", "backpack", "trekking poles", "rain jacket",
          "camping stove", "headlamp", "water filter", "trail runners", "hammock", "base layer",
          "down jacket", "camp chair", "gps watch", "cooler", "sleeping pad", "bear canister"]
pages = []  # (url, section, base_clicks/day, base_ctr, base_pos, [queries])
for t in TOPICS:
    slug = t.replace(" ", "-")
    pages.append((f"{SITE}/guides/how-to-choose-{slug}/", "guides", random.uniform(18, 60), random.uniform(0.045, 0.08), random.uniform(2.2, 4.5),
                  [f"how to choose {t}", f"what {t} do i need", f"how to choose a {t} for beginners", f"{t} buying guide", f"how to clean {t}"]))
    pages.append((f"{SITE}/reviews/best-{slug}/", "reviews", random.uniform(25, 70), random.uniform(0.06, 0.10), random.uniform(2.5, 4.8),
                  [f"best {t}", f"best {t} 2026", f"{t} reviews", f"top rated {t}"]))
for t in TOPICS[:12]:
    slug = t.replace(" ", "-")
    pages.append((f"{SITE}/deals/{slug}-deals/", "deals", random.uniform(10, 28), random.uniform(0.07, 0.11), random.uniform(3, 6),
                  [f"{t} deals", f"{t} sale", f"cheap {t}"]))
pages.append((f"{SITE}/", "home", 140, 0.42, 1.1, ["trailpeak", "trailpeak outdoors", "trailpeak gear"]))
pages.append((f"{SITE}/about/", "home", 12, 0.30, 1.3, ["trailpeak reviews", "trailpeak about"]))


def season(d):  # summer peak, mild weekly cycle
    doy = d.timetuple().tm_yday
    import math
    return (1 + 0.18 * math.sin((doy - 100) / 365 * 2 * math.pi)) * (0.92 if d.weekday() >= 5 else 1.03)


def ramp(d, start, end):
    if d < start:
        return 0.0
    if d >= end:
        return 1.0
    return (d - start).days / max(1, (end - start).days)


def multipliers(section, d):
    """Return (impressions_mult, ctr_mult, position_delta)."""
    if section == "deals":
        return (0.0, 1.0, 0.0) if d >= date(2026, 9, 9) else (1.0, 1.0, 0.0)
    if section == "reviews":
        r = ramp(d, date(2026, 9, 4), date(2026, 9, 17))
        return (1 - 0.30 * r, 1 - 0.55 * r, 5.2 * r)
    if section == "guides":
        r = ramp(d, date(2026, 8, 30), date(2026, 9, 14))
        return (1.02, 1 - 0.47 * r, 0.2 * r)
    return (1.0, 1.0, 0.0)


days = [START + timedelta(days=i) for i in range((AFTER[1] - START).days + 1)]
page_daily = {}
for url, sec, bc, ctr, pos, qs in pages:
    rows = []
    for d in days:
        im, cm, pd_ = multipliers(sec, d)
        impr = bc / ctr * season(d) * im * random.uniform(0.9, 1.1)
        clicks = impr * ctr * cm * random.uniform(0.92, 1.08)
        rows.append((d, clicks, impr, pos + pd_ + random.uniform(-0.3, 0.3)))
    page_daily[url] = rows


def window(rows, w):
    sel = [r for r in rows if w[0] <= r[0] <= w[1]]
    c = sum(r[1] for r in sel); i = sum(r[2] for r in sel)
    p = sum(r[3] * r[2] for r in sel) / i if i else 0
    return round(c), round(i), p


A, B = "Last 28 days", "Previous 28 days"
hdr = lambda key: [key] + [f"{l} {m}" for l in (A, B) for m in ("Clicks", "Impressions", "CTR", "Position")]


def row(key, a, b):
    out = [key]
    for c, i, p in (a, b):
        out += [c, i, f"{(c / i * 100 if i else 0):.2f}%", f"{p:.1f}" if i else "0"]
    return out


with open(os.path.join(OUT, "Pages.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(hdr("Top pages"))
    for url, *_ in pages:
        w.writerow(row(url, window(page_daily[url], AFTER), window(page_daily[url], BEFORE)))

with open(os.path.join(OUT, "Queries.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(hdr("Top queries"))
    for url, sec, bc, ctr, pos, qs in pages:
        shares = [random.uniform(0.5, 1.5) for _ in qs]; s = sum(shares); shares = [x / s * 0.8 for x in shares]  # 20% anonymized
        (ca, ia, pa), (cb, ib, pb) = window(page_daily[url], AFTER), window(page_daily[url], BEFORE)
        for q, sh in zip(qs, shares):
            off = random.uniform(0, 1.2) if pos > 2 else 0.0
            w.writerow(row(q, (round(ca * sh), round(ia * sh), pa + off), (round(cb * sh), round(ib * sh), pb + off)))

tot_a = [sum(window(page_daily[u], AFTER)[k] for u, *_ in pages) for k in (0, 1)]
tot_b = [sum(window(page_daily[u], BEFORE)[k] for u, *_ in pages) for k in (0, 1)]
with open(os.path.join(OUT, "Devices.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(hdr("Device"))
    for dev, sh, pa, pb in (("MOBILE", 0.64, 5.4, 4.0), ("DESKTOP", 0.33, 4.6, 3.6), ("TABLET", 0.03, 5.1, 4.2)):
        w.writerow(row(dev, (round(tot_a[0] * sh), round(tot_a[1] * sh), pa), (round(tot_b[0] * sh), round(tot_b[1] * sh), pb)))
with open(os.path.join(OUT, "Countries.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(hdr("Country"))
    for c, sh in (("United States", 0.71), ("Canada", 0.12), ("United Kingdom", 0.09), ("Australia", 0.08)):
        w.writerow(row(c, (round(tot_a[0] * sh), round(tot_a[1] * sh), 4.9), (round(tot_b[0] * sh), round(tot_b[1] * sh), 3.8)))

with open(os.path.join(HERE, "Dates.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["Date", "Clicks", "Impressions", "CTR", "Position"])
    for i, d in enumerate(days):
        c = sum(page_daily[u][i][1] for u, *_ in pages); im = sum(page_daily[u][i][2] for u, *_ in pages)
        p = sum(page_daily[u][i][3] * page_daily[u][i][2] for u, *_ in pages) / im
        w.writerow([d.isoformat(), round(c), round(im), f"{c / im * 100:.2f}%", f"{p:.1f}"])

with open(os.path.join(HERE, "events.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["name", "type", "start", "end"])
    w.writerow(["Demo core update (fictional)", "core", "2026-09-03", "2026-09-18"])
    w.writerow(["Deploy v4.2: new deals template", "deploy", "2026-09-06", "2026-09-06"])
print("demo data written to", HERE)

# bundle the compare CSVs as a Search Console-style .zip
import shutil
import zipfile
with zipfile.ZipFile(os.path.join(HERE, "demo-export.zip"), "w", zipfile.ZIP_DEFLATED) as z:
    for n in sorted(os.listdir(OUT)):
        z.write(os.path.join(OUT, n), n)
shutil.rmtree(OUT)
