from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(
    prefix="/budget",
    tags=["Budget"]
)


class BudgetInput(BaseModel):
    income: float
    rent: float
    food: float
    transport: float
    other_expenses: float


@router.post("/calculate")
def calculate_budget(data: BudgetInput):

    total_expenses = (
        data.rent
        + data.food
        + data.transport
        + data.other_expenses
    )

    remaining_budget = data.income - total_expenses

    return {
        "income": data.income,
        "total_expenses": total_expenses,
        "remaining_budget": remaining_budget
    }