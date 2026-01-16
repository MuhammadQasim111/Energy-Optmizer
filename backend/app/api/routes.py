from fastapi import APIRouter, UploadFile
from app.services.analytics import run_pipeline

router = APIRouter()

@router.post("/upload")
async def upload_energy_data(file: UploadFile):
    return run_pipeline(file)
