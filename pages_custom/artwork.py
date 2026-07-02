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
        st.success("Future AI Generation Center")

        st.button("🎨 Generate Artwork", use_container_width=True)
        st.button("🔄 Regenerate", use_container_width=True)
        st.button("⭐ Save Favorite", use_container_width=True)

        st.divider()

        st.write("Future Features")
        st.write("• OpenAI Images")
        st.write("• GPT Image 1")
        st.write("• Flux")
        st.write("• Midjourney")
        st.write("• Stable Diffusion")