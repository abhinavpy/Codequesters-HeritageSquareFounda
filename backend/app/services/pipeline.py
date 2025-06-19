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

    try:
        # 1. Download files
        statuses[job_id] = {"status": "DOWNLOADING", "details": "Downloading files from Drive..."}
        drive_service = get_drive_service()
        drive_files = download_files_from_folder(drive_service, drive_folder_id, source_docs_path)

        # 2. Sync and update vector store
        statuses[job_id] = {"status": "SYNCING", "details": "Syncing vector store..."}
        sync_and_update_vector_store(drive_files, vector_store_path)

        statuses[job_id] = {"status": "COMPLETED", "details": "Ingestion pipeline finished successfully."}
        print(f"\n--- Ingestion Pipeline for Job {job_id} Complete ---")

    except Exception as e:
        error_message = f"An error occurred: {e}"
        statuses[job_id] = {"status": "FAILED", "details": error_message}
        print(f"--- ERROR in Ingestion Pipeline for Job {job_id} ---")
        print(error_message)
