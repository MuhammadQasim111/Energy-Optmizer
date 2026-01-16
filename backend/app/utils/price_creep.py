import pandas as pd

def detect_price_creep(df):
    # Calculate average monthly spend per vendor per plant
    # In a real app, this would use unit_rate if available.
    # Here uses invoice_amount_usd as a proxy for "cost trend"
    
    df_sorted = df.sort_values('invoice_date')
    
    # Calculate pct change month over month for each plant/vendor combo
    grp = df_sorted.groupby(['plant', 'energy_vendor'])['invoice_amount_usd']
    
    # Rolling average to smooth out volatility
    rolling_3m = grp.rolling(window=3, min_periods=1).mean().reset_index(level=[0,1], drop=True)
    df_sorted['rolling_spend'] = rolling_3m
    
    # Calculate growth on the smoothed trend
    growth = df_sorted.groupby(['plant', 'energy_vendor'])['rolling_spend'].pct_change()
    
    df_sorted['spend_growth'] = growth
    
    # Aggregate to find consistent creepers (avg growth > 0)
    creep_summary = df_sorted.groupby(['plant', 'energy_vendor'])['spend_growth'].mean().reset_index()
    creep_summary = creep_summary[creep_summary['spend_growth'] > 0.0]
    
    # Sort by highest growth
    creep_summary = creep_summary.sort_values('spend_growth', ascending=False).head(5)
    
    # Check if empty
    if creep_summary.empty:
        return []

    creep_summary.columns = ['plant', 'vendor', 'avg_growth_pct']
    return creep_summary.to_dict(orient="records")

