from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Generic Project Configuration ---

# Project Root Directory
ROOT_DIR = Path(__file__).parent.parent.parent

# Base directory for all dynamically generated data (downloads, vector stores, etc.)
DATA_PATH = ROOT_DIR / "data"

# Google Drive API settings
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
TOKEN_FILE = ROOT_DIR / "token.json"
CREDENTIALS_FILE = ROOT_DIR / "credentials.json"