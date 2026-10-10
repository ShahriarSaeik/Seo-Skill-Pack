# Schema Markup: Structured Data for Search & AI Visibility

- **Updated**: 2026-10-05

## TL;DR
Schema markup is standardized code (JSON-LD) that helps search engines understand page content unambiguously and powers rich results like stars, prices, and event details. It also feeds the Knowledge Graph, which increasingly shapes brand representation in AI answers. Implement the few types Google actually supports, validate them, and keep them error-free.

## Framework / Step-by-step
1. **Pick the right types for your site** — e-commerce: Product, Breadcrumb, Organization/Person; blogs/news: Article, Breadcrumb, Organization/Person; topical sites: Recipe, Job Posting, Event, Local Business as relevant.
2. **Generate JSON-LD** — most modern CMSes emit basic schema out of the box (adjust settings or use a plugin); otherwise generate JSON-LD code manually or with a developer. JSON-LD beats microdata/RDFa because it's less error-prone.
3. **Deploy** — place the script block in the `<head>` or `<body>`; either works.
4. **Validate** — test single pages with a schema validator or rich results test; check site-wide rich result status in Search Console.
5. **Monitor at scale** — include structured data checks in scheduled site crawls; fix errors on high-traffic pages first, spot-check fixes, and request reindexing for important URLs.

6. **Start from a ready template** — copy the matching JSON-LD below, replace every value with your real data (never mark up anything that isn't visible on the page), then validate.

**Product (ecommerce, Bangladesh example)**
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Handmade Leather Wallet – Brown",
  "image": ["https://example.com/images/wallet-brown.jpg"],
  "description": "Full-grain leather bifold wallet, hand-stitched in Dhaka.",
  "sku": "WAL-BRN-01",
  "brand": {"@type": "Brand", "name": "Your Brand"},
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/products/leather-wallet-brown",
    "price": "1450",
    "priceCurrency": "BDT",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "shippingDetails": {
      "@type": "OfferShippingDetails",
      "shippingRate": {"@type": "MonetaryAmount", "value": "80", "currency": "BDT"},
      "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "BD"},
      "deliveryTime": {"@type": "ShippingDeliveryTime",
        "handlingTime": {"@type": "QuantitativeValue", "minValue": 0, "maxValue": 1, "unitCode": "DAY"},
        "transitTime": {"@type": "QuantitativeValue", "minValue": 1, "maxValue": 3, "unitCode": "DAY"}}
    },
    "hasMerchantReturnPolicy": {
      "@type": "MerchantReturnPolicy",
      "applicableCountry": "BD",
      "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
      "merchantReturnDays": 7,
      "returnMethod": "https://schema.org/ReturnByMail",
      "returnFees": "https://schema.org/FreeReturn"
    }
  }
}
```
Add `aggregateRating` / `review` only when real customer reviews are shown on the page.

**LocalBusiness (shop, restaurant, clinic)** — use the most specific subtype (e.g., `Restaurant`, `Dentist`)
```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Your Restaurant Name",
  "image": "https://example.com/images/storefront.jpg",
  "url": "https://example.com/",
  "telephone": "+8801XXXXXXXXX",
  "address": {"@type": "PostalAddress", "streetAddress": "House 00, Road 00, Gulshan 1",
    "addressLocality": "Dhaka", "postalCode": "1212", "addressCountry": "BD"},
  "geo": {"@type": "GeoCoordinates", "latitude": 23.7808, "longitude": 90.4167},
  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "11:00", "closes": "23:00"}],
  "servesCuisine": "Bangladeshi",
  "priceRange": "৳৳"
}
```
Name, address and phone must match your Google Business Profile exactly.

**Organization (every site, usually on the homepage)**
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Your Brand",
  "url": "https://example.com/",
  "logo": "https://example.com/images/logo.png",
  "sameAs": ["https://www.facebook.com/yourpage", "https://www.linkedin.com/company/yourbrand"]
}
```

## Actionable checklist
- [ ] Add Organization schema with a stable `@id` for entity disambiguation
- [ ] Add Author/Person schema to strengthen authorship attribution and E-E-A-T signals
- [ ] Add Article schema to blog/news pages (better titles, images, dates in results)
- [ ] Add Product schema with complete price, availability, shipping, and returns fields
- [ ] Prefer schema in the server-rendered HTML: Google can process JavaScript-injected JSON-LD, but many AI crawlers don't run JavaScript
- [ ] Verify `sameAs` links point to your own profiles (wrong values can misattribute your brand)
- [ ] Re-validate schema after redesigns, plugin updates, or theme changes
- [ ] If using knowledge-graph entity IDs in markup, re-verify they still resolve (a major graph cleanup in early 2025 removed many)

## Data points & benchmarks
- Schema.org lists 823+ schema types, but Google supports only a couple dozen (Article, Product, Event, Local Business, Recipe, Review, Job Posting, Breadcrumb, Video, etc.).
- FAQ rich results now only display for well-known, authoritative government and health sites; HowTo rich results were removed entirely (2023).
- Experiment evidence on AI: LLM chatbots will quote fabricated values found only in schema — because they read markup as plain page text, not structured data. One AI assistant, however, uses structured data as part of its grounding/retrieval process.
- Many AI crawlers don't execute JavaScript, so schema injected client-side may be invisible to them.

## Mistakes to avoid
- Marking up invisible or misleading content (violates policies; kills eligibility).
- Adding FAQ/HowTo markup expecting search display in most niches.
- Injecting schema via a tag manager and assuming AI crawlers can see it.
- Sloppy `sameAs` values — one wrong property was enough to make Google attribute a major company's website to an individual.
- Assuming schema directly steers LLM answers; its AI value is indirect (via the Knowledge Graph and entity understanding).

## Key principles
- Schema is an understanding and eligibility layer, not a ranking factor — the payoff is rich results, better representation, and machine-readable product data for AI shopping agents.
- Indirect AI pathway: Organization and Person schema feed entity understanding, which AI answers draw on — accurate, complete entity markup protects how your brand appears in generated answers.
- Complete Product schema = machine-readable products; incomplete schema = incomplete visibility.
