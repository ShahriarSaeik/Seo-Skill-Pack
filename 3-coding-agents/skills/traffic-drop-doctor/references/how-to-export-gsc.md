# How to Export Search Console Data for a Traffic-Drop Diagnosis

The export takes about 5 minutes and needs no technical skills. You need access to the site's Google Search Console property (owner, full or restricted user).

## Export 1: the Compare export (required)
1. Open Search Console → choose the property → **Performance → Search results**.
2. Make sure **Total clicks**, **Total impressions**, **Average CTR** and **Average position** are all switched on. The export includes only the metrics you have selected.
3. Click the **Date** filter → **Compare** tab, and pick one of:
   - **"Compare last 28 days to previous period"** for a recent drop.
   - **A custom range:** 4 weeks after the drop vs 4 weeks before it. This is best if you know the date.
   - **Year over year** (the same 28 days last year), if the business is seasonal.
4. Click **Export → Download CSV**. You get a .zip containing `Queries.csv`, `Pages.csv`, `Countries.csv`, `Devices.csv` and others. **Keep the .zip as it is.**

## Export 2: the daily timeline (strongly recommended)
1. Change the Date filter to **Filter → Last 16 months** (not Compare).
2. **Export → Download CSV**. From this .zip you only need `Dates.csv`.

## Optional: an events file
Create a simple CSV called `events.csv` with these columns:
```
name,type,start,end
March 2025 core update,core,2025-03-13,2025-03-27
Site redesign launch,deploy,2025-04-02,2025-04-02
```
- Use type `core`, `spam` or `algorithm` for Google updates.
- Use type `deploy`, `migration`, `redesign` or `content` for your own changes.
- Start from `google-updates.csv` in this folder. Check the **Google Search Status Dashboard** for updates newer than the file, and add them.

## Good to know
- Search Console hides rare ("anonymized") queries, so query totals are lower than page totals. The analyzer uses page totals for the headline numbers.
- The data is usually about 2 days behind.
- For very large sites, the export is capped at 1,000 rows per table. Analyze one section at a time with a **Page** filter, or use the Search Console API or bulk export.
- If you can't export, screenshots of the Performance graph (16 months) and the Queries and Pages tables (Compare mode, sorted by click difference) still allow a rough diagnosis.
