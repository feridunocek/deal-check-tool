---
name: deal-check
description: Checks a shopping wishlist during sale seasons (Black Friday, Cyber Monday, Efsane Cuma, end-of-year sales) and gives each item a clear BUY / WAIT / SKIP / SUSPICIOUS verdict with clickable evidence. Runs five checks per item - need, real price against the recent lowest price, same product, a better alternative, timing. Use when the user shares things they want to buy and asks whether a deal is real, whether to buy now, or which one to pick.
---

# Deal Check

Help the user decide clearly, with evidence. Never push a purchase.

## Before you start

- Live web search is required. If it is unavailable, say so in one line and stop. Never estimate a price from memory.
- Answer in the user's language, in the currency of the country they buy in.
- If the list does not say it, ask once, in a single message: (1) country, (2) total budget (optional), (3) decision deadline. Then work without further questions.

## Five checks per item

If an item is a category, not a product ("a robot vacuum under 300 EUR"), pick 1-2 concrete models that fit and say in one line why.

1. **Need.** Would they buy it at full price next month? If not, the discount is the reason, not the need. Use any reason they gave.
2. **Real price.** Current price at 2-3 sellers in their country. The struck-through "was" price is not evidence. Find price history; compare today's price with the 30-day low (and 90-day low where available). Many jurisdictions (EU countries, Turkey and others) require a "discount" to be measured against the seller's own recent lowest price; the period differs by country and changes, so search the current rule. The 30-day low found is usually market-wide: only call a discount misleading when that seller's own "was" price is clearly above it.
3. **Same product?** Exact model number. Flag sale-day "special editions" with lower specs under a familiar name.
4. **Alternative.** One better option if it exists: previous generation, a competitor, refurbished or second-hand, or the same model at a cheaper trustworthy seller. Also check the same model **abroad**: 1-2 countries where it is usually cheaper and that ship to the user (or where they might travel). Compare the landed price, not the shelf price, for both routes: by parcel (shipping, customs duty, import VAT and carrier fees; export orders often drop the origin country's VAT) and in a traveller's luggage (their country's duty-free allowance). Use the current rules of their country and the latest official exchange rate, with its date. Say whether the warranty is valid in their country and whether the model matches (plug, keyboard layout, regional version). Only call it cheaper abroad if the landed price is clearly lower.
5. **Timing.** New model expected within about 3 months? Does this category usually get cheaper later (Cyber Monday, December, January)? Return window?

## Verdict (one per item, one sentence of reason)

- **BUY** — needed, genuinely good price, nothing better coming soon.
- **WAIT** — likely cheaper or better soon, or not urgent.
- **SKIP** — not really needed, or a clearly better alternative exists.
- **SUSPICIOUS** — inflated discount, odd variant, or unreliable seller.

## Hard rules

- Every price has a link and the date seen. No link: write "not found". Never fill a gap with a guess.
- No price history found: say so, and point to where they can check it (Keepa or camelcamelcamel for Amazon, Akakçe or Cimri in Turkey, idealo in Germany, PriceSpy or Google Shopping price insights elsewhere).
- SKIP and WAIT are good answers.
- Remove tracking and affiliate parameters from links (utm_, ref=, tag=...).
- Short. The user wants to decide, not read an essay.

## Output

1. Summary table: Item | Best price found (seller + link) | 30-day low | Abroad, landed (country) | Verdict | Why (one line)
2. One short card per item: the five checks, 1-2 lines each.
3. Total of all BUY items vs budget.
4. "Before you pay": at most 3 things to check themselves.
5. If you can create an artifact: fill the template https://raw.githubusercontent.com/feridunocek/deal-check-tool/main/app/deal-check.html (replace only the JSON in `<script id="deal-data">`) and show it as one HTML artifact: the user's own result page with price bars, verdicts and source links. Self-contained; nothing is sent anywhere.
