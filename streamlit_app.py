import streamlit as st
import pandas as pd

from analytics.insights import generate_insights

st.set_page_config(page_title="RevOps MVP", layout="wide")

st.title("📊 RevOps Auditor MVP")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Data")
    st.dataframe(df)

    st.subheader("Funnel")
    st.json(funnel_conversion(df))

    st.subheader("Unit Economics")
    st.json(unit_economics(10000, 50, 1200, 12, 100))
    st.subheader("AI Insights")

funnel_data = funnel_conversion(df)
unit_data = unit_economics(10000, 50, 1200, 12, 100)

insights = generate_insights(funnel_data, unit_data)

for i in insights:
    st.write(i)
else:
    st.info("Upload CSV to start")
