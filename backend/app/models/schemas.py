from pydantic import BaseModel

class UploadResponse(BaseModel):
    summary: dict
    insights: dict
    savings: dict
