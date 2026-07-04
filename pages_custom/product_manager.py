import streamlit as st
import pandas as pd

from database import get_projects


def render_product_manager(df):
    st.header("📁 Product Manager")

    projects = get_projects()

    tab_projects, tab_products = st.tabs(["📁 Saved Projects", "🛍 Generated Products"])

    with tab_projects:
        st.subheader("Saved Projects")

        if not projects:
            st.info("No saved projects yet. Go to Opportunity Engine and save one.")
        else:
            for project in projects:
                project_id = project[0]
                name = project[1]
                product_type = project[2]
                score = project[3]
                recommendation = project[4]
                status = project[5]
                created_at = project[6]

                with st.container(border=True):
                    col1, col2, col3 = st.columns([3, 1, 1])

                    with col1:
                        st.markdown(f"### {name}")
                        st.write(f"**Type:** {product_type}")
                        st.write(f"**Next Step:** {recommendation}")
                        st.caption(f"Created: {created_at}")

                    with col2:
                        st.metric("Score", f"{score}/100")

                    with col3:
                        st.write(f"**Status:** {status}")
                        st.caption(f"ID: {project_id}")

    with tab_products:
        st.subheader("Generated Products")

        if df.empty:
            st.info("Generate products first in Product Factory.")
            return

        selected = st.selectbox("Select Product", df["Product ID"].tolist())
        row = df[df["Product ID"] == selected].iloc[0]

        st.subheader(f"📁 {row['Artwork Name']}")

        product_tabs = st.tabs(
            ["📋 Overview", "🎨 Artwork", "✍️ Listing", "🖼 Mockups", "📈 SEO", "📦 Export"]
        )

        with product_tabs[0]:
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

        with product_tabs[1]:
            st.subheader("🎨 Artwork")
            st.text_area("Image Prompt", row["Image Prompt"], height=220)
            st.text_area("Negative Prompt", row["Negative Prompt"], height=120)
            st.text_area("Variation Prompt", row["Variation Prompt"], height=120)
            st.text_area("Upscale Prompt", row["Upscale Prompt"], height=120)

        with product_tabs[2]:
            st.subheader("✍️ Listing")
            st.text_area("SEO Title", row["SEO Title"], height=80)
            st.text_input("Short Title", row["Short Title"])
            st.text_area("Full Description", row["Full Description"], height=250)
            st.text_area("13 Tags", row["13 Tags"], height=100)
            st.text_input("Materials", row["Materials"])

        with product_tabs[3]:
            st.subheader("🖼 Mockups")
            st.text_area("Mockup Prompt", row["Mockup Prompt"], height=180)
            st.text_area("Hero Image Prompt", row["Hero Image Prompt"], height=140)
            st.text_area("Thumbnail Prompt", row["Thumbnail Prompt"], height=140)

        with product_tabs[4]:
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

        with product_tabs[5]:
            st.subheader("📦 Export Product")

            product_export = pd.DataFrame([row])
            csv = product_export.to_csv(index=False).encode("utf-8")

            st.download_button(
                label=f"Download {row['Product ID']} CSV",
                data=csv,
                file_name=f"{row['Product ID']}_listing.csv",
                mime="text/csv",
            )

            st.info("Future versions will export full product folders, prompt packs, listing packs, and image files.")