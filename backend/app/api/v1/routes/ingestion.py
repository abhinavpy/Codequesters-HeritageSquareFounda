import uuid
from fastapi import APIRouter, BackgroundTasks, HTTPException, status

from app.schemas.ingestion import IngestionRequest, IngestionResponse, JobStatus
from app.services.pipeline import run_ingestion_pipeline

router = APIRouter()

# NOTE: This is a simple in-memory store. For production, you would replace
# this with a more robust solution like Redis or a database.
job_statuses = {}

@router.post("/run", status_code=status.HTTP_202_ACCEPTED, response_model=IngestionResponse)
def run_ingestion_endpoint(
    request: IngestionRequest,
    background_tasks: BackgroundTasks
):
    """
    Starts the ingestion process and returns a job ID for status tracking.
    """
    drive_folder_id = request.drive_folder_id
    if not drive_folder_id or "PASTE" in drive_folder_id:
        raise HTTPException(status_code=400, detail="A valid drive_folder_id must be provided.")

    job_id = str(uuid.uuid4())
    job_statuses[job_id] = {"status": "PENDING", "details": "Ingestion has been queued."}
    
    background_tasks.add_task(run_ingestion_pipeline, drive_folder_id, job_id, job_statuses)
    
    return {
        "message": "Ingestion process started in the background.",
        "job_id": job_id
    }

@router.get("/status/{job_id}", response_model=JobStatus)
def get_ingestion_status(job_id: str):
    """
    Retrieves the status of an ingestion job.
    """
    job = job_statuses.get(job_id)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found.")
    return job