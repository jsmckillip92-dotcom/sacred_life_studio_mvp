import streamlit as st


def render_home(df):
    st.header("🏠 Sacred Life Studio HQ")
    st.write("Your AI-powered Etsy digital product factory.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Products Created", len(df))
    col2.metric("Ready to Export", len(df) if not df.empty else 0)
    col3.metric("Current Version", "v3.0")

    st.divider()

    st.subheader("Production Pipeline")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="sls-card">
            <h3>💡 Product Factory</h3>
            <p>Create Etsy-ready product concepts, titles, tags, pricing, and prompts.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="sls-card">
            <h3>🎨 Artwork Studio</h3>
            <p>Build image prompts, negative prompts, variation prompts, and upscale prompts.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="sls-card">
            <h3>📦 Export Center</h3>
            <p>Download CSV files and prepare complete Etsy listing packages.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.info("Welcome back to Sacred Life Studio.")

    st.subheader("📋 Project Roadmap")

    roadmap = [
        ("✅", "Product generation"),
        ("✅", "CSV export"),
        ("✅", "Prompt generation"),
        ("✅", "Product Manager workspace"),
        ("🟡", "AI generation waiting on API credits"),
        ("⬜", "Artwork generation"),
        ("⬜", "Mockup generation"),
        ("⬜", "Etsy draft publishing"),
        ("⬜", "Trend research"),
    ]

    for status, item in roadmap:
        st.write(f"{status} {item}")