
import streamlit as st
import pandas as pd
from generator import generate_products
from schema import COLUMNS

st.set_page_config(page_title="Sacred Life Studio", layout="wide")

st.title("Sacred Life Studio")
st.subheader("AI-assisted Etsy digital product generator")

st.write(
    "Generate review-ready Etsy product catalogs with artwork prompts, mockup prompts, SEO titles, descriptions, tags, pricing, and download package notes."
)

with st.sidebar:
    st.header("Generate Products")
    count = st.number_input("Number of products", min_value=1, max_value=200, value=25)
    start_number = st.number_input("Start product number", min_value=1, value=1)
    collection = st.text_input("Collection", value="Sacred Geometry")
    series = st.text_input("Series", value="Foundations")
    target_buyer = st.text_area(
        "Target buyer",
        value="meditation room, yoga studio, and spiritual home decor buyer"
    )
    style_direction = st.text_input(
        "Optional style override",
        value="",
        placeholder="Example: vintage black ink sacred geometry"
    )
    price = st.number_input("Price", min_value=0.99, max_value=99.00, value=9.99, step=1.00)

    generate = st.button("Generate Catalog", type="primary")

if "catalog" not in st.session_state:
    st.session_state.catalog = pd.DataFrame(columns=COLUMNS)

if generate:
    rows = generate_products(
        count=count,
        collection=collection,
        series=series,
        target_buyer=target_buyer,
        price=price,
        start_number=start_number,
        style_direction=style_direction
    )
    df = pd.DataFrame(rows)
    df = df.reindex(columns=COLUMNS)
    st.session_state.catalog = df

df = st.session_state.catalog

st.markdown("### Product Catalog")
st.dataframe(df, use_container_width=True, height=500)

if not df.empty:
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="sacred_life_studio_catalog.csv",
        mime="text/csv"
    )

    st.markdown("### Best Products by Overall Score")
    score_cols = ["Product ID", "Artwork Name", "Primary Subject", "SEO Title", "Overall Score", "SEO Score", "Artwork Score", "Originality Score"]
    st.dataframe(df[score_cols].sort_values("Overall Score", ascending=False), use_container_width=True)

    st.markdown("### Copy One Product")
    selected = st.selectbox("Select Product ID", df["Product ID"].tolist())
    row = df[df["Product ID"] == selected].iloc[0]

    st.markdown("#### Image Prompt")
    st.code(row["Image Prompt"])

    st.markdown("#### Etsy Title")
    st.code(row["SEO Title"])

    st.markdown("#### Description")
    st.text_area("Full Description", value=row["Full Description"], height=250)

    st.markdown("#### 13 Tags")
    st.code(row["13 Tags"])

st.markdown("---")
st.caption("MVP: review-ready catalog generator. Next versions can add OpenAI API calls, image generation, print-file export, mockup creation, and Etsy draft listing integration.")
