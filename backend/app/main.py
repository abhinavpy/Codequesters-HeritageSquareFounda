from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import ingestion, qa
# from app.core.config import settings

app = FastAPI(
    title="Heritage Square AI API",
    description="API for interacting with the Heritage Square AI agent.",
    version="1.0.0"
)

# --- Add this CORS middleware section ---
origins = [
    "http://localhost",
    "http://localhost:5173", # The default port for Vite React projects
    "http://127.0.0.1:5173",
    # Add any other origins you might use
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)
# --- End of CORS middleware section ---

# Include the ingestion router
app.include_router(
    ingestion.router,
    prefix="/api/v1/ingestion",
    tags=["Ingestion"]
)

# Include the QA router
app.include_router(
    qa.router,
    prefix="/api/v1/qa",
    tags=["Q&A"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Heritage Square AI API"}
