# SEO Forecasting Model: Traffic → Conversions → Revenue (Spreadsheet Method)

- **Updated**: 2026-10-05

## TL;DR
Executives fund forecasts with ranges and assumptions, not single numbers. Model each keyword cluster: **search volume (or traffic potential) × expected CTR at target position × ramp-up curve × conversion rate × value per conversion**. Build three scenarios (conservative, expected, aggressive), subtract the traffic you already get (forecast the *incremental* gain), and show the gap between the target and what current resources can deliver. That gap becomes the budget ask.

## Framework / Step-by-step
1. **Baseline.** Export 12–24 months of organic clicks, conversions and revenue. Split them into brand and non-brand, and note seasonality. If you need a trend, fit a simple seasonal trend in a spreadsheet, or use a time-series library in a notebook.
2. **Opportunity set.** List target clusters (from the keyword map) with: volume or traffic potential, current position (or "not ranking"), target position, difficulty and page status (exists or new).
3. **CTR curve.** Use your own Search Console CTR by position for non-brand queries, which is more accurate than published curves. Adjust it down for SERPs with AI Overviews, ads or heavy SERP features.
4. **Ramp-up.** Apply a time-to-rank curve:
   - New pages on an established site: about 0% → 100% of target over 6–12 months.
   - Refreshed pages that already rank: about 2–4 months.
   - Lower-authority sites: slower.
5. **Incremental traffic** = (target-position clicks − current clicks) × ramp % per month.
6. **Value.** Multiply incremental clicks by the organic conversion rate and the value per conversion (AOV, or lead value = close rate × deal value). Also report **traffic value** (clicks × CPC) as the "ad-spend equivalent".
7. **Scenarios.** Conservative = lower target positions, slower ramp, −20% CTR. Expected = base assumptions. Aggressive = top-3 positions and faster ramp. Show all three.
8. **Gap and ask.** Compare the expected scenario with the business target. Translate the shortfall into resources (pages, links, dev tickets, headcount) using your historical output-to-result ratios.
9. **Track and re-forecast.** Each quarter, plot actuals against the three lines. Explain variance (updates, seasonality, execution slippage) and update the assumptions.

10. **Add the cost side and ROI.** Cost = content + links/PR + dev hours + tools + people for the forecast period. Report **ROI** = (incremental gross profit − cost) ÷ cost, and **payback month** = first month cumulative incremental profit exceeds cumulative cost. Use gross profit (revenue × margin), not revenue.
11. **Worked example (illustrative numbers):**

| Scenario | Incremental clicks / month at month 12 | Conv. rate | Value per conversion | 12-month incremental gross profit (40% margin) | 12-month cost | ROI | Payback |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Conservative | 6,000 | 1.5% | 3,000 BDT | ≈ 0.70M BDT | 1.2M BDT | ≈ −42% | not within 24 months |
| Expected | 10,000 | 2.0% | 3,000 BDT | ≈ 1.56M BDT | 1.2M BDT | ≈ +30% | month 9 (break-even) |
| Aggressive | 15,000 | 2.5% | 3,000 BDT | ≈ 2.92M BDT | 1.2M BDT | ≈ +144% | month 5 |

Assumptions: clicks ramp linearly from 0 to the month-12 level; cost is 100,000 BDT/month; payback counts cumulative profit vs cumulative cost (costs continue after month 12). A forecast where the conservative case doesn't pay back is normal; it tells executives what must go right. Add a sensitivity line: "every ±0.5 pp in conversion rate moves expected-case profit by about ±25%".

## Actionable checklist
- [ ] Separate brand and non-brand; forecast non-brand growth only
- [ ] Use your own CTR-by-position data where possible
- [ ] Discount CTR for AI Overviews and SERP features
- [ ] Apply ramp-up curves by page type (new vs refresh)
- [ ] Forecast incremental gain, not total traffic
- [ ] Present 3 scenarios with an explicit assumptions table
- [ ] Tie traffic to revenue or pipeline, and show traffic value as a secondary metric
- [ ] Show the target-vs-forecast gap and the resources needed to close it
- [ ] Show cost, ROI and payback month per scenario
- [ ] Re-forecast quarterly against actuals

## Data points & benchmarks
- Clicks to the #1 organic result fall noticeably when an AI Overview is present, so discount any CTR curve built before AI Overviews were common.
- On average, one top-ranking page ranks for about 1,000 keywords, which is why traffic potential beats single-keyword volume for forecasts.
- Many SEO projects take 3–6+ months to show results. A forecast with a flat first quarter is realistic, not pessimistic.

## Mistakes to avoid
- Single-point forecasts ("we'll get 100k visits") with no ranges or assumptions
- Using total search volume × #1 CTR for every keyword (wildly optimistic)
- Counting brand traffic growth as an SEO result
- Ignoring cannibalization: two pages don't both get the #1 CTR
- Never comparing forecasts with actuals, which loses credibility next budget cycle

## Key principles
- Executives want one number (revenue); give it with a range.
- The forecast is a negotiation tool. The gap to target justifies resources.
- Assumptions should be visible and editable. Transparency earns trust.
