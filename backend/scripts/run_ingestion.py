import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.config import DATA_PATH
from app.services.drive import get_drive_service, download_files_from_folder
from app.services.documents import load_from_directory, chunk_documents, create_and_save_vector_store

def main():
    """
    Main function to run the full ingestion pipeline for a specific Drive folder.
    This mimics how an API endpoint would orchestrate the services.
    """
    # --- DYNAMIC INPUT ---
    # This ID would come from an API call parameter, e.g., /ingest/{folder_id}
    drive_folder_id = "PASTE_YOUR_DRIVE_FOLDER_ID_HERE"

    if drive_folder_id == "PASTE_YOUR_DRIVE_FOLDER_ID_HERE":
        print("ERROR: Please edit scripts/run_ingestion.py and set the drive_folder_id variable.")
        return

    # --- DYNAMIC PATHS ---
    # Create dynamic paths based on the input ID to keep data separated.
    source_docs_path = DATA_PATH / drive_folder_id / "source_docs"
    vector_store_path = DATA_PATH / drive_folder_id / "vector_store"

    # --- PIPELINE EXECUTION ---
    print("--- Starting Ingestion Pipeline ---")
    print(f"Processing Drive Folder ID: {drive_folder_id}")

    # 1. Download files from Google Drive
    print("\nStep 1: Authenticating and Downloading Files...")
    drive_service = get_drive_service()
    download_files_from_folder(drive_service, drive_folder_id, source_docs_path)

    # 2. Load documents from the local directory
    documents = load_from_directory(source_docs_path)

    # 3. Chunk documents
    chunks = chunk_documents(documents)

    # 4. Create and save vector store
    create_and_save_vector_store(chunks, vector_store_path)

    print("\n--- Ingestion Pipeline Complete ---")

if __name__ == "__main__":
    main()