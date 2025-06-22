# Heritage Square AI - Backend

This is the backend service for the Heritage Square AI project. It is a FastAPI application that provides a RAG (Retrieval-Augmented Generation) pipeline. The service can ingest documents from a specified Google Drive folder, store them in a local vector database, and answer questions based on the ingested content using Google's Gemini models.

## Architecture Diagram
![Architecture Diagram](https://raw.githubusercontent.com/Codequesters-HeritageSquareFounda/main/backend/Architecture_Diagram.png)

## Prerequisites

Before you begin, ensure you have the following installed:
- [Git](https://git-scm.com/)
- [Python 3.10+](https://www.python.org/downloads/)
- A Google Account

## Development Setup

Follow these steps to get the backend running on your local machine.

### 1. Clone the Repository

First, clone the project repository to your local machine.

```bash
git clone <your-repository-url>
cd <repository-folder>/backend
```

### 2. Google Cloud Project & Credentials Setup

This application requires Google Cloud credentials to access the Google Drive API.

#### a. Create Google Cloud Project & Enable APIs
1.  Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project (e.g., "HeritageSquareDev").
2.  Select your new project.
3.  In the navigation menu (☰), go to **APIs & Services > Library**.
4.  Search for and **enable** the following two APIs:
    *   **Google Drive API**
    *   **Google Generative AI API** (or Vertex AI API if you plan to use it)

#### b. Create OAuth 2.0 Credentials
1.  In the navigation menu, go to **APIs & Services > Credentials**.
2.  Click **+ CREATE CREDENTIALS** and select **OAuth client ID**.
3.  If prompted, configure the consent screen first (see next step).
4.  For **Application type**, select **Desktop app**.
5.  Give it a name (e.g., "Heritage Backend Client").
6.  Click **CREATE**. A popup will appear with your credentials. Click **DOWNLOAD JSON**.
7.  **Crucially**, rename the downloaded file to `credentials.json` and place it in the root of the `backend` directory.

#### c. Configure OAuth Consent Screen
1.  In the navigation menu, go to **APIs & Services > OAuth consent screen**.
2.  For **User Type**, select **External** and click **CREATE**.
3.  Fill in the required fields:
    *   **App name:** Heritage Square AI
    *   **User support email:** Your email
    *   **Developer contact information:** Your email
4.  Click **SAVE AND CONTINUE** through the "Scopes" and "Optional Info" sections.
5.  On the "Test users" screen, click **+ ADD USERS**.
6.  Add the Google Account email you will use to authenticate with. This is essential to bypass the "Google hasn't verified this app" screen during development.
7.  Click **SAVE AND CONTINUE**, then **BACK TO DASHBOARD**.

### 3. Python Virtual Environment

Create and activate a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

The application uses a `.env` file to manage API keys and other configuration.

1.  Create a new file named `.env` in the `backend` directory.
2.  Copy the contents of the example below into your new `.env` file.

```properties
# .env file

# Your Google Generative AI API Key from Google AI Studio
# Get it here: https://aistudio.google.com/app/apikey
GOOGLE_API_KEY="AIzaSy..."

# The Gemini model to use for the RAG agent
GEMINI_MODEL_NAME="gemini-1.5-flash"

# Optional: Your OpenAI API key if you plan to use OpenAI models
OPENAI_API_KEY="sk-..."
```

3.  Replace `"AIzaSy..."` with your actual **Google Generative AI API Key**.

### 6. Run the Application

You are now ready to start the FastAPI server.

```bash
uvicorn app.main:app --reload
```
The server should now be running at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Usage Workflow

### Step 1: Ingest Documents from Google Drive

First, you need to tell the application to ingest documents from a specific Google Drive folder.

1.  Create a folder in your Google Drive and upload some PDF, TXT, or DOCX files.
2.  Get the **Folder ID** from the URL (e.g., `https://drive.google.com/drive/folders/THIS_IS_THE_ID`).
3.  Run the following `curl` command, replacing `YOUR_DRIVE_FOLDER_ID` with your ID.

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/ingestion/run" \
-H "Content-Type: application/json" \
-d '{"drive_folder_id": "YOUR_DRIVE_FOLDER_ID"}'
```

The first time you run this, a browser window will open asking you to log in with your Google account and grant permissions. This is the OAuth flow in action. After you approve, a `token.json` file will be created in the `backend` directory, and the ingestion will begin.

The API will return a `job_id`.

### Step 2: Check Ingestion Status

Use the `job_id` from the previous step to check the status of the ingestion process.

```bash
curl http://127.0.0.1:8000/api/v1/ingestion/status/YOUR_JOB_ID
```
Wait until the status is `"COMPLETED"`.

### Step 3: Ask a Question

Once ingestion is complete, you can ask questions about the documents.

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/qa/ask" \
-H "Content-Type: application/json" \
-d '{
  "drive_folder_id": "YOUR_DRIVE_FOLDER_ID",
  "question": "What is the main topic of the documents?"
}'
```

The API will return a JSON object with the answer from the RAG agent. You have now successfully set up and used the backend!
```# Heritage Square AI - Backend

This is the backend service for the Heritage Square AI project. It is a FastAPI application that provides a RAG (Retrieval-Augmented Generation) pipeline. The service can ingest documents from a specified Google Drive folder, store them in a local vector database, and answer questions based on the ingested content using Google's Gemini models.

## Prerequisites

Before you begin, ensure you have the following installed:
- [Git](https://git-scm.com/)
- [Python 3.10+](https://www.python.org/downloads/)
- A Google Account

## Development Setup

Follow these steps to get the backend running on your local machine.

### 1. Clone the Repository

First, clone the project repository to your local machine.

```bash
git clone <your-repository-url>
cd <repository-folder>/backend
```

### 2. Google Cloud Project & Credentials Setup

This application requires Google Cloud credentials to access the Google Drive API.

#### a. Create Google Cloud Project & Enable APIs
1.  Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project (e.g., "HeritageSquareDev").
2.  Select your new project.
3.  In the navigation menu (☰), go to **APIs & Services > Library**.
4.  Search for and **enable** the following two APIs:
    *   **Google Drive API**
    *   **Google Generative AI API** (or Vertex AI API if you plan to use it)

#### b. Create OAuth 2.0 Credentials
1.  In the navigation menu, go to **APIs & Services > Credentials**.
2.  Click **+ CREATE CREDENTIALS** and select **OAuth client ID**.
3.  If prompted, configure the consent screen first (see next step).
4.  For **Application type**, select **Desktop app**.
5.  Give it a name (e.g., "Heritage Backend Client").
6.  Click **CREATE**. A popup will appear with your credentials. Click **DOWNLOAD JSON**.
7.  **Crucially**, rename the downloaded file to `credentials.json` and place it in the root of the `backend` directory.

#### c. Configure OAuth Consent Screen
1.  In the navigation menu, go to **APIs & Services > OAuth consent screen**.
2.  For **User Type**, select **External** and click **CREATE**.
3.  Fill in the required fields:
    *   **App name:** Heritage Square AI
    *   **User support email:** Your email
    *   **Developer contact information:** Your email
4.  Click **SAVE AND CONTINUE** through the "Scopes" and "Optional Info" sections.
5.  On the "Test users" screen, click **+ ADD USERS**.
6.  Add the Google Account email you will use to authenticate with. This is essential to bypass the "Google hasn't verified this app" screen during development.
7.  Click **SAVE AND CONTINUE**, then **BACK TO DASHBOARD**.

### 3. Python Virtual Environment

Create and activate a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

The application uses a `.env` file to manage API keys and other configuration.

1.  Create a new file named `.env` in the `backend` directory.
2.  Copy the contents of the example below into your new `.env` file.

```properties
# .env file

# Your Google Generative AI API Key from Google AI Studio
# Get it here: https://aistudio.google.com/app/apikey
GOOGLE_API_KEY="AIzaSy..."

# The Gemini model to use for the RAG agent
GEMINI_MODEL_NAME="gemini-1.5-flash"

# Optional: Your OpenAI API key if you plan to use OpenAI models
OPENAI_API_KEY="sk-..."
```

3.  Replace `"AIzaSy..."` with your actual **Google Generative AI API Key**.

### 6. Run the Application

You are now ready to start the FastAPI server.

```bash
uvicorn app.main:app --reload
```
The server should now be running at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## API Usage Workflow

### Step 1: Ingest Documents from Google Drive

First, you need to tell the application to ingest documents from a specific Google Drive folder.

1.  Create a folder in your Google Drive and upload some PDF, TXT, or DOCX files.
2.  Get the **Folder ID** from the URL (e.g., `https://drive.google.com/drive/folders/THIS_IS_THE_ID`).
3.  Run the following `curl` command, replacing `YOUR_DRIVE_FOLDER_ID` with your ID.

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/ingestion/run" \
-H "Content-Type: application/json" \
-d '{"drive_folder_id": "YOUR_DRIVE_FOLDER_ID"}'
```

The first time you run this, a browser window will open asking you to log in with your Google account and grant permissions. This is the OAuth flow in action. After you approve, a `token.json` file will be created in the `backend` directory, and the ingestion will begin.

The API will return a `job_id`.

### Step 2: Check Ingestion Status

Use the `job_id` from the previous step to check the status of the ingestion process.

```bash
curl http://127.0.0.1:8000/api/v1/ingestion/status/YOUR_JOB_ID
```
Wait until the status is `"COMPLETED"`.

### Step 3: Ask a Question

Once ingestion is complete, you can ask questions about the documents.

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/qa/ask" \
-H "Content-Type: application/json" \
-d '{
  "drive_folder_id": "YOUR_DRIVE_FOLDER_ID",
  "question": "What is the main topic of the documents?"
}'
```

The API will return a JSON object with the answer from the RAG agent. You have now successfully set