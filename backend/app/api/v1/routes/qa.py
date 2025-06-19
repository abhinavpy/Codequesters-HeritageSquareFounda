from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag import rag_chain
from app.core.config import DATA_PATH

router = APIRouter()

class QARequest(BaseModel):
    drive_folder_id: str
    question: str

@router.post("/ask")
def ask_qa(request: QARequest):
    vector_store_path = DATA_PATH / request.drive_folder_id / "vector_store"
    answer = rag_chain(vector_store_path, request.question)
    return {"answer": answer}