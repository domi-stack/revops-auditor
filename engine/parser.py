import pandas as pd

def analyze_schema(df):
    df.columns = [c.lower().strip() for c in df.columns]

    schema = {
        "columns": list(df.columns),
        "row_count": len(df),
    }

    # heurística simple de tipo de dataset
    if any("revenue" in c or "arr" in c for c in df.columns):
        schema["type"] = "revenue_dataset"
    elif any("lead" in c or "mql" in c for c in df.columns):
        schema["type"] = "funnel_dataset"
    else:
        schema["type"] = "unknown_business_dataset"

    return schema


def extract_signals(df):
    df.columns = [c.lower().strip() for c in df.columns]

    signals = {}

    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        signals[col] = {
            "sum": float(df[col].sum()),
            "avg": float(df[col].mean())
        }

    return signals
