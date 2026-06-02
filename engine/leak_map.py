def revenue_leak_map(data):
    leaks = []

    if "lead" in data and "mql" in data:
        loss = data["lead"] - data["mql"]
        if loss > 0:
            leaks.append(f"Lead → MQL leak: -{loss} opportunities lost")

    if "mql" in data and "sql" in data:
        loss = data["mql"] - data["sql"]
        if loss > 0:
            leaks.append(f"MQL → SQL leak: -{loss} opportunities lost")

    if "sql" in data and "revenue" in data:
        potential = data["sql"] * 100  # simplificación
        leaks.append(f"Revenue gap potential: up to +{potential}")

    return leaks
