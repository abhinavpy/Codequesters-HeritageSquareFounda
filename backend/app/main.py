from fastapi import FastAPI
from app.api.v1.routes import ingestion, qa

app = FastAPI(
    title="Heritage Square AI API",
    description="API for interacting with the Heritage Square AI agent.",
    version="1.0.0"
)

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
