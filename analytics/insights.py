def generate_insights(funnel, unit_economics):
    insights = []

    # ---------------- SAFE FUNNEL ----------------
    for k, v in funnel.items():

        # evitar errores si no es número
        try:
            val = float(v)
        except:
            continue

        if val < 20:
            insights.append(f"⚠️ Problema en {k}: {val}%")
        elif val > 60:
            insights.append(f"✅ Bien en {k}: {val}%")
        else:
            insights.append(f"ℹ️ Normal en {k}: {val}%")

    # ---------------- UNIT ECONOMICS ----------------
    try:
        ltv_cac = float(unit_economics.get("LTV_CAC_Ratio", 0))
    except:
        ltv_cac = 0

    try:
        payback = float(unit_economics.get("Payback_Months", 0))
    except:
        payback = 0

    if ltv_cac < 3:
        insights.append("🚨 LTV/CAC bajo (no escalable)")
    else:
        insights.append("✅ LTV/CAC correcto")

    if payback > 12:
        insights.append("⚠️ Payback alto")
    else:
        insights.append("✅ Payback correcto")

    return insights
