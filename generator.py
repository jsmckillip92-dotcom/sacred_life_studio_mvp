
from datetime import date
import random

SYMBOL_MEANINGS = {
    "Tree of Life": "growth, grounding, ancestry, and connection between earth and spirit",
    "Flower of Life": "unity, creation, harmony, and the interconnected pattern of life",
    "Seed of Life": "new beginnings, potential, creation, and sacred order",
    "Metatron's Cube": "divine structure, balance, protection, and universal geometry",
    "Sri Yantra": "abundance, meditation, balance, and the union of inner and outer worlds",
    "Merkaba": "light body, spiritual protection, ascension, and energetic harmony",
    "Moon Phases": "cycles, intuition, feminine rhythm, reflection, and renewal",
    "Golden Ratio": "natural proportion, beauty, order, and divine design",
    "Chakana": "Andean cosmology, sacred balance, earth, sky, and spiritual alignment",
}

SUBJECTS = [
    "Tree of Life", "Flower of Life", "Seed of Life", "Metatron's Cube", "Sri Yantra",
    "Merkaba", "Moon Phases", "Golden Ratio Fern", "Sacred Whale", "Monstera Mandala",
    "Tropical Sun", "Ancient Mountain", "Mystic Owl", "Ocean Spiral", "Lotus Geometry",
    "Celestial Compass", "Sacred Mushroom", "Jungle Portal", "Root Network", "Solar Mandala"
]

STYLES = [
    "vintage black ink sacred geometry",
    "minimalist boho line art",
    "aged parchment mystical illustration",
    "luxury neutral gallery print",
    "tropical botanical sacred geometry",
    "ancient manuscript style",
    "dark ink on warm handmade paper",
    "soft earth-tone meditation art",
    "high-contrast spiritual wall art",
    "refined Japanese-inspired minimalism"
]

INTERIORS = [
    "meditation room", "yoga studio", "boho bedroom", "minimalist living room",
    "tropical home", "healing room", "modern office", "bookshelf vignette",
    "gallery wall", "earthy wellness space"
]

MOODS = ["calm", "grounded", "mystical", "elegant", "ancient", "peaceful", "earthy", "spiritual"]

PALETTES = [
    "black ink on warm parchment",
    "charcoal and ivory",
    "soft beige, cream, and muted gold",
    "deep forest green and warm ivory",
    "burnt umber, sand, and black ink",
    "sepia, antique white, and charcoal",
    "earth brown, muted olive, and cream",
    "minimal black and white"
]

def clean_tag(tag: str) -> str:
    return tag.lower().replace("'", "").strip()[:20]

def make_tags(subject, collection, style):
    raw = [
        subject + " print",
        "sacred geometry",
        "spiritual wall art",
        "printable wall art",
        "digital download",
        "meditation decor",
        "yoga room decor",
        "boho wall art",
        "mystic art",
        "zen wall decor",
        "earthy decor",
        "square print",
        "wall art download",
        collection,
        style.split()[0] + " art",
    ]
    tags = []
    for t in raw:
        tag = clean_tag(t)
        if tag and tag not in tags:
            tags.append(tag)
    return ", ".join(tags[:13])

def score_product(subject, style, tags):
    seo = min(100, 72 + len(tags.split(",")))
    artwork = random.randint(78, 96)
    brand = random.randint(82, 98)
    originality = random.randint(74, 94)
    thumbnail = random.randint(76, 95)
    overall = round((seo + artwork + brand + originality + thumbnail) / 5)
    return seo, thumbnail, artwork, brand, originality, overall

def generate_products(
    count=25,
    collection="Sacred Geometry",
    series="Foundations",
    target_buyer="meditation room, yoga studio, and spiritual home decor buyer",
    price=9.99,
    start_number=1,
    style_direction=""
):
    rows = []
    today = date.today().isoformat()

    for i in range(start_number, start_number + count):
        subject = SUBJECTS[(i - start_number) % len(SUBJECTS)]
        sacred_symbol = subject if subject in SYMBOL_MEANINGS else random.choice(list(SYMBOL_MEANINGS.keys()))
        meaning = SYMBOL_MEANINGS.get(sacred_symbol, "balance, intention, and connection with nature")
        art_style = style_direction.strip() or random.choice(STYLES)
        interior = random.choice(INTERIORS)
        mood = random.choice(MOODS)
        palette = random.choice(PALETTES)
        product_id = f"SLS-{i:03d}"
        artwork_name = f"{subject} {random.choice(['Temple', 'Offering', 'Portal', 'Study', 'Prayer', 'Map', 'Bloom'])}"
        primary_keyword = f"{subject.lower()} printable wall art"
        secondary_keywords = f"sacred geometry, spiritual decor, meditation room decor, yoga studio wall art, boho printable"
        tags = make_tags(subject, collection, art_style)
        seo, thumb, artwork, brand, originality, overall = score_product(subject, art_style, tags)

        image_prompt = (
            f"Create a premium square printable wall art design featuring {subject}, "
            f"integrated with {sacred_symbol} symbolism representing {meaning}. "
            f"Use {art_style}, {palette}, a clean elegant border, balanced centered composition, "
            f"subtle handmade texture, refined line work, high contrast, museum-quality print aesthetic, "
            f"spiritual but not cheesy, timeless, upscale Etsy wall art, 300 DPI feel."
        )

        negative_prompt = (
            "blurry, low resolution, distorted geometry, misspelled text, extra limbs, messy composition, "
            "cheap clip art, oversaturated colors, fake watermark, cartoonish, noisy background, uneven border"
        )

        mockup_prompt = (
            f"Show this square {subject} printable artwork framed in a simple natural wood frame inside a {interior}, "
            f"with soft natural daylight, plants, neutral decor, premium Etsy product photography, clean lifestyle mockup."
        )

        hero_prompt = (
            f"Create an eye-catching Etsy thumbnail for a square framed {subject} sacred wall art print, "
            f"warm natural lighting, clear artwork visibility, premium spiritual home decor, not cluttered."
        )

        title = (
            f"{subject} Printable Wall Art, Sacred Geometry Digital Download, "
            f"Spiritual {interior.title()} Decor, Boho Square Print"
        )[:140]

        short_title = f"{subject} Sacred Geometry Print"

        meta = (
            f"Printable {subject} wall art with sacred geometry styling, designed for meditation rooms, "
            f"yoga studios, and peaceful spiritual spaces."
        )

        description = (
            f"Bring calm, beauty, and intention into your space with this {subject} printable wall art. "
            f"Designed in a {art_style} style with {palette}, this piece blends sacred symbolism with a refined, "
            f"gallery-quality look that feels timeless and grounded.\n\n"
            f"This digital download is ideal for a {interior}, meditation corner, yoga studio, office, bedroom, "
            f"or healing space.\n\n"
            f"WHAT YOU RECEIVE:\n"
            f"- High-resolution printable files\n"
            f"- Square format options: 8x8, 10x10, 12x12, 16x16, 20x20, 24x24\n"
            f"- Easy print guide\n\n"
            f"PLEASE NOTE:\n"
            f"This is a digital download. No physical item will be shipped."
        )

        rows.append({
            "Product ID": product_id,
            "SKU": product_id + "-DIGITAL",
            "Collection": collection,
            "Series": series,
            "Artwork Name": artwork_name,
            "Version": "v1",
            "Status": "Idea",
            "Launch Date": "",
            "Last Updated": today,
            "Theme": collection,
            "Primary Subject": subject,
            "Secondary Subject": "sacred geometry and nature symbolism",
            "Sacred Symbol": sacred_symbol,
            "Symbol Meaning": meaning,
            "Interior Style": interior,
            "Art Style": art_style,
            "Mood": mood,
            "Color Palette": palette,
            "Border Style": "clean elegant square border",
            "Texture": "subtle aged paper / handmade print texture",
            "Lighting": "soft natural daylight for mockups",
            "Composition": "centered, symmetrical, balanced",
            "Complexity": "medium",
            "Master Prompt": image_prompt,
            "Image Prompt": image_prompt,
            "Negative Prompt": negative_prompt,
            "Variation Prompt": f"Create 4 refined variations of {subject} using the same brand style but different border and texture details.",
            "Upscale Prompt": "Upscale for crisp 300 DPI print quality, preserve clean geometry, sharpen linework, remove artifacts.",
            "Editing Prompt": "Clean edges, correct geometry, improve contrast, remove visual noise, keep authentic handmade texture.",
            "Mockup Prompt": mockup_prompt,
            "Hero Image Prompt": hero_prompt,
            "Thumbnail Prompt": hero_prompt,
            "Print Sizes": "8x8, 10x10, 12x12, 16x16, 20x20, 24x24",
            "DPI": "300",
            "Aspect Ratio": "1:1",
            "File Formats": "JPG, PNG, PDF",
            "SEO Title": title,
            "Short Title": short_title,
            "Meta Description": meta,
            "Full Description": description,
            "13 Tags": tags,
            "Category": "Art & Collectibles > Prints > Digital Prints",
            "Materials": "digital download, printable wall art, JPG, PNG, PDF",
            "Primary Keyword": primary_keyword,
            "Secondary Keywords": secondary_keywords,
            "Room Suggestions": f"{interior}, meditation room, yoga studio, bedroom, office",
            "Price": price,
            "Pinterest Title": f"{subject} Printable Wall Art for Peaceful Spiritual Spaces",
            "Pinterest Description": meta,
            "Instagram Caption": f"New {subject} print for peaceful spaces, meditation corners, and sacred homes. #printablewallart #sacredgeometry #spiritualdecor",
            "Facebook Caption": f"Bring a little more calm and intention into your space with this {subject} printable wall art.",
            "Email Announcement": f"Introducing {short_title}, a new digital print designed for calm, grounding, and intentional spaces.",
            "Thank You Note": "Thank you so much for supporting Sacred Life Studio. I hope this piece brings beauty, calm, and intention into your space.",
            "Printing Guide": "Print at home, through a local print shop, or with an online print service. Use matte or fine art paper for best results.",
            "License": "Personal use only. Do not resell, redistribute, or use commercially without permission.",
            "AI Disclosure": "This design was created with AI-assisted tools and refined with human creative direction.",
            "Views": "",
            "Favorites": "",
            "Sales": "",
            "Revenue": "",
            "Conversion Rate": "",
            "SEO Score": seo,
            "Thumbnail Score": thumb,
            "Artwork Score": artwork,
            "Brand Score": brand,
            "Originality Score": originality,
            "Overall Score": overall,
            "Notes": ""
        })

    return rows
