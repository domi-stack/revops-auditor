def generate_insights(funnel, unit_economics):
    insights = []

    # Funnel insights
    for k, v in funnel.items():
        if v < 20:
            insights.append(f"⚠️ Weak conversion in {k}: {v}% (bottleneck detected)")
        elif v > 60:
            insights.append(f"✅ Strong conversion in {k}: {v}% (healthy stage)")
        else:
            insights.append(f"ℹ️ Moderate conversion in {k}: {v}% (room for optimization)")

    # Unit economics insights
    if unit_economics["LTV_CAC_Ratio"] < 3:
        insights.append("🚨 LTV/CAC < 3: acquisition model is not scalable")
    else:
        insights.append("✅ LTV/CAC healthy for scaling")

    if unit_economics["Payback_Months"] > 12:
        insights.append("⚠️ Payback period too long (>12 months)")
    else:
        insights.append("✅ Payback period under control")

    return insights
