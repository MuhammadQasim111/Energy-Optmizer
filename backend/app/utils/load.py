import pandas as pd
import io
from fastapi import HTTPException

REQUIRED_COLUMNS = ['invoice_date', 'plant', 'energy_vendor', 'invoice_amount_usd']

def load_csv(file):
    try:
        content = file.file.read()
        buffer = io.BytesIO(content)
        df = pd.read_csv(buffer)
        
        # Normalize columns: strip whitespace and lower case if needed (but currently just strip)
        df.columns = df.columns.str.strip()
        
        # Check for expected columns
        
        # Validation
        missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if missing:
            raise HTTPException(status_code=400, detail=f"Missing columns: {missing}")
            
        return df
    except Exception as e:
        print(f"DEBUG: Error loading CSV: {e}")
        raise HTTPException(status_code=400, detail=f"Error reading file: {str(e)}")

