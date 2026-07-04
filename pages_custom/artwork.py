import streamlit as st


def render_artwork(df):
    st.header("🎨 Artwork Studio")

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
            "📝 Prompts",
            "🖼 Preview",
            "⚙️ Generation",
        ]
    )

    with tabs[0]:
        st.text_area(
            "Image Prompt",
            row["Image Prompt"],
            height=220,
        )

        st.text_area(
            "Negative Prompt",
            row["Negative Prompt"],
            height=120,
        )

        st.text_area(
            "Variation Prompt",
            row["Variation Prompt"],
            height=120,
        )

        st.text_area(
            "Upscale Prompt",
            row["Upscale Prompt"],
            height=120,
        )

    with tabs[1]:
        st.info("Artwork preview coming soon.")

        st.container(height=350)

    with tabs[2]:
        st.subheader("AI Artwork Generator")

    model = st.selectbox(
        "Model",
        ["GPT Image 1", "DALL·E 3"],
    )

    size = st.selectbox(
        "Image Size",
        ["1024x1024", "1024x1536", "1536x1024"],
    )

    num_images = st.selectbox(
        "Number of Images",
        [1, 2, 4],
    )

    st.divider()

    if st.button("🎨 Generate Artwork", type="primary", use_container_width=True):
        st.warning(
            "OpenAI billing is not enabled yet. Once API credits are added, this button will generate artwork directly inside Sacred Life Studio."
        )

    st.divider()

    st.subheader("Generated Images")
    st.info("No artwork generated yet.")