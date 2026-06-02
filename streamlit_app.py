import streamlit as st
import pandas as pd

from engine.parser import normalize_csv
from engine.diagnostics import detect_bottlenecks
from engine.simulator import simulate_impact
from engine.leak_map import revenue_leak_map

st.set_page_config(page_title="Revenue Decision Engine", layout="wide")

st.title("📊 Revenue Decision Engine")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Raw Data")
    st.dataframe(df)

    # ---------------- DATA ----------------
    data = normalize_csv(df)

    st.subheader("Normalized Metrics")
    st.json(data)

    # ---------------- BOTTLENECKS ----------------
    st.subheader("Bottlenecks")
    insights = detect_bottlenecks(data)

    for i in insights:
        st.write(i)

    # ---------------- LEAK MAP ----------------
    st.subheader("Revenue Leak Map")
    leaks = revenue_leak_map(data)

    for l in leaks:
        st.write(l)

    # ---------------- SIMULATION ----------------
    st.subheader("Impact Simulation")
    scenarios = simulate_impact(data)

    for s in scenarios:
        st.write(s)

else:
    st.info("Upload a CSV to start analysis")
