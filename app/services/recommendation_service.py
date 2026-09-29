from app.services.catalog_service import get_catalog
from app.services.gemini_service import generate_recommendation


def _fallback(
    planner_type: str,
    request_data: dict,
) -> dict:

    budget = float(
        request_data["budget"]
    )

    catalog = get_catalog(
        planner_type
    )

    if planner_type == "home":

        title = (
            f"{request_data.get('style', 'Modern')} "
            f"{request_data.get('room', 'Room')} Plan"
        )

        description = (
            "A simple budget-friendly room setup "
            "using the demo catalog. Prices are estimates "
            "and should be checked on the linked site."
        )

    elif planner_type == "party":

        title = (
            f"{request_data.get('theme', 'Simple')} "
            "Party Plan"
        )

        description = (
            f"A simple plan for "
            f"{request_data.get('guests', 1)} guests "
            "with spending kept around the requested budget."
        )

    else:

        title = (
            f"{request_data.get('jewelry_type', 'Jewelry')} "
            "Suggestion"
        )

        description = (
            "A simple jewelry combination based on "
            "the selected occasion, budget and preferences."
        )

    chosen = []

    total = 0.0

    for item in catalog:

        if total + item["price"] <= budget:

            chosen.append(
                {
                    "name": item["name"],
                    "category": item["category"],
                    "estimated_price": item["price"],
                    "reason": (
                        "Fits the selected budget "
                        "and preference."
                    ),
                    "link": item["link"],
                }
            )

            total += item["price"]

        if len(chosen) >= 4:
            break

    if not chosen and catalog:

        item = catalog[0]

        chosen.append(
            {
                "name": item["name"],
                "category": item["category"],
                "estimated_price": item["price"],
                "reason": (
                    "A starting option from "
                    "the demo catalog."
                ),
                "link": item["link"],
            }
        )

        total = item["price"]

    return {
        "title": title,

        "description": description,

        "estimated_total": round(
            total,
            2,
        ),

        "tips": [
            (
                "Check the seller page for the "
                "current price before purchasing."
            ),
            (
                "Keep a small part of the budget "
                "for unexpected expenses."
            ),
            (
                "The displayed marketplace links are "
                "demo links, not live inventory results."
            ),
        ],

        "items": chosen,

        "source": (
            "Local fallback recommendation"
        ),
    }


def create_recommendation(
    planner_type: str,
    request_data: dict,
    image_bytes: bytes | None = None,
) -> dict:

    catalog = get_catalog(
        planner_type
    )

    try:

        result = generate_recommendation(
            planner_type=planner_type,
            request_data=request_data,
            catalog=catalog,
            image_bytes=image_bytes,
        )

        result.setdefault(
            "source",
            "Google Gemini",
        )

        result.setdefault(
            "tips",
            [],
        )

        result.setdefault(
            "items",
            [],
        )

        result.setdefault(
            "estimated_total",
            request_data["budget"],
        )

        return result

    except Exception:

        return _fallback(
            planner_type,
            request_data,
        )