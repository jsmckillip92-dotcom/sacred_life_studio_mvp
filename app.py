import streamlit as st
import pandas as pd

from generator import generate_products
from schema import COLUMNS
from pages_custom.home import render_home

st.set_page_config(
    page_title="Sacred Life Studio",
    page_icon="🌿",
    layout="wide",
)

st.title("🌿 Sacred Life Studio")
st.caption("AI Digital Product Factory for Etsy printable wall art")

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
    }

    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #1b2a1f, #243b2a);
        border: 1px solid #355e3b;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    }

    div[data-testid="stMetricLabel"] {
        color: #b7d7b2;
    }

    div[data-testid="stMetricValue"] {
        color: #ffffff;
        font-size: 2.2rem;
    }

    .sls-card {
        background: #111827;
        border: 1px solid #2f3b4a;
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.22);
    }

    .sls-card h3 {
        margin-top: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- Sidebar ----------
st.sidebar.title("Sacred Life Studio")
page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dashboard",
        "💡 Product Factory",
        "📁 Product Manager",
        "🎨 Artwork Studio",
        "🖼 Mockup Studio",
        "✍️ Listing Studio",
        "📦 Export Center",
        "📈 Analytics",
        "⚙️ Settings",
    ],
)


# ---------- Session State ----------
if "catalog" not in st.session_state:
    st.session_state.catalog = pd.DataFrame(columns=COLUMNS)

df = st.session_state.catalog


# ---------- Home ----------
if page == "🏠 Home":
    render_home(df)

# ---------- Dashboard ----------
elif page == "📊 Dashboard":
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


# ---------- Product Manager ----------
elif page == "📁 Product Manager":
    st.header("📁 Product Manager")

    if df.empty:
        st.info("Generate products first in Product Factory.")

    else:
        selected = st.selectbox(
            "Select Product",
            df["Product ID"].tolist(),
        )

        row = df[df["Product ID"] == selected].iloc[0]

        st.subheader(f"📁 {row['Artwork Name']}")

        tabs = st.tabs(
            [
                "📋 Overview",
                "🎨 Artwork",
                "✍️ Listing",
                "🖼 Mockups",
                "📈 SEO",
                "📦 Export",
            ]
        )

        with tabs[0]:
            left, right = st.columns([1, 2])

            with left:
                st.metric("Overall Score", row["Overall Score"])
                st.metric("SEO Score", row["SEO Score"])
                st.metric("Artwork Score", row["Artwork Score"])

            with right:
                st.write(f"**Collection:** {row['Collection']}")
                st.write(f"**Series:** {row['Series']}")
                st.write(f"**SKU:** {row['SKU']}")
                st.write(f"**Price:** ${row['Price']}")
                st.write(f"**Status:** {row['Status']}")
                st.write(f"**Version:** {row['Version']}")

            st.divider()

            st.subheader("Quick Actions")

            col1, col2, col3, col4 = st.columns(4)
            col1.button("🎨 Artwork")
            col2.button("✍️ Listing")
            col3.button("🖼 Mockups")
            col4.button("📦 Export")

        with tabs[1]:
            st.subheader("🎨 Artwork")
            st.markdown("### Image Prompt")
            st.text_area("Image Prompt", row["Image Prompt"], height=220)

            st.markdown("### Negative Prompt")
            st.text_area("Negative Prompt", row["Negative Prompt"], height=120)

            st.markdown("### Variation Prompt")
            st.text_area("Variation Prompt", row["Variation Prompt"], height=120)

            st.markdown("### Upscale Prompt")
            st.text_area("Upscale Prompt", row["Upscale Prompt"], height=120)

        with tabs[2]:
            st.subheader("✍️ Listing")

            st.markdown("### Etsy Title")
            st.text_area("SEO Title", row["SEO Title"], height=80)

            st.markdown("### Short Title")
            st.text_input("Short Title", row["Short Title"])

            st.markdown("### Description")
            st.text_area("Full Description", row["Full Description"], height=250)

            st.markdown("### 13 Etsy Tags")
            st.text_area("13 Tags", row["13 Tags"], height=100)

            st.markdown("### Materials")
            st.text_input("Materials", row["Materials"])

        with tabs[3]:
            st.subheader("🖼 Mockups")

            st.markdown("### Mockup Prompt")
            st.text_area("Mockup Prompt", row["Mockup Prompt"], height=180)

            st.markdown("### Hero Image Prompt")
            st.text_area("Hero Image Prompt", row["Hero Image Prompt"], height=140)

            st.markdown("### Thumbnail Prompt")
            st.text_area("Thumbnail Prompt", row["Thumbnail Prompt"], height=140)

        with tabs[4]:
            st.subheader("📈 SEO Scorecard")

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("SEO", row["SEO Score"])
            col2.metric("Artwork", row["Artwork Score"])
            col3.metric("Originality", row["Originality Score"])
            col4.metric("Overall", row["Overall Score"])

            st.divider()

            st.write(f"**Primary Keyword:** {row['Primary Keyword']}")
            st.write(f"**Secondary Keywords:** {row['Secondary Keywords']}")
            st.write(f"**Meta Description:** {row['Meta Description']}")

        with tabs[5]:
            st.subheader("📦 Export Product")

            product_export = pd.DataFrame([row])
            csv = product_export.to_csv(index=False).encode("utf-8")

            st.download_button(
                label=f"Download {row['Product ID']} CSV",
                data=csv,
                file_name=f"{row['Product ID']}_listing.csv",
                mime="text/csv",
            )

            st.markdown("### Product Notes")
            st.write("Future versions will export product folders, prompt packs, listing packs, and image files.")


# ---------- Artwork Studio ----------
elif page == "🎨 Artwork Studio":
    st.header("🎨 Artwork Studio")

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


# ---------- Mockup Studio ----------
elif page == "🖼 Mockup Studio":
    st.header("🖼 Mockup Studio")

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


# ---------- Listing Studio ----------
elif page == "✍️ Listing Studio":
    st.header("✍️ Listing Studio")

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
    st.write("If AI generation fails with insufficient_quota, add billing/credits to your OpenAI API account.")

    st.subheader("App Info")
    st.write("Sacred Life Studio MVP v3.0")
