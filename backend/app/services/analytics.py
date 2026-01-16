import pandas as pd
from app.utils.load import load_csv
from app.utils.features import add_features
from app.utils.price_creep import detect_price_creep
from app.utils.benchmarking import plant_benchmark
from app.utils.rate_plan import rate_plan_analysis
from app.utils.savings import calculate_savings

def run_pipeline(file):
    df = load_csv(file)
    df = add_features(df)

    insights = {
        "price_creep": detect_price_creep(df),
        "benchmarking": plant_benchmark(df),
        "rate_plan": rate_plan_analysis(df),
    }

    savings = calculate_savings(df, insights)

    # Calculate monthly spend for charts
    # Ensure invoice_date is datetime
    if not pd.api.types.is_datetime64_any_dtype(df['invoice_date']):
        df['invoice_date'] = pd.to_datetime(df['invoice_date'])
    
    monthly_spend = (
        df.groupby(df['invoice_date'].dt.strftime('%b'))['invoice_amount_usd']
        .sum()
        .reindex(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        .fillna(0)
        .reset_index()
    )
    monthly_spend.columns = ['name', 'value']
    monthly_spend_list = monthly_spend.to_dict(orient='records')

    return {
        "summary": {
            "total_spend": float(df.invoice_amount_usd.sum()),
            "plants": df.plant.nunique(),
            "vendors": df.energy_vendor.nunique(),
        },
        "insights": insights,
        "savings": savings,
        "monthly_spend": monthly_spend_list
    }
