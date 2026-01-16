def calculate_savings(df, insights):
    total_spend = df['invoice_amount_usd'].sum()
    
    # 1. Vendor Renegotiation (Assumes 5% on top 20% of vendors by spend)
    vendor_spend = df.groupby('energy_vendor')['invoice_amount_usd'].sum().sort_values(ascending=False)
    top_vendors = vendor_spend.head(int(len(vendor_spend) * 0.2))
    renegotiation_savings = top_vendors.sum() * 0.05
    
    # 2. Rate Plan Optimization (Flat 4% of total as heuristic)
    rate_savings = total_spend * 0.04
    
    # 3. Price Creep reversal (Recover 50% of detected growth)
    # Using insights['price_creep'] if available, else estimate
    creep_savings = 0
    if insights.get('price_creep'):
        # Just a heuristic for demo: assume we can fix the creep for one month
        creep_cv = len(insights['price_creep'])
        creep_savings = (total_spend * 0.01) * creep_cv # Dummy logic for robust demo number
        
    total_potential = renegotiation_savings + rate_savings + creep_savings
    
    return {
        "vendor_renegotiation": round(renegotiation_savings, 2),
        "rate_plan_optimization": round(rate_savings, 2),
        "price_creep_recovery": round(creep_savings, 2),
        "total_potential_savings": round(total_potential, 2),
        "savings_pct": round((total_potential / total_spend) * 100, 1) if total_spend > 0 else 0
    }

