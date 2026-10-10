# Image SEO: 12 Actionable Tips

- **Updated**: 2026-10-05

## TL;DR
Image optimization is filenames, alt text, the right format, correct dimensions, compression, plus delivery mechanics (sitemap, srcset, lazy loading, caching, CDN). Even with machine-learning image recognition, search engines misread images — explicit signals still matter, and images are usually the largest contributor to page weight, so this work pays twice: in image search and in page speed.

## Framework / Step-by-step
1. **Descriptive filenames** — `my-new-black-kitten.jpg`, not `IMG00023.JPG`. No keyword stuffing.
2. **Alt text + captions** — formula: "This is a photograph of ___" → use the ending as alt text; add product/serial numbers for product images; place images near relevant text with captions.
3. **Right file type** — WebP or AVIF usually compress best (serve them with JPEG/PNG fallbacks via `<picture>` where needed); JPEG for photographs, PNG for line art/transparency; prefer video or animated WebP/AVIF over GIF.
4. **Resize to actual display width** — browsers download the full file even when displaying smaller; find your content column's max width in CSS and cap uploads there.
5. **Compress aggressively** — dial quality down; visual results stay good while savings are large. Batch-compress (keep JPEG and PNG in separate batches; keep filenames intact).
6. **Image sitemap** — adds images search engines might miss; may reference other domains (CDN-hosted images are fine — verify the CDN domain in Search Console).
7. **Vector graphics (SVG)** for logos/icons/text — minify + gzip; razor sharp at every resolution, tiny files.
8. **Responsive images (`srcset`)** — serve multiple widths; the browser picks the efficient one per device/DPR. Most CMSes generate sizes + srcset automatically.
9. **Structured data** — product, recipe, and video markup adds descriptive badges in image search results.
10. **Lazy loading** — recommended by page-speed tooling; implement so search engines still see the content, and never lazy-load the hero/LCP image.
11. **Browser caching** — cache images ~1 year via expires headers.
12. **CDN** — serve from edge servers near users; use a CNAME alias (cdn.yourdomain.com) so links and future migrations stay on your domain; image CDNs automate resizing/format negotiation.

## Actionable checklist
- [ ] Filenames descriptive across new uploads
- [ ] Alt text present on meaningful images (decorative can be empty)
- [ ] Modern format (WebP/AVIF with fallbacks) matched to content type
- [ ] No image uploaded wider than its display max width
- [ ] Compression run on legacy image libraries
- [ ] Image sitemap submitted (or images included in main sitemap)
- [ ] srcset/responsive variants served
- [ ] Lazy loading verified crawlable/rendered
- [ ] Cache headers set for images
- [ ] CDN on your own subdomain (CNAME)

## Data points & benchmarks
- Same photo, same visible quality: 31 KB vs 73 KB (58% smaller) — compression is free bandwidth.
- In a 15-image compression test: best tool averaged 69% reduction on JPEGs; dropping PNG quality settings to 40% achieved ~76% reduction.
- An 8.54 KB SVG minified + gzipped to 3.56 KB (42% saving).
- In one example, a brand found 2,300+ backlinks from 158 sites pointing at image/CDN file URLs instead of pages — every one a link-recovery opportunity.

## Mistakes to avoid
- Keyword-stuffed filenames or alt attributes — spam signal, poor UX.
- Uploading multi-thousand-pixel originals for a 720px content column.
- CDN URLs on a third-party domain — future migrations and earned links point at the wrong host.
- Letting embedders link to the .jpg file instead of the page — recover that equity with quick, polite outreach (success rates are often good).

## Key principles
- Every image signal (name, alt, caption, page context, schema) helps disambiguate what machine vision gets wrong.
- Image work IS speed work: images dominate page weight, and speed affects UX and Core Web Vitals (a minor ranking factor).
- Don't count on EXIF data as a ranking signal; strip GPS/personal metadata before publishing (it also shrinks files).
