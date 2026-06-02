import pandas as pd

def normalize_csv(df):
    df.columns = [c.lower().strip() for c in df.columns]

    data = {}

    if "lead" in df.columns:
        data["lead"] = df["lead"].sum()

    if "mql" in df.columns:
        data["mql"] = df["mql"].sum()

    if "sql" in df.columns:
        data["sql"] = df["sql"].sum()

    if "revenue" in df.columns:
        data["revenue"] = df["revenue"].sum()

    if "cost" in df.columns:
        data["cost"] = df["cost"].sum()

    return data
