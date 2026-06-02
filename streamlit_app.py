import streamlit as st
import pandas as pd

from engine.parser import normalize_csv
from engine.copilot import revenue_copilot
from engine.executive import executive_summary

st.set_page_config(page_title="Revenue Growth OS", layout="wide")

st.title("📊 Revenue Growth OS")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Raw Data")
    st.dataframe(df)

    # ---------------- DATA ----------------
    data = normalize_csv(df)

    st.subheader("Normalized Metrics")
    st.json(data)

    # ---------------- COPILOT ----------------
    actions = revenue_copilot(data)

    # ---------------- EXECUTIVE LAYER ----------------
    report = executive_summary(actions)

    st.subheader("🧠 Executive Summary")

    if report["status"] == "GREEN":
        st.success(report["summary"])
    elif report["status"] == "YELLOW":
        st.warning(report["summary"])
    else:
        st.error(report["summary"])

    st.write("Total Impact (€):", report["total_impact"])

    st.subheader("🔥 Top 3 Actions")

    for i, a in enumerate(report["top_actions"], 1):
        st.markdown(f"### {i}. {a['problem']}")
        st.write("Recommendation:", a["recommendation"])
        st.write("Impact:", a["estimated_gain"])

else:
    st.info("Upload a CSV to start analysis")
