def detect_bottlenecks(data):
    insights = []

    if "lead" in data and "mql" in data:
        if data["lead"] > 0 and data["mql"] / data["lead"] < 0.2:
            insights.append("🚨 Lead → MQL débil")

    if "mql" in data and "sql" in data:
        if data["mql"] > 0 and data["sql"] / data["mql"] < 0.3:
            insights.append("🚨 MQL → SQL débil")

    if "cost" in data and "revenue" in data:
        if data["cost"] > 0 and data["revenue"] / data["cost"] < 3:
            insights.append("🚨 Unit economics mala")

    return insights
