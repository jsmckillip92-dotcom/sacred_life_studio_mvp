import streamlit as st

from database import save_project


def render_opportunity_engine():
    st.header("🚀 Opportunity Engine")
    st.caption("Quickly score product ideas before spending time building them.")

    idea = st.text_input(
        "Product or niche idea",
        placeholder="Example: vintage botanical printable wall art",
    )

    product_type = st.selectbox(
        "Product type",
        [
            "Printable Wall Art",
            "Planner",
            "Journal",
            "SVG Pack",
            "Sticker Pack",
            "Canva Template",
            "Digital Workbook",
            "KDP Book",
            "Prompt Pack",
            "Other",
        ],
    )

    st.divider()

    col1, col2, col3 = st.columns(3)
    demand = col1.slider("Demand", 1, 10, 7)
    competition = col2.slider("Competition", 1, 10, 5)
    ease = col3.slider("Ease to Create", 1, 10, 8)

    col4, col5, col6 = st.columns(3)
    profit = col4.slider("Profit Potential", 1, 10, 7)
    evergreen = col5.slider("Evergreen Potential", 1, 10, 8)
    brand_fit = col6.slider("Brand Fit", 1, 10, 8)

    opportunity_score = round(
        (
            demand * 0.25
            + (11 - competition) * 0.20
            + ease * 0.15
            + profit * 0.20
            + evergreen * 0.10
            + brand_fit * 0.10
        )
        * 10
    )

    st.divider()
    st.metric("Opportunity Score", f"{opportunity_score}/100")

    if opportunity_score >= 80:
        st.success("Build: strong opportunity. Start with a small test collection.")
        recommendation = "Build a 5–10 product test collection."
    elif opportunity_score >= 60:
        st.warning("Research more: possible opportunity, but validate first.")
        recommendation = "Research competitors, pricing, and search demand before building."
    else:
        st.error("Skip for now: weak opportunity or too much friction.")
        recommendation = "Skip or rethink the angle."

    st.subheader("Recommendation")

    if not idea:
        st.info("Enter a product or niche idea to evaluate.")
    else:
        st.write(f"**Idea:** {idea}")
        st.write(f"**Product Type:** {product_type}")
        st.write(f"**Next Step:** {recommendation}")

    st.divider()

    if st.button("📁 Save Project", use_container_width=True):
        if not idea:
            st.error("Enter a project idea before saving.")
        else:
            save_project(
                name=idea,
                product_type=product_type,
                score=opportunity_score,
                recommendation=recommendation,
            )
            st.success(f"Saved project to database: {idea}")