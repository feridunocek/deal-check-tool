# Deal Check

**If you know what you need, the solution is simple.**

A five-question thinking system for Black Friday and other sale days. It runs in
the AI assistant you already use. No app, no account, no server, no API key.

You paste your wishlist. Your AI checks each item against five questions and
tells you **BUY**, **WAIT**, **SKIP** or **SUSPICIOUS**, with links you can
click to check it yourself.

[Türkçe aşağıda](#türkçe)

---

## Why

On sale days we compare struck-through prices, open twenty tabs and decide in a
hurry. The struck-through price is the seller's story. The useful questions are
different:

| # | Question | What it catches |
|---|----------|-----------------|
| 1 | **Need** — would I buy this at full price next month? | Buying because of the discount, not the need |
| 2 | **Real price** — what was the lowest price in the last 30 days? | Prices raised before the sale, then "reduced" |
| 3 | **Same product?** — is this the exact model I think it is? | Cheaper sale-day variants under a familiar name |
| 4 | **Alternative** — is there a better option for the same need? | Previous generation, refurbished, another seller, the same model abroad (with shipping, customs and tax) |
| 5 | **Timing** — will it be cheaper or better soon? | New models next month, better deals in January |

The tool is the questions. The AI only does the legwork.

## How to use

**Any AI chat with web search** (ChatGPT, Gemini, Claude, Perplexity, Copilot)

1. Open [`PROMPT.md`](PROMPT.md) and copy everything below the line.
2. Paste it into a new chat, add your list at the end, send.

**Claude, as a skill**

- Claude Code: copy `skills/deal-check/` into `~/.claude/skills/`.
- Claude apps: zip the `skills/deal-check/` folder and upload it under Skills in
  settings. Then just say "check my wishlist".

**As your own assistant** (Custom GPT, Gemini Gem, Claude Project)

Paste `PROMPT.md` (without "My list") into the instructions field. Keep web
search on.

Not sure how to write your list? Use [`wishlist-template.md`](wishlist-template.md).
A real run is in [`examples/`](examples/).

## What it will not do

- It does not collect anything. Your list stays between you and your own AI.
- No affiliate links, no tracking parameters.
- It does not guess. A price without a source link is written as "not found".
- It does not decide for you. It shows the evidence and a verdict; you click
  and check before you pay.

AI can still be wrong. Prices change by the hour. Treat the answer as a well-
prepared second opinion.

## Make it yours

It is a plain text file. Change the five questions, add your own rules ("never
recommend refurbished", "only these three shops"), translate it. That is the
real lesson: once you write down how you think, an AI can run it for you.

---

## Türkçe

**İhtiyacını biliyorsan çözüm basit.**

Black Friday, Efsane Cuma ve diğer indirim günleri için beş soruluk bir düşünme
sistemi. Zaten kullandığın yapay zeka asistanında çalışır. Uygulama, üyelik,
sunucu ya da API anahtarı yok.

Almak istediklerinin listesini yapıştırırsın. Yapay zeka her ürünü beş soruyla
kontrol eder ve tıklayıp doğrulayabileceğin linklerle **AL**, **BEKLE**,
**ATLA** ya da **ŞÜPHELİ** der. Türkçe yazarsan Türkçe cevap verir.

**Beş soru**

1. **İhtiyaç:** Bunu gelecek ay tam fiyata alır mıydım?
2. **Gerçek fiyat:** Son 30 günün en düşük fiyatı neydi? Üstü çizili fiyat kanıt değildir.
3. **Aynı ürün mü:** Model numarası tam olarak düşündüğüm ürün mü?
4. **Alternatif:** Aynı ihtiyaç için daha iyi bir seçenek var mı? (önceki nesil, yenilenmiş, başka satıcı, ya da aynı ürünün yurt dışı fiyatı: kargo, gümrük ve vergi dahil, garanti geçerli mi)
5. **Zamanlama:** Yakında ucuzlayacak ya da yenisi çıkacak mı?

**Nasıl kullanılır:** [`PROMPT.md`](PROMPT.md) dosyasındaki metni kopyala, web
araması açık herhangi bir yapay zeka sohbetine (ChatGPT, Gemini, Claude,
Perplexity, Copilot) yapıştır, listeni sonuna ekle, gönder. Claude kullanıyorsan
`skills/deal-check/` klasörünü skill olarak ekleyebilirsin.

Hiçbir veri bize gelmez; listen sadece sen ve kendi yapay zekan arasında kalır.
Kaynağı olmayan fiyat yazılmaz. Asıl ders şu: nasıl düşündüğünü bir kez yazıya
dökersen, gerisini yapay zeka senin yerine yürütür.

---

MIT License · Feridun Öcek · [ocekdigital.com](https://ocekdigital.com)
