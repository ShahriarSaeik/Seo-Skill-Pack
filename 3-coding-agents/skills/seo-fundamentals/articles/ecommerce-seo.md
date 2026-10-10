# Ecommerce SEO: A Beginner's Guide

- **Updated**: 2026-10-05

## TL;DR
Ecommerce SEO is mostly about ranking category and product pages. The recurring hazards are technical (faceted navigation creating thousands of junk URLs, duplicate products across category paths), and the wins come from aligning subcategories with search demand, hybrid template/unique on-page copy, product-led blog content, image optimization, and selectively indexing filter URLs that have real search volume.

## Framework / Step-by-step
1. **Technical foundation** — HTTPS everywhere; simple hierarchy (home → category → subcategory → product) with internal links following that flow; solve faceted navigation: filter combinations generate parameterized URLs that split ranking signals and waste crawl budget — canonicalize faceted URLs to their master category by default.
2. **Keyword research for page architecture** — derive subcategories from search demand: enter broad category terms, read matching terms, keep sensible subcategory candidates (skip ultra-specific brands/features; 3-10 subcategories per category is enough). For branded products, the product page already targets the keyword; for unbranded products, target the descriptive term people actually search. If top results are all category pages, searchers want choice → target with a (sub)category page, not a product page.
3. **On-page** — templated title tags/meta descriptions/H1s for scale, but hand-write unique copy for highest-traffic pages (avoid near-duplicate templated pages with no unique value); URLs: domain.com/category/subcategory for browses, domain.com/product for products (avoids duplicates when a product fits multiple categories); add short, helpful, long-tail-rich descriptions to products and categories (mine synonyms from top-ranking competitors' keyword footprints).
4. **Link building** (product pages rarely attract links naturally):
   - Product feedback technique: find popular "best X" lists that don't mention your product; offer the product for feedback; ask for consideration — never trade product for a link explicitly (link scheme risk), and if free product is provided, ask the reviewer to disclose it and tag any link rel="sponsored" or nofollow
   - Claim unlinked brand mentions, especially reviews ("intitle:brand review" minus your domain/outlinks); asking reviewers to link the official product page is a natural pitch
   - Journalist-source services: answer product roundups requests for authority links
5. **Content marketing** — target commercial-investigation keywords ("best X", buying-adjacent questions) and problem keywords your product solves ("how to fix broken headphones" works; "how to clean headphones" doesn't); write product-led content that solves the problem and offers your product when the fix is replacement.
6. **Image SEO** — image search was reported at >20% of searches (older study): hyphenated descriptive filenames, succinct descriptive alt text, modern formats (WebP/AVIF with JPEG/PNG fallbacks); audit for missing alt text prioritizing high-traffic pages; track image performance in Search Console.
7. **Advanced** — selectively self-canonicalize faceted URLs that map to real search demand ("brand + design" combos with volume) for traffic without new content; add filters for attributes people search but you don't expose; product schema (name, brand, price, availability, and rating only from genuine reviews) for rich results; link key subcategories near the top of category pages (UX + reasonable-surfer placement value); schedule recurring crawls — ecommerce technical issues regenerate.

## Actionable checklist
- [ ] Verify HTTPS and clean home → category → subcategory → product linking
- [ ] Confirm faceted URLs canonicalize to master categories
- [ ] Build subcategory list from real search terms (3-10 per category)
- [ ] Each product has one canonical URL (e.g., `/products/name` or `/name`), not several versions under different category paths
- [ ] Hand-write titles/descriptions for top-traffic pages; template the rest
- [ ] Add descriptive long-tail copy to thin product/category pages
- [ ] Run product-feedback outreach to "best X" lists excluding you
- [ ] Reclaim unlinked review mentions
- [ ] Fix missing alt text on high-traffic pages first
- [ ] Index only demand-backed faceted URLs (self-canonical)
- [ ] Deploy product schema with price/availability/rating

## Data points & benchmarks
- Branded product example: 622K monthly US searches for a single product name — the product page is the keyword target by existing.
- Faceted navigation: a handful of filters can generate thousands of parameterized URLs.
- Image search was reported to account for over 20% of searches (older study).
- One "fix it or replace it" blog post: ~13.3K monthly visits from buyers-in-waiting.
- Example audit finding: 2,712 images missing alt text on a single site.

## Mistakes to avoid
- Indexing low-value filter/search pages.
- Putting products under multiple category paths (duplicate URLs).
- Templated copy left on the pages that get the most traffic.
- Keyword stuffing product descriptions.
- Accidental noindex/robots blocks on key pages; slow mobile experience.
- Missing breadcrumbs, schema, or alt text at scale.

## Key principles
- Category and subcategory pages are the ecommerce money pages; architect them from search demand.
- Default faceted URLs OFF for indexing; turn ON selectively only with proven volume.
- Product pages earn links through outreach and PR, not merit alone.
- Shopping and AI-driven results increasingly draw on product feeds and structured data — polish product data, schema, and attributes.
