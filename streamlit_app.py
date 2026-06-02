import streamlit as st
import pandas as pd

from analytics.funnel import funnel_conversion
from analytics.unit_economics import unit_economics
from analytics.insights import generate_insights
from analytics.score import revops_score
from analytics.report import generate_pdf

st.set_page_config(page_title="RevOps MVP", layout="wide")

st.title("📊 RevOps Auditor MVP")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Data")
    st.dataframe(df)

    st.subheader("Funnel Analysis")
    funnel_data = funnel_conversion(df)
    st.json(funnel_data)

    st.subheader("Unit Economics")
    unit_data = unit_economics(10000, 50, 1200, 12, 100)
    st.json(unit_data)

    st.subheader("AI Insights")
    insights = generate_insights(funnel_data, unit_data)

    for i in insights:
        st.write(i)

    st.subheader("RevOps Score")
    score = revops_score(funnel_data, unit_data)
    st.metric("Score", f"{score}/100")

    if score >= 80:
        st.success("Healthy growth system")
    elif score >= 50:
        st.warning("Growth system needs optimization")
    else:
        st.error("Critical RevOps issues detected")

    st.subheader("Export Report")

    if st.button("Generate PDF Report"):
        file_path = generate_pdf(score, insights)
        with open(file_path, "rb") as f:
            st.download_button(
                label="Download PDF",
                data=f,
                file_name="revops_report.pdf",
                mime="application/pdf"
            )

else:
    st.info("Upload CSV to start analysis")
