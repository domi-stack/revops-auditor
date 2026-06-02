import streamlit as st
import pandas as pd

from analytics.funnel import funnel_conversion
from analytics.unit_economics import unit_economics
from analytics.insights import generate_insights

st.set_page_config(page_title="RevOps MVP", layout="wide")

st.title("📊 RevOps Auditor MVP")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Data")
    st.dataframe(df)

    # Funnel
    st.subheader("Funnel")
    funnel_data = funnel_conversion(df)
    st.json(funnel_data)

    # Unit economics
    st.subheader("Unit Economics")
    unit_data = unit_economics(10000, 50, 1200, 12, 100)
    st.json(unit_data)

    # AI insights
    st.subheader("AI Insights")
    insights = generate_insights(funnel_data, unit_data)

    for i in insights:
        st.write(i)

else:
    st.info("Upload CSV to start")
