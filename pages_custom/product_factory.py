import streamlit as st
import pandas as pd

from generator import generate_products
from schema import COLUMNS


def render_product_factory():
    st.header("💡 Product Factory")
    st.write("Generate Etsy-ready printable wall art product concepts.")

    col1, col2 = st.columns(2)

    with col1:
        count = st.number_input(
            "Number of products",
            min_value=1,
            max_value=200,
            value=10,
        )

        start_number = st.number_input(
            "Start product number",
            min_value=1,
            value=1,
        )

        collection = st.text_input(
            "Collection",
            value="Sacred Geometry",
        )

        series = st.text_input(
            "Series",
            value="Foundations",
        )

    with col2:
        price = st.number_input(
            "Price",
            min_value=0.99,
            max_value=99.00,
            value=9.99,
            step=1.00,
        )

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
        st.dataframe(
            df,
            width="stretch",
            height=500,
        )