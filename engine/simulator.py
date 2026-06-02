def simulate_impact(data):
    results = []

    if "sql" in data:
        results.append(f"+10% SQL = +{round(data['sql'] * 0.1, 2)} oportunidades")

    if "revenue" in data:
        results.append(f"+15% revenue = +{round(data['revenue'] * 0.15, 2)} impacto")

    return results
