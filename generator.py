from datetime import date
import json
import streamlit as st
from openai import OpenAI


FALLBACK_SUBJECTS = [
    "Tree of Life",
    "Flower of Life",
    "Seed of Life",
    "Metatron's Cube",
    "Sri Yantra",
    "Merkaba",
    "Moon Phases",
    "Golden Ratio Fern",
    "Sacred Whale",
    "Lotus Geometry",
]


def _fallback_products(count, collection, series, target_buyer, price, start_number, style_direction):
    today = date.today().isoformat()
    rows = []

    for i in range(start_number, start_number + count):
        subject = FALLBACK_SUBJECTS[(i - start_number) % len(FALLBACK_SUBJECTS)]
        product_id = f"SLS-{i:03d}"
        style = style_direction or "vintage black ink sacred geometry"

        rows.append({
            "Product ID": product_id,
            "SKU": product_id + "-DIGITAL",
            "Collection": collection,
            "Series": series,
            "Artwork Name": f"{subject} Study",
            "Version": "v1",
            "Status": "Fallback Generated",
            "Launch Date": "",
            "Last Updated": today,
            "Theme": collection,
            "Primary Subject": subject,
            "Secondary Subject": "sacred geometry and nature symbolism",
            "Sacred Symbol": subject,
            "Symbol Meaning": "balance, harmony, intention, and connection with nature",
            "Interior Style": "meditation room, yoga studio, boho bedroom",
            "Art Style": style,
            "Mood": "calm, spiritual, grounded",
            "Color Palette": "black ink on warm parchment",
            "Border Style": "clean elegant square border",
            "Texture": "subtle aged paper texture",
            "Lighting": "soft natural daylight",
            "Composition": "centered, balanced, symmetrical",
            "Complexity": "medium",
            "Master Prompt": f"Create premium printable wall art featuring {subject} in {style}.",
            "Image Prompt": f"Create a premium square printable wall art design featuring {subject} in {style}, clean border, high contrast, refined spiritual wall art, 300 DPI print quality.",
            "Negative Prompt": "blurry, distorted, low resolution, messy geometry, cheap clip art, watermark, text errors",
            "Variation Prompt": f"Create 4 elegant variations of {subject} in the same brand style.",
            "Upscale Prompt": "Upscale for crisp 300 DPI print quality while preserving geometry and linework.",
            "Editing Prompt": "Clean edges, improve contrast, correct geometry, remove artifacts.",
            "Mockup Prompt": f"Show this square {subject} print framed in a warm meditation room with plants and natural light.",
            "Hero Image Prompt": f"Create an Etsy thumbnail showing a framed square {subject} sacred geometry print.",
            "Thumbnail Prompt": f"Create a clean premium Etsy thumbnail for {subject} printable wall art.",
            "Print Sizes": "8x8, 10x10, 12x12, 16x16, 20x20, 24x24",
            "DPI": "300",
            "Aspect Ratio": "1:1",
            "File Formats": "JPG, PNG, PDF",
            "SEO Title": f"{subject} Printable Wall Art, Sacred Geometry Digital Download, Spiritual Decor",
            "Short Title": f"{subject} Sacred Geometry Print",
            "Meta Description": f"Printable {subject} wall art for meditation rooms, yoga studios, and peaceful spiritual spaces.",
            "Full Description": f"Bring calm, beauty, and intention into your space with this {subject} printable wall art. This is a digital download. No physical item will be shipped.",
            "13 Tags": "printable wall art,sacred geometry,spiritual decor,digital download,meditation decor,yoga room decor,boho wall art,mystic art,zen decor,square print,wall art print,energy art,download print",
            "Category": "Art & Collectibles > Prints > Digital Prints",
            "Materials": "digital download, printable wall art, JPG, PNG, PDF",
            "Primary Keyword": f"{subject.lower()} printable wall art",
            "Secondary Keywords": "sacred geometry, spiritual decor, meditation wall art, yoga studio print",
            "Room Suggestions": "meditation room, yoga studio, bedroom, office",
            "Price": price,
            "Pinterest Title": f"{subject} Printable Wall Art",
            "Pinterest Description": f"A peaceful {subject} printable for spiritual spaces and meditation rooms.",
            "Instagram Caption": f"New {subject} printable wall art for peaceful spaces. #printablewallart #sacredgeometry",
            "Facebook Caption": f"Bring calm and intention into your space with this {subject} printable wall art.",
            "Email Announcement": f"Introducing {subject} Sacred Geometry Print.",
            "Thank You Note": "Thank you so much for supporting Sacred Life Studio. I hope this piece brings beauty, calm, and intention into your space.",
            "Printing Guide": "Print at home, through a local print shop, or with an online print service. Matte or fine art paper is recommended.",
            "License": "Personal use only. Do not resell, redistribute, or use commercially without permission.",
            "AI Disclosure": "This design was created with AI-assisted tools and refined with human creative direction.",
            "Views": "",
            "Favorites": "",
            "Sales": "",
            "Revenue": "",
            "Conversion Rate": "",
            "SEO Score": 80,
            "Thumbnail Score": 80,
            "Artwork Score": 80,
            "Brand Score": 85,
            "Originality Score": 78,
            "Overall Score": 81,
            "Notes": "Fallback template generated.",
        })

    return rows


def _parse_json(text):
    try:
        return json.loads(text)
    except Exception:
        start = text.find("[")
        end = text.rfind("]") + 1
        return json.loads(text[start:end])


def generate_products(
    count=25,
    collection="Sacred Geometry",
    series="Foundations",
    target_buyer="meditation room, yoga studio, and spiritual home decor buyer",
    price=9.99,
    start_number=1,
    style_direction="",
):
    today = date.today().isoformat()

    try:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        prompt = f"""
Generate {count} unique Etsy digital-download printable wall art products for Sacred Life Studio.

Brand:
Premium sacred geometry, spiritual, botanical, mystical, and nature-inspired printable wall art.
Elegant, timeless, clean, high-quality, not generic AI art.

Collection: {collection}
Series: {series}
Target buyer: {target_buyer}
Style direction: {style_direction or "choose the strongest Etsy-friendly style"}
Price: {price}

Return ONLY valid JSON as an array of objects.

Each object must include:
Artwork Name, Theme, Primary Subject, Secondary Subject, Sacred Symbol, Symbol Meaning,
Interior Style, Art Style, Mood, Color Palette, Border Style, Texture, Lighting,
Composition, Complexity, Master Prompt, Image Prompt, Negative Prompt, Variation Prompt,
Upscale Prompt, Editing Prompt, Mockup Prompt, Hero Image Prompt, Thumbnail Prompt,
SEO Title, Short Title, Meta Description, Full Description, 13 Tags, Category, Materials,
Primary Keyword, Secondary Keywords, Room Suggestions, Pinterest Title, Pinterest Description,
Instagram Caption, Facebook Caption, Email Announcement, Thank You Note, Printing Guide,
License, AI Disclosure, SEO Score, Thumbnail Score, Artwork Score, Brand Score,
Originality Score, Overall Score.

Rules:
- 13 Tags must be exactly 13 comma-separated Etsy tags.
- SEO Title must be under 140 characters.
- Full Description must say it is a digital download and no physical item will be shipped.
- Scores must be numbers from 1 to 100.
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You return only valid JSON. No markdown."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.9,
        )

        products = _parse_json(response.choices[0].message.content)

        rows = []
        for index, item in enumerate(products[:count], start=start_number):
            product_id = f"SLS-{index:03d}"

            row = {
                "Product ID": product_id,
                "SKU": product_id + "-DIGITAL",
                "Collection": collection,
                "Series": series,
                "Version": "v1",
                "Status": "AI Generated",
                "Launch Date": "",
                "Last Updated": today,
                "Print Sizes": "8x8, 10x10, 12x12, 16x16, 20x20, 24x24",
                "DPI": "300",
                "Aspect Ratio": "1:1",
                "File Formats": "JPG, PNG, PDF",
                "Price": price,
                "Views": "",
                "Favorites": "",
                "Sales": "",
                "Revenue": "",
                "Conversion Rate": "",
                "Notes": "",
            }

            row.update(item)
            rows.append(row)

        return rows

    except Exception as e:
        st.warning(f"AI generation failed, using fallback templates. Error: {e}")
        return _fallback_products(
            count=count,
            collection=collection,
            series=series,
            target_buyer=target_buyer,
            price=price,
            start_number=start_number,
            style_direction=style_direction,
        )
