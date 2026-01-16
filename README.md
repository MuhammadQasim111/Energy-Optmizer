# Energy Cost Optimizer

Production-grade energy spend intelligence platform.

## Structure

```
energy-cost-optimizer/
│
├── backend/        ← Analytics & API (FastAPI)
├── frontend/       ← CFO-facing dashboard (Next.js)
├── data/           ← Synthetic demo data
└── README.md
```

## Getting Started

### Backend

1. Navigate to `backend/`
2. Install dependencies: `pip install -r requirements.txt`
3. Run server: `uvicorn app.main:app --reload`

### Frontend

1. Navigate to `frontend/`
2. Install dependencies: `npm install`
3. Run dev server: `npm run dev`

## Features

- **Upload & Analyze**: Upload AP invoices (CSV) and get instant insights.
- **Price Creep Detection**: Identify vendors silently raising prices.
- **Benchmarking**: Compare plant performance.
- **Savings Engine**: Calcualte potential recoverable savings.
