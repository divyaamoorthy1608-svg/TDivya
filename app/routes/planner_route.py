from fastapi import APIRouter
from pydantic import BaseModel

from app.services.recommendation_service import create_recommendation


router = APIRouter(
    prefix="/planner",
    tags=["Planner"]
)


class PlannerRequest(BaseModel):
    planner_type: str
    budget: float
    room: str | None = None
    style: str | None = None
    theme: str | None = None
    guests: int | None = None
    jewelry_type: str | None = None


@router.post("/recommend")
def recommend(data: PlannerRequest):

    request_data = data.model_dump()

    return create_recommendation(
        planner_type=data.planner_type,
        request_data=request_data
    )