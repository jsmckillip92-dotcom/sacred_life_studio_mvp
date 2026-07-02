import streamlit as st
import pandas as pd

from generator import generate_products
from schema import COLUMNS


st.set_page_config(
    page_title="Sacred Life Studio",
    page_icon="🌿",
    layout="wide",
)

st.title("🌿 Sacred Life Studio")
st.caption("AI Digital Product Factory for Etsy printable wall art")


# ---------- Sidebar ----------
st.sidebar.title("Sacred Life Studio")
page = st.sidebar.radio(
    "Navigation",
    [
        "📊 Dashboard",
        "💡 Product Factory",
        "🎨 Artwork Factory",
        "🖼 Mockup Factory",
        "✍️ Listing Factory",
        "📦 Export Center",
        "📈 Analytics",
        "⚙️ Settings",
    ],
)


# ---------- Session State ----------
if "catalog" not in st.session_state:
    st.session_state.catalog = pd.DataFrame(columns=COLUMNS)

df = st.session_state.catalog


# ---------- Dashboard ----------
if page == "📊 Dashboard":
    st.header("📊 Dashboard")

    total_products = len(df)
    ai_generated = len(df[df["Status"] == "AI Generated"]) if not df.empty and "Status" in df else 0
    fallback_generated = len(df[df["Status"] == "Fallback Generated"]) if not df.empty and "Status" in df else 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Products", total_products)
    col2.metric("AI Generated", ai_generated)
    col3.metric("Fallback", fallback_generated)
    col4.metric("Avg Score", round(df["Overall Score"].mean(), 1) if not df.empty and "Overall Score" in df else 0)

    st.divider()

    if df.empty:
        st.info("No products yet. Go to Product Factory to generate your first catalog.")
    else:
        st.subheader("Current Catalog")
        st.dataframe(df, width="stretch", height=500)


# ---------- Product Factory ----------
elif page == "💡 Product Factory":
    st.header("💡 Product Factory")
    st.write("Generate Etsy-ready printable wall art product concepts.")

    col1, col2 = st.columns(2)

    with col1:
        count = st.number_input("Number of products", min_value=1, max_value=200, value=10)
        start_number = st.number_input("Start product number", min_value=1, value=1)
        collection = st.text_input("Collection", value="Sacred Geometry")
        series = st.text_input("Series", value="Foundations")

    with col2:
        price = st.number_input("Price", min_value=0.99, max_value=99.00, value=9.99, step=1.00)
        style_direction = st.text_input(
            "Style direction",
            value="vintage black ink sacred geometry",
        )
        target_buyer = st.text_area(
            "Target buyer",
            value="meditation room, yoga studio, and spiritual home decor buyer",
        )

    if st.button("Generate Product Catalog", type="primary"):
        with st.spinner("Generating products..."):
            rows = generate_products(
                count=count,
                collection=collection,
                series=series,
                target_buyer=target_buyer,
                price=price,
                start_number=start_number,
                style_direction=style_direction,
            )
            new_df = pd.DataFrame(rows)
            new_df = new_df.reindex(columns=COLUMNS)
            st.session_state.catalog = new_df
            st.success("Catalog generated.")

    df = st.session_state.catalog

    if not df.empty:
        st.subheader("Generated Products")
        st.dataframe(df, width="stretch", height=500)


# ---------- Artwork Factory ----------
elif page == "🎨 Artwork Factory":
    st.header("🎨 Artwork Factory")

    if df.empty:
        st.info("Generate products first in Product Factory.")
    else:
        selected = st.selectbox("Select product", df["Product ID"].tolist())
        row = df[df["Product ID"] == selected].iloc[0]

        st.subheader(row["Artwork Name"])
        st.markdown("### Image Prompt")
        st.code(row["Image Prompt"])

        st.markdown("### Negative Prompt")
        st.code(row["Negative Prompt"])

        st.markdown("### Variation Prompt")
        st.code(row["Variation Prompt"])

        st.markdown("### Upscale Prompt")
        st.code(row["Upscale Prompt"])


# ---------- Mockup Factory ----------
elif page == "🖼 Mockup Factory":
    st.header("🖼 Mockup Factory")

    if df.empty:
        st.info("Generate products first in Product Factory.")
    else:
        selected = st.selectbox("Select product", df["Product ID"].tolist())
        row = df[df["Product ID"] == selected].iloc[0]

        st.markdown("### Mockup Prompt")
        st.code(row["Mockup Prompt"])

        st.markdown("### Hero Image Prompt")
        st.code(row["Hero Image Prompt"])

        st.markdown("### Thumbnail Prompt")
        st.code(row["Thumbnail Prompt"])


# ---------- Listing Factory ----------
elif page == "✍️ Listing Factory":
    st.header("✍️ Listing Factory")

    if df.empty:
        st.info("Generate products first in Product Factory.")
    else:
        selected = st.selectbox("Select product", df["Product ID"].tolist())
        row = df[df["Product ID"] == selected].iloc[0]

        st.markdown("### Etsy Title")
        st.code(row["SEO Title"])

        st.markdown("### Short Title")
        st.code(row["Short Title"])

        st.markdown("### Description")
        st.text_area("Full Description", value=row["Full Description"], height=250)

        st.markdown("### 13 Etsy Tags")
        st.code(row["13 Tags"])

        st.markdown("### Materials")
        st.code(row["Materials"])


# ---------- Export Center ----------
elif page == "📦 Export Center":
    st.header("📦 Export Center")

    if df.empty:
        st.info("Generate products first before exporting.")
    else:
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Full Etsy Catalog CSV",
            data=csv,
            file_name="sacred_life_studio_catalog.csv",
            mime="text/csv",
        )

        st.subheader("Export Preview")
        st.dataframe(df, width="stretch", height=500)


# ---------- Analytics ----------
elif page == "📈 Analytics":
    st.header("📈 Analytics")

    if df.empty:
        st.info("No analytics yet. Generate products first.")
    else:
        score_cols = [
            "Product ID",
            "Artwork Name",
            "Primary Subject",
            "Overall Score",
            "SEO Score",
            "Artwork Score",
            "Originality Score",
        ]

        st.subheader("Top Products by Score")
        st.dataframe(
            df[score_cols].sort_values("Overall Score", ascending=False),
            width="stretch",
        )


# ---------- Settings ----------
elif page == "⚙️ Settings":
    st.header("⚙️ Settings")

    st.subheader("OpenAI Connection")

    if "OPENAI_API_KEY" in st.secrets:
        st.success("OPENAI_API_KEY is saved in Streamlit Secrets.")
    else:
        st.error("OPENAI_API_KEY is missing from Streamlit Secrets.")

    st.subheader("Current Status")
    st.write("If AI generation fails with `insufficient_quota`, add billing/credits to your OpenAI API account.")

    st.subheader("App Info")
    st.write("Sacred Life Studio MVP v1.1")
