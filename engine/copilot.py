def revenue_copilot(data):
    actions = []

    # Lead → MQL
    if "lead" in data and "mql" in data and data["lead"] > 0:
        rate = data["mql"] / data["lead"]
        if rate < 0.2:
            actions.append({
                "problem": "Low Lead → MQL conversion",
                "impact": "HIGH",
                "recommendation": "Improve lead quality + fix acquisition targeting",
                "estimated_gain": data["lead"] * 0.1
            })

    # MQL → SQL
    if "mql" in data and "sql" in data and data["mql"] > 0:
        rate = data["sql"] / data["mql"]
        if rate < 0.3:
            actions.append({
                "problem": "Low MQL → SQL conversion",
                "impact": "HIGH",
                "recommendation": "Fix lead scoring + qualification rules",
                "estimated_gain": data["mql"] * 0.15
            })

    # Revenue efficiency
    if "cost" in data and "revenue" in data and data["cost"] > 0:
        ratio = data["revenue"] / data["cost"]
        if ratio < 3:
            actions.append({
                "problem": "Poor unit economics",
                "impact": "CRITICAL",
                "recommendation": "Reduce CAC or increase pricing",
                "estimated_gain": data["revenue"] * 0.2
            })

    # ordenar por impacto estimado
    actions = sorted(actions, key=lambda x: x["estimated_gain"], reverse=True)

    return actions
