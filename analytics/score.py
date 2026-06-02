def revops_score(funnel, unit):
    score = 100

    # penalizar funnel débil
    for k, v in funnel.items():
        if v < 20:
            score -= 10
        elif v < 40:
            score -= 5

    # penalizar unit economics
    if unit["LTV_CAC_Ratio"] < 3:
        score -= 20

    if unit["Payback_Months"] > 12:
        score -= 15

    return max(0, min(100, score))
