def generate_insights(funnel, unit_economics):
    insights = []

    for k, v in funnel.items():
        if v < 20:
            insights.append(f"⚠️ Problema en {k}: {v}%")
        elif v > 60:
            insights.append(f"✅ Bien en {k}: {v}%")
        else:
            insights.append(f"ℹ️ Normal en {k}: {v}%")

    if unit_economics["LTV_CAC_Ratio"] < 3:
        insights.append("🚨 LTV/CAC bajo (no escalable)")
    else:
        insights.append("✅ LTV/CAC correcto")

    if unit_economics["Payback_Months"] > 12:
        insights.append("⚠️ Payback alto")
    else:
        insights.append("✅ Payback correcto")

    return insights
