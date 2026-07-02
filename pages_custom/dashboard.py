import streamlit as st


def render_dashboard(df):
    st.header("📊 Dashboard")

    total_products = len(df)
    ai_generated = len(df[df["Status"] == "AI Generated"]) if not df.empty and "Status" in df else 0
    fallback_generated = len(df[df["Status"] == "Fallback Generated"]) if not df.empty and "Status" in df else 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Products", total_products)
    col2.metric("AI Generated", ai_generated)
    col3.metric("Fallback", fallback_generated)
    col4.metric(
        "Avg Score",
        round(df["Overall Score"].mean(), 1) if not df.empty and "Overall Score" in df else 0,
    )

    st.divider()

    if df.empty:
        st.info("No products yet. Go to Product Factory to generate your first catalog.")
    else:
        st.subheader("Current Catalog")
        st.dataframe(df, width="stretch", height=500)