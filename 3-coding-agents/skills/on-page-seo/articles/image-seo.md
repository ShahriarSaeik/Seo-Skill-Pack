# Image SEO: 12 Actionable Tips (for More Organic Traffic)

- **Updated**: 2026-10-05

## TL;DR
Image SEO goes far beyond alt tags: 12 tips covering naming, formats, resizing, compression, sitemaps, vectors, responsive serving, schema, lazy loading, caching, CDNs — plus recovering link equity from image backlinks. Even with ML image recognition, Google misclassifies images (91% "cheese" that was butter), so explicit signals still matter.

## Framework / Step-by-step
The 12 tips:
1. **Name images appropriately** — descriptive filenames (`my-new-black-kitten.jpg` not `IMG00023.JPG`); no keyword stuffing (`dog.jpg` beats `dog-puppy-pup-pups-puppies.jpg`)
2. **Descriptive alt text + captions** — finish "This is a(n) image/photo of ___" and use the ending as alt text; add product/serial numbers for product images; captions extracted by Google too
3. **Choose the best file type** — WebP or AVIF for most images (serve JPEG/PNG fallbacks via `<picture>` where needed); JPEG for photos and PNG for graphics/transparency as fallbacks; for animation prefer video or animated WebP/AVIF over GIF
4. **Resize to site dimensions** — upload at max displayed width (e.g. 720px); browsers still download full-size images even when scaled down
5. **Decrease file size** — compress; "don't be afraid to dial down the quality" (Google)
6. **Create an image sitemap** — can include cross-domain (CDN) URLs
7. **Use vector graphics (SVG)** for logos/icons — minify + gzip (example: 8.54kb → 3.56kb)
8. **Serve responsive images** — `srcset` lets browsers pick the right size (most modern CMSs do this automatically)
9. **Schema markup** for recipes/products/videos — powers badges in mobile image search
10. **Lazy load** below-the-fold images — recommended by Google's page-speed tooling (don't lazy-load the main above-the-fold/LCP image)
11. **Leverage browser caching** — cache images ~1 year via Cache-Control headers, a caching plugin, or your CDN
12. **Use a CDN** — serve from nearest server; use a CNAME (cdn.yourdomain.com) so links/credit aren't lost to the CDN domain

**Bonus: recover link equity** — find sites linking directly to your image files (in a backlink tool, filter backlinks whose target URL ends in .jpg/.png) and ask them to link to the page instead.

## Actionable checklist
- [ ] Rename all uploads descriptively before publishing
- [ ] Alt text every image (formula: "This is a photo of ___"); include SKUs on product shots
- [ ] Use captions where possible; place images near relevant text
- [ ] WebP/AVIF with JPEG/PNG fallbacks; video or animated WebP/AVIF instead of GIF for motion
- [ ] Resize to max display width in bulk (a bulk image resizer keeps filenames)
- [ ] Compress with any image compressor (savings vary widely by tool; free options are common)
- [ ] Don't count on EXIF data as a ranking signal; strip GPS and personal metadata before publishing
- [ ] Minify + gzip SVGs; check gzip is enabled server-side
- [ ] Ensure srcset/responsive images (automatic in most modern CMSs)
- [ ] Add Recipe/Product/Video schema where applicable
- [ ] Enable lazy loading (a lazy-load plugin or native browser support)
- [ ] Set browser caching for images to 1 year
- [ ] CDN with custom CNAME subdomain
- [ ] Audit with a site crawler or Lighthouse (missing alt text, oversized images)
- [ ] Outreach: convert image-URL backlinks to page-URL backlinks

## Data points & benchmarks
- Compression test results across popular tools (default settings): JPEG reductions ranged 6%–69% and PNG 1%–65%; no single tool led on both formats
- Example JPEGs: 31kb vs 73kb with little visible difference (58% smaller)
- Most CMSs auto-generate thumbnail (150px), medium (300px), medium-large (768px), large (1024px), full
- EXIF metadata: don't rely on it for rankings; it can expose GPS location and personal details, so strip it
- Real example: one site's CDN subdomain had 2,300+ backlinks from 158 domains pointing at image files — wasted equity

## Mistakes to avoid
- Keyword-stuffing filenames or alt attributes (negative UX, spam signal)
- Uploading 6000px images displayed at 720px (browser downloads full file)
- Mixing JPEGs and PNGs in one bulk-resize batch (tools convert formats)
- Using the CDN's default domain (xyz.cdnprovider.com) — loses attribution and creates migration pain
- Implementing lazy loading in a way Google can't see (follow Google's JS guidance)

## Key principles
- Google's image recognition is good but fallible — "do everything in your power to help them understand your images."
- Images are often the largest contributor to page size; page speed feeds Google's page experience signals, a modest ranking input on desktop and mobile.
- Place images near relevant text; Google extracts context from captions, titles, and surrounding content.
- Embedded infographics/charts attract links — make sure they land on pages, not file URLs.
