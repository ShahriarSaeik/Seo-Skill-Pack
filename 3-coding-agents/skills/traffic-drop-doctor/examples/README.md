# Demo: trailpeak.example (fictional)

This is a realistic but **fictional** Search Console dataset with three planted causes. Use it to try the skill, to test an agent, or to show clients what they'll receive.

| Planted cause | Section | What the data shows |
|---|---|---|
| Deploy accidentally noindexes the deals template (Sep 6) | /deals/ | Impressions −90%, position unchanged |
| Fictional core update (Sep 3–18) | /reviews/ | Position 3.7 → 7.7 |
| AI answers appear on informational queries | /guides/ | Position unchanged, CTR −42% |

Run the demo:
```bash
python ../scripts/analyze_gsc.py --export demo-export.zip --dates Dates.csv \
  --brand "trailpeak" --events events.csv --site "trailpeak.example (demo)" --out example-report
```

Files:
- `demo-export.zip`, `Dates.csv`, `events.csv`: the input data
- `example-report/report.md`: the script's raw output
- `example-report/client-report.md`: the polished deliverable an agent should produce from it
- `make_demo_data.py`: regenerates the data
