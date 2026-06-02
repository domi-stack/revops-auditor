import streamlit as st
import pandas as pd

from engine.parser import analyze_schema, extract_signals
from engine.copilot import revenue_copilot
from engine.executive import executive_summary
from engine.leak_map import revenue_leak_map

st.set_page_config(page_title="Revenue Intelligence Engine", layout="wide")

st.title("🧠 Revenue Intelligence Engine")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Raw Data")
    st.dataframe(df)

    # ---------------- UNDERSTANDING ----------------
    schema = analyze_schema(df)
    signals = extract_signals(df)

    st.subheader("🧠 Data Understanding")
    st.json(schema)

    st.subheader("📊 Data Signals")
    st.json(signals)

    data = signals

    # ---------------- COPILOT ----------------
    actions = revenue_copilot(data)
    report = executive_summary(actions)

    st.subheader("🧠 Executive Summary")
    st.json(report)

    # ---------------- LEAK MAP ----------------
    st.subheader("🚨 Revenue Leak Map")
    leaks = revenue_leak_map(data)

    for l in leaks:
        st.write(l)

else:
    st.info("Upload a CSV to analyze revenue system")
