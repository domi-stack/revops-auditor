def unit_economics(marketing_cost, new_customers, avg_revenue, lifetime_months, monthly_revenue):

    cac = marketing_cost / new_customers if new_customers > 0 else 0
    ltv = avg_revenue * lifetime_months
    payback = cac / monthly_revenue if monthly_revenue > 0 else 0

    return {
        "CAC": round(cac, 2),
        "LTV": round(ltv, 2),
        "LTV_CAC_Ratio": round(ltv / cac, 2) if cac > 0 else 0,
        "Payback_Months": round(payback, 2)
    }
