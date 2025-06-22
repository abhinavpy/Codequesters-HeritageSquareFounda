graph TD
    subgraph User Interaction
        User([<fa:fa-user> User])
    end

    subgraph FastAPI Backend
        direction LR
        subgraph API Endpoints
            IngestEP["POST /ingest"]
            StatusEP["GET /status/{job_id}"]
            QA_EP["POST /qa/ask"]
        end
        subgraph In-Memory State
            JobStore{{"<fa:fa-tasks> Job Statuses"}}
        end
    end

    subgraph Background Ingestion Pipeline
        direction TB
        DriveSvc["<fa:fa-google> Drive Service"]
        SyncSvc["<fa:fa-sync> Sync & Update Service"]
        EmbedSvc["<fa:fa-cogs> Embeddings (Gemini)"]
    end

    subgraph RAG Q&A Pipeline
        direction TB
        Retriever["<fa:fa-search> Retriever"]
        LLM["<fa:fa-robot> LLM (Gemini)"]
        Prompt["<fa:fa-file-alt> Prompt Template"]
    end

    subgraph Local Storage & Secrets
        direction TB
        SourceDocs["<fa:fa-folder> /data/.../source_docs"]
        VectorStore["<fa:fa-database> /data/.../vector_store (FAISS)"]
        MetadataDB["<fa:fa-database> metadata.db (SQLite)"]
        Secrets[".env / credentials.json / token.json"]
    end

    subgraph External Services
        GoogleDriveAPI["<fa:fa-google> Google Drive API"]
        GoogleGenerativeAI["<fa:fa-google> Google Generative AI API"]
    end

    %% --- Workflow Connections ---

    %% Ingestion Flow
    User -- "POST /ingest" --> IngestEP
    IngestEP -- "Creates Job ID" --> JobStore
    IngestEP -- "Starts Background Task" --> DriveSvc
    DriveSvc -- "OAuth w/ credentials.json" --> GoogleDriveAPI
    DriveSvc -- "Downloads Files" --> SourceDocs
    DriveSvc -- "Triggers Sync" --> SyncSvc
    SyncSvc -- "Reads/Writes Metadata" --> MetadataDB
    SyncSvc -- "Loads/Deletes from" --> VectorStore
    SyncSvc -- "Creates Embeddings" --> EmbedSvc
    EmbedSvc -- "API Call" --> GoogleGenerativeAI
    EmbedSvc -- "Adds Vectors" --> VectorStore
    SyncSvc -- "Updates Status" --> JobStore
    User -- "Checks Status" --> StatusEP -- "Reads from" --> JobStore

    %% Q&A Flow
    User -- "A. POST /qa/ask" --> QA_EP
    QA_EP -- "B. Invokes RAG Chain" --> Retriever
    Retriever -- "C. Loads Store" --> VectorStore
    Retriever -- "D. Gets Relevant Docs" --> Prompt
    QA_EP -- "E. Passes Question" --> Prompt
    Prompt -- "F. Formats Prompt" --> LLM
    LLM -- "G. API Call" --> GoogleGenerativeAI
    LLM -- "H. Returns Answer" --> QA_EP
    QA_EP -- "I. Sends Response" --> User

    %% Secrets Connections
    Secrets -- "API Keys" --> GoogleGenerativeAI
    Secrets -- "OAuth Credentials" --> GoogleDriveAPI