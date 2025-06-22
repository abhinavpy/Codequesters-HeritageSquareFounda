import time
from datetime import datetime

from app.core.config import DATA_PATH
from app.services.drive import get_drive_service, download_files_from_folder
from app.services.documents import sync_and_update_vector_store

def run_ingestion_pipeline(drive_folder_id: str, job_id: str, statuses: dict):
    """
    Runs the full ingestion pipeline and updates the status in a shared dictionary.
    """
    print(f"--- Starting Background Ingestion Pipeline for Job ID: {job_id} ---")

    # Create dynamic paths
    source_docs_path = DATA_PATH / drive_folder_id / "source_docs"
    vector_store_path = DATA_PATH / drive_folder_id / "vector_store"

    start_time = datetime.utcnow()
    statuses[job_id].update({
        "start_time": start_time.isoformat() + "Z",
        "end_time": None,
        "elapsed_time": 0,
        "total_time": None,
    })

    try:
        # 1. Download files
        statuses[job_id].update({"status": "DOWNLOADING", "details": "Downloading files from Drive..."})
        drive_service = get_drive_service()
        drive_files = download_files_from_folder(drive_service, drive_folder_id, source_docs_path)

        # 2. Sync and update vector store
        statuses[job_id].update({"status": "SYNCING", "details": "Syncing vector store..."})
        sync_and_update_vector_store(drive_files, vector_store_path)

        end_time = datetime.utcnow()
        total_time = (end_time - start_time).total_seconds()
        statuses[job_id].update({
            "status": "COMPLETED",
            "details": "Ingestion pipeline finished successfully.",
            "end_time": end_time.isoformat() + "Z",
            "total_time": total_time,
            "elapsed_time": total_time,
        })
        print(f"\n--- Ingestion Pipeline for Job {job_id} Complete ---")

    except Exception as e:
        end_time = datetime.utcnow()
        total_time = (end_time - start_time).total_seconds()
        statuses[job_id].update({
            "status": "FAILED",
            "details": str(e),
            "end_time": end_time.isoformat() + "Z",
            "total_time": total_time,
            "elapsed_time": total_time,
        })
        print(f"--- ERROR in Ingestion Pipeline for Job {job_id} ---")
        print(str(e))
