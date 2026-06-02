import streamlit as st
import pandas as pd

from engine.parser import analyze_schema, extract_signals
from engine.copilot import revenue_copilot
from engine.executive import executive_summary
from engine.forecast import arr_forecast
from engine.scenarios import scenario_analysis

st.set_page_config(page_title="Revenue Intelligence Engine", layout="wide")

st.title("🧠 Revenue Intelligence Engine")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    # ---------------- RAW DATA ----------------
    st.subheader("Raw Data")
    st.dataframe(df)

    # ---------------- DATA UNDERSTANDING ----------------
    schema = analyze_schema(df)
    signals = extract_signals(df)

    st.subheader("🧠 Data Understanding")
    st.json(schema)

    st.subheader("📊 Data Signals")
    st.json(signals)

    # ---------------- NORMALIZED DATA ----------------
    data = signals  # usamos signals como input del engine

    # ---------------- COPILOT ----------------
    actions = revenue_copilot(data)
    report = executive_summary(actions)

    st.subheader("🧠 Executive View")
    st.json(report)

    # ---------------- FORECAST ----------------
    st.subheader("📈 ARR Forecast")

    forecast = arr_forecast(data)
    st.json(forecast)

    # ---------------- SCENARIOS ----------------
    st.subheader("🔥 Scenario Impact Ranking")

    scenarios = scenario_analysis(data)

    for s in scenarios:
        st.write(s)

else:
    st.info("Upload a CSV to analyze revenue system")
