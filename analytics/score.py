def revops_score(funnel, unit):
    score = 100

    # ---------------- SAFE FUNNEL ----------------
    for k, v in funnel.items():
        try:
            val = float(v)
        except:
            continue

        if val < 20:
            score -= 10
        elif val < 40:
            score -= 5

    # ---------------- SAFE UNIT ECONOMICS ----------------
    try:
        ltv_cac = float(unit.get("LTV_CAC_Ratio", 0))
    except:
        ltv_cac = 0

    try:
        payback = float(unit.get("Payback_Months", 0))
    except:
        payback = 0

    if ltv_cac < 3:
        score -= 20

    if payback > 12:
        score -= 15

    return max(0, min(100, score))
