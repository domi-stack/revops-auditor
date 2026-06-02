def funnel_conversion(df):
    # detectar columna automáticamente
    possible_columns = ["stage", "Stage", "funnel_stage", "status"]

    stage_col = None

    for col in possible_columns:
        if col in df.columns:
            stage_col = col
            break

    if stage_col is None:
        return {"error": "No stage column found in CSV"}

    stages = ["MQL", "SQL", "Opportunity", "Won"]
    results = {}

    for i in range(len(stages) - 1):
        a = stages[i]
        b = stages[i + 1]

        a_count = len(df[df[stage_col] == a])
        b_count = len(df[df[stage_col] == b])

        results[f"{a}_to_{b}"] = round((b_count / a_count) * 100, 2) if a_count > 0 else 0

    return results
