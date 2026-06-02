import streamlit as st
import pandas as pd

from engine.parser import normalize_csv
from engine.diagnostics import detect_bottlenecks
from engine.simulator import simulate_impact
from engine.leak_map import revenue_leak_map
from engine.copilot import revenue_copilot

st.set_page_config(page_title="Revenue AI Copilot", layout="wide")

st.title("🤖 Revenue AI Copilot")

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
    st.write(detect_bottlenecks(data))

    # ---------------- LEAK MAP ----------------
    st.subheader("Revenue Leak Map")
    st.write(revenue_leak_map(data))

    # ---------------- COPILOT (CORE VALUE) ----------------
    st.subheader("🔥 Top Revenue Actions (AI Copilot)")

    actions = revenue_copilot(data)

    if not actions:
        st.success("No critical issues detected")

    for i, a in enumerate(actions, 1):
        st.markdown(f"### {i}. {a['problem']}")
        st.write("Impact:", a["impact"])
        st.write("Recommendation:", a["recommendation"])
        st.write("Estimated Gain:", a["estimated_gain"])

else:
    st.info("Upload a CSV to start")
