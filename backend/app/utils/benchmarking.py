import pandas as pd

def plant_benchmark(df):
    # Calculate total spend per plant
    plant_spend = df.groupby('plant')['invoice_amount_usd'].sum().to_dict()
    
    # Calculate average spend across all plants
    avg_spend = df.groupby('plant')['invoice_amount_usd'].sum().mean()
    
    return {
        "plant_spend": plant_spend,
        "average_plant_spend": float(avg_spend) if not pd.isna(avg_spend) else 0.0
    }
