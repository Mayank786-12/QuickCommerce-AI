"""Pydantic request models used to validate incoming API data."""

from pydantic import BaseModel, Field


class CreateOrderRequest(BaseModel):
    product_id: int = Field(gt=0)
    quantity: int = Field(default=1, ge=1, le=100)


class AssistantQuestion(BaseModel):
    question: str = Field(min_length=1, max_length=500)
