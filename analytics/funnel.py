def funnel_conversion(df):
    stages = ["MQL", "SQL", "Opportunity", "Won"]

    results = {}

    for i in range(len(stages) - 1):
        a = stages[i]
        b = stages[i + 1]

        a_count = len(df[df["stage"] == a])
        b_count = len(df[df["stage"] == b])

        results[f"{a}_to_{b}"] = round((b_count / a_count) * 100, 2) if a_count > 0 else 0

    return results
