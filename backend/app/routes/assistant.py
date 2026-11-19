"""Natural-language assistant endpoint."""

from fastapi import APIRouter, HTTPException

from app.schemas import AssistantQuestion
from app.services.recommendation import get_assistant_answer

router = APIRouter(prefix="/api", tags=["AI Assistant"])


@router.post("/assistant")
def ask_assistant(request: AssistantQuestion):
    """Accept a question and return an assistant response."""
    question = request.question.strip()

    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    return get_assistant_answer(question)
