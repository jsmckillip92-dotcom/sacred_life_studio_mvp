
# Sacred Life Studio MVP

This is a starter AI-assisted Etsy product/listing generator.

It creates:
- Product IDs
- Collection ideas
- Artwork concepts
- Image prompts
- Negative prompts
- Mockup prompts
- Etsy titles
- Descriptions
- 13 tags
- Pricing
- File package notes
- AI disclosure notes
- Export-ready CSV

## What this version does

This MVP runs locally in your browser using Streamlit.

You enter:
- Number of products
- Collection theme
- Style direction
- Target buyer
- Price

Then it generates a structured product catalog you can export as CSV.

## What it does NOT do yet

- It does not directly publish to Etsy.
- It does not generate the actual artwork files.
- It does not upload images or digital downloads.
- It does not connect to the Etsy API yet.

That is intentional. The safest first version is a review-ready system, not a blind auto-publisher.

## Install

1. Install Python 3.10+
2. Open Terminal in this folder
3. Run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Optional AI Mode

If you add an OpenAI API key, you can modify `generator.py` later to call an AI model directly.
For now, this uses strong built-in templates so you can test the workflow immediately.

## Recommended Workflow

1. Generate 25 products first.
2. Review and improve the strongest ones.
3. Create the artwork.
4. Export print files.
5. Create mockups.
6. Copy listing text into Etsy.
7. Track sales and improve future batches.
