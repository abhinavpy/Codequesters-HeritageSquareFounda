from pathlib import Path
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
    DirectoryLoader,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.db.metadata import init_db, get_all_metadata, upsert_metadata, delete_metadata

def load_from_directory(source_path: Path):
    """Loads documents from a directory using various loaders."""
    print(f"\nLoading documents from {source_path}...")
    docs = []
    for file_path in source_path.glob("**/*"):
        if file_path.suffix == ".pdf":
            loader = PyPDFLoader(str(file_path))
        elif file_path.suffix == ".txt":
            loader = TextLoader(str(file_path))
        elif file_path.suffix == ".docx":
            loader = UnstructuredWordDocumentLoader(str(file_path))
        else:
            continue
        docs.extend(loader.load())
    print(f"Successfully loaded {len(docs)} document objects.")
    return docs

def chunk_documents(docs: list):
    """Splits documents into smaller chunks."""
    print("\nChunking documents...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_documents(docs)
    print(f"Split {len(docs)} documents into {len(chunks)} chunks.")
    return chunks

def create_and_save_vector_store(chunks: list, save_path: Path):
    """Creates a FAISS vector store from chunks and saves it to disk."""
    if not chunks:
        print("No chunks to process. Skipping vector store creation.")
        return

    print("\nCreating vector store with Google Generative AI embeddings...")
    # Ensure your GOOGLE_API_KEY is in the .env file
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    # FAISS is efficient for similarity search
    vector_store = FAISS.from_documents(chunks, embeddings)
    
    save_path.mkdir(parents=True, exist_ok=True)
    vector_store.save_local(str(save_path))
    print(f"Vector store created and saved to '{save_path}'")

def sync_and_update_vector_store(drive_files, vector_store_path):
    """
    Syncs the vector store with the current state of Drive files.
    Adds new, updates changed, and removes deleted vectors.
    """
    print("Initializing metadata DB...")
    init_db()
    local_meta = get_all_metadata()
    drive_ids = {f['id'] for f in drive_files}

    # Load or create vector store
    if vector_store_path.exists():
        vector_store = FAISS.load_local(str(vector_store_path), GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
    else:
        vector_store = None

    # 1. Delete vectors for files removed from Drive
    for drive_id, row in local_meta.items():
        if drive_id not in drive_ids:
            print(f"Deleting vector for removed file: {row[1]}")
            if vector_store:
                vector_store.delete([row[3]])  # row[3] is vector_id
            delete_metadata(drive_id)

    # 2. Add or update vectors for new/changed files
    for file in drive_files:
        drive_id = file['id']
        file_name = file['name']
        modified_time = file['modified_time']
        local_path = file['local_path']
        meta = local_meta.get(drive_id)
        needs_update = not meta or meta[2] != modified_time  # meta[2] is modified_time

        if needs_update:
            print(f"{'Updating' if meta else 'Adding'} vector for: {file_name}")
            docs = load_from_directory(Path(local_path).parent)  # Load single file
            chunks = chunk_documents(docs)
            embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            if not vector_store:
                vector_store = FAISS.from_documents(chunks, embeddings)
            else:
                vector_ids = vector_store.add_documents(chunks)
            # Save/Update metadata
            upsert_metadata(drive_id, file_name, modified_time, drive_id)  # Use drive_id as vector_id

    # 3. Save vector store
    if vector_store:
        vector_store.save_local(str(vector_store_path))
        print(f"Vector store synced and saved to '{vector_store_path}'")

def get_retriever(vector_store_path):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local(str(vector_store_path), embeddings)
    return vector_store.as_retriever()
