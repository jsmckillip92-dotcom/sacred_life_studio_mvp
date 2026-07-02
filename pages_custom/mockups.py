import streamlit as st


def render_mockups(df):
    st.header("🖼 Mockup Studio")

    if df.empty:
        st.info("Generate products first in Product Factory.")
        return

    selected = st.selectbox(
        "Select Product",
        df["Product ID"].tolist(),
    )

    row = df[df["Product ID"] == selected].iloc[0]

    st.subheader(row["Artwork Name"])

    tabs = st.tabs(
        [
            "🏠 Room Mockups",
            "🖼 Hero Image",
            "🛒 Etsy Thumbnail",
        ]
    )

    with tabs[0]:
        st.text_area(
            "Mockup Prompt",
            row["Mockup Prompt"],
            height=180,
        )

    with tabs[1]:
        st.text_area(
            "Hero Image Prompt",
            row["Hero Image Prompt"],
            height=160,
        )

    with tabs[2]:
        st.text_area(
            "Thumbnail Prompt",
            row["Thumbnail Prompt"],
            height=160,
        )

        st.info("Future feature: generate Etsy-ready thumbnail mockups.")