import os
import io
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

from app.core.config import SCOPES, TOKEN_FILE, CREDENTIALS_FILE

def get_drive_service():
    """Authenticates with Google Drive API and returns the service object."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    
    return build("drive", "v3", credentials=creds)

def download_files_from_folder(service, folder_id: str, download_path: Path):
    """Downloads all files from a specified Google Drive folder to a dynamic path."""
    download_path.mkdir(parents=True, exist_ok=True)
    
    query = f"'{folder_id}' in parents and trashed=false"
    results = service.files().list(
        q=query,
        pageSize=100,
        fields="files(id, name, mimeType, modifiedTime)"
    ).execute()
    
    items = results.get("files", [])
    file_info_list = []

    for item in items:
        file_id = item["id"]
        file_name = item["name"]
        mime_type = item["mimeType"]
        modified_time = item.get("modifiedTime", "")
        request = None
        if mime_type == 'application/vnd.google-apps.document':
            request = service.files().export_media(fileId=file_id, mimeType='application/pdf')
            file_name += '.pdf'
        elif not mime_type.startswith('application/vnd.google-apps'):
            request = service.files().get_media(fileId=file_id)
        if request:
            file_path = download_path / file_name
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                _, done = downloader.next_chunk()
            with open(file_path, "wb") as f:
                f.write(fh.getvalue())
            file_info_list.append({
                "id": file_id,
                "name": file_name,
                "modified_time": modified_time,
                "local_path": str(file_path)
            })
    return file_info_list
