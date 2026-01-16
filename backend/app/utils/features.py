import pandas as pd

def add_features(df):
    df['invoice_date'] = pd.to_datetime(df['invoice_date'], errors='coerce')
    df = df.dropna(subset=['invoice_date'])
    df = df.sort_values(by=['plant', 'energy_vendor', 'invoice_date'])
    
    df['month_year'] = df['invoice_date'].dt.to_period('M').astype(str)
    df['month_index'] = df['invoice_date'].dt.month
    df['quarter'] = df['invoice_date'].dt.to_period('Q').astype(str)
    
    return df

