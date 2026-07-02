import streamlit as st
import pandas as pd

from generator import generate_products
from schema import COLUMNS
from pages_custom.home import render_home
from pages_custom.dashboard import render_dashboard
from pages_custom.product_manager import render_product_manager
from pages_custom.product_factory import render_product_factory

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
    render_dashboard(df)

# ---------- Product Factory ----------
elif page == "💡 Product Factory":
    render_product_factory()
# ---------- Product Manager ----------
elif page == "📁 Product Manager":
    render_product_manager(df)

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
