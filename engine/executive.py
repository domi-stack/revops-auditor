def executive_summary(actions):
    if not actions:
        return {
            "status": "HEALTHY",
            "summary": "No critical revenue issues detected",
            "total_impact": 0,
            "top_actions": []
        }

    total_impact = sum(a["estimated_gain"] for a in actions)

    status = "RED"
    if total_impact < 100:
        status = "GREEN"
    elif total_impact < 500:
        status = "YELLOW"

    return {
        "status": status,
        "summary": f"Revenue leakage detected with potential upside of {round(total_impact,2)}",
        "total_impact": total_impact,
        "top_actions": actions[:3]
    }
