from pydantic import BaseModel, Field
from typing import Optional

class IngestionRequest(BaseModel):
    drive_folder_id: str = Field(
        ..., 
        description="The ID of the Google Drive folder to ingest.",
        example="1a2b3c4d5e6f7g8h9i0j"
    )

class IngestionResponse(BaseModel):
    message: str
    job_id: str

class JobStatus(BaseModel):
    status: str
    details: Optional[str] = None