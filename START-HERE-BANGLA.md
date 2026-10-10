# এখান থেকে শুরু করুন: SEO Skills Pack (বাংলা গাইড)

এই প্যাক আপনার AI-কে (Claude, ChatGPT, Gemini বা অন্য যেকোনো AI agent) একজন অভিজ্ঞ SEO এক্সপার্টে পরিণত করে। আপনি SEO-তে একদম নতুন হলেও সমস্যা নেই। AI আপনার প্রশ্ন বুঝে আপনার লেভেল অনুযায়ী সহজ ভাষায় উত্তর দেবে, আর বাংলায় প্রশ্ন করলে বাংলাতেই উত্তর পাবেন।

> **৫ মিনিটে শুরু:** নিচের তিনটা ধাপ মানলেই হবে। বিস্তারিত দরকার হলে `docs-bn` ফোল্ডারের গাইডগুলো পড়ুন।

---

## ধাপ ১: আপনি কোন AI ব্যবহার করেন?

| আপনি ব্যবহার করেন… | কোন ফোল্ডার খুলবেন | গাইড |
|---|---|---|
| **Claude** (claude.ai ওয়েবসাইট বা Desktop অ্যাপ) | `1-Claude` | [docs-bn/02-install-claude.md](docs-bn/02-install-claude.md) |
| **ChatGPT** বা **Gemini** | `2-ChatGPT-Gemini` | [docs-bn/03-install-chatgpt-gemini.md](docs-bn/03-install-chatgpt-gemini.md) |
| **Claude Code, Cursor, Copilot, Codex, Gemini CLI** (কোডিং টুল) | `3-coding-agents` | [docs-bn/04-install-coding-agents.md](docs-bn/04-install-coding-agents.md) |

**কোনটা বেছে নেবেন বুঝতে পারছেন না?** Claude ব্যবহার করুন। সেখানে ফাইল আপলোড করলেই কাজ শেষ, আর Traffic Drop Doctor-এর অ্যানালাইসিস স্ক্রিপ্টও সেখানে নিজে থেকেই চলে। (Skills ফিচার আপনার প্ল্যানে না থাকলে Claude-এর Project পদ্ধতি বা ChatGPT ব্যবহার করুন। গাইডে দুটোই আছে।)

## ধাপ ২: ইনস্টল করুন (২–৫ মিনিট)

**Claude-এর জন্য সংক্ষেপে:**
1. claude.ai-তে যান → **Settings** → **Capabilities**।
2. **"Code execution and file creation"** চালু করুন।
3. **Skills** অংশে `1-Claude` ফোল্ডারের `.skill` ফাইলগুলো একটা একটা করে আপলোড করুন। সবার আগে দিন **`seo-router.skill`**।

**ChatGPT-এর জন্য সংক্ষেপে:** একটা Custom GPT বা Project বানান। `2-ChatGPT-Gemini/chatgpt-files/00-instructions.md` ফাইলের `---` লাইনের নিচের লেখাটা Instructions ঘরে পেস্ট করুন, আর বাকি ১৩টা ফাইল Knowledge হিসেবে আপলোড করুন। **Gemini-তে** একই নির্দেশনা দিন, কিন্তু ফাইল আপলোড করুন `gemini-files` ফোল্ডার থেকে।

বিস্তারিত ধাপে ধাপে বর্ণনা গাইডে আছে।

## ধাপ ৩: প্রথম প্রশ্নটা করুন

নতুন একটা চ্যাট খুলে নিচের যেকোনো একটা লিখুন:

```
আমি একটা অনলাইন কেকের দোকানের ওয়েবসাইট বানিয়েছি। Google-এ কীভাবে আনব? আমি SEO-তে একদম নতুন।
```

```
আমার ব্লগের জন্য ২০টা keyword খুঁজে দাও। বিষয়: ঢাকার রেস্টুরেন্ট রিভিউ। নতুন সাইট, তাই কম প্রতিযোগিতার keyword চাই।
```

```
গত মাসে আমার সাইটের ট্রাফিক ৪০% কমে গেছে। কেন হলো বুঝতে সাহায্য করো।
```

আরও ৭০টার বেশি রেডি প্রম্পট আছে [06-prompt-library.md](docs-bn/06-prompt-library.md)-এ।

---

## পুরো ছবিটা এক নজরে
নতুন হোন বা অভিজ্ঞ, প্যাকটা ভেতরে কীভাবে কাজ করে বুঝতে চাইলে [10-pura-strategy.md](docs-bn/10-pura-strategy.md) পড়ুন। সেখানে আছে সিস্টেম ম্যাপ, কোন সমস্যায় কোন skill লাগে, নতুনদের ৩০ দিনের পথ আর অভিজ্ঞদের workflow।

## ভালো উত্তর পাওয়ার ৪টা টিপস
1. **নিজের পরিস্থিতি বলুন:** সাইটের ধরন (ব্লগ, দোকান, সার্ভিস), কোন দেশ বা শহরের জন্য, সাইট কত পুরনো, আর লক্ষ্য কী (বিক্রি, লিড, ট্রাফিক)।
2. **নিজের লেভেল বলুন:** "আমি নতুন" বললে AI সহজ ভাষায় বোঝাবে। "আমি এজেন্সি চালাই" বললে পুরো ফ্রেমওয়ার্ক দেবে।
3. **শেষে কী চান সেটা বলুন:** চেকলিস্ট, ৩০ দিনের প্ল্যান, ক্লায়েন্ট রিপোর্ট, নাকি সরাসরি লেখা (title, meta description)।
4. **ফলো-আপ প্রশ্ন করুন:** "এটা আরও সহজ করে বলো", "ধাপ ২ কীভাবে করব?", "ফ্রি টুল দিয়ে কীভাবে করব?"

## সব গাইডের তালিকা
| ফাইল | কী আছে |
|---|---|
| [01-ei-pack-e-ki-ache.md](docs-bn/01-ei-pack-e-ki-ache.md) | ১১টা skill কী করে, কখন কোনটা কাজে লাগে |
| [02-install-claude.md](docs-bn/02-install-claude.md) | Claude-এ ইনস্টল (ওয়েব, Desktop, Claude Code) |
| [03-install-chatgpt-gemini.md](docs-bn/03-install-chatgpt-gemini.md) | ChatGPT আর Gemini-তে সেটআপ |
| [04-install-coding-agents.md](docs-bn/04-install-coding-agents.md) | Cursor, Copilot, Codex, Gemini CLI |
| [05-prothom-babohar.md](docs-bn/05-prothom-babohar.md) | প্রথমবার ব্যবহার: কীভাবে কথা বলবেন, উদাহরণ সহ |
| [06-prompt-library.md](docs-bn/06-prompt-library.md) | কাজ আর লেভেল অনুযায়ী রেডি প্রম্পট |
| [07-traffic-drop-doctor.md](docs-bn/07-traffic-drop-doctor.md) | ট্রাফিক কমে গেলে করণীয়, Search Console থেকে ডেটা নামানোর নিয়ম |
| [08-somossa-o-somadhan.md](docs-bn/08-somossa-o-somadhan.md) | কিছু কাজ না করলে কী করবেন |
| [09-shobdokosh.md](docs-bn/09-shobdokosh.md) | SEO শব্দের সহজ বাংলা মানে |
| [10-pura-strategy.md](docs-bn/10-pura-strategy.md) | ⭐ পুরো স্ট্র্যাটেজি: সিস্টেম কীভাবে কাজ করে, সমস্যা অনুযায়ী skill, ৩০ দিনের পথ, অভিজ্ঞ ও এজেন্সির workflow |

> **সতর্কতা:** এই skills আপনাকে সঠিক পথ দেখাবে, কিন্তু Google-এ র‍্যাংক পাওয়ার কোনো গ্যারান্টি দেয় না। SEO-তে ফল আসতে সাধারণত ৩–৬ মাস, কখনো তার বেশি সময় লাগে। পরিসংখ্যানগুলো ২০২৬ সালের তথ্যভিত্তিক, তাই গুরুত্বপূর্ণ সিদ্ধান্তের আগে যাচাই করে নিন।
