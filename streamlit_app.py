import streamlit as st
import pandas as pd

from analytics.funnel import funnel_conversion
from analytics.unit_economics import unit_economics

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
else:
    st.info("Upload CSV to start")
