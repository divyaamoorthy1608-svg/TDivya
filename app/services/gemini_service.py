import json
from typing import Any

from google import genai
from google.genai import types

from app.config import settings


def _client():

    if not settings.gemini_api_key:
        return None

    return genai.Client(
        api_key=settings.gemini_api_key
    )


def _generate(
    prompt: str,
    image_bytes: bytes | None = None,
) -> dict[str, Any]:

    client = _client()

    if client is None:
        raise RuntimeError(
            "Gemini API key is not configured."
        )

    contents: list[Any] = [
        prompt
    ]

    if image_bytes:

        contents.append(
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/jpeg",
            )
        )

    response = client.models.generate_content(
        model=settings.gemini_model,
        contents=contents,
        config=types.GenerateContentConfig(
            temperature=0.4,
            response_mime_type="application/json",
        ),
    )

    text = response.text or "{}"

    return json.loads(text)


def generate_recommendation(
    planner_type: str,
    request_data: dict,
    catalog: list[dict],
    image_bytes: bytes | None = None,
) -> dict[str, Any]:

    catalog_text = json.dumps(
        catalog,
        ensure_ascii=False,
    )

    if planner_type == "home":

        task = f"""
Create a practical home-budget recommendation.

User request:
{json.dumps(request_data, ensure_ascii=False)}

Available demo catalog:
{catalog_text}

Return JSON with exactly these keys:
title, description, estimated_total, tips, items, source

items must be a list of objects containing:
name, category, estimated_price, reason, link

Stay within the user's budget when possible.
Do not invent live prices or inventory.
"""

    elif planner_type == "party":

        task = f"""
Create a practical party plan within the user's budget.

User request:
{json.dumps(request_data, ensure_ascii=False)}

Available demo catalog:
{catalog_text}

Return JSON with exactly these keys:
title, description, estimated_total, tips, items, source

items must be a list of objects containing:
name, category, estimated_price, reason, link

Use the catalog links as demo links only.
Do not claim live prices or stock.
"""

    else:

        task = f"""
Create a practical jewelry recommendation.

User request:
{json.dumps(request_data, ensure_ascii=False)}

Available demo catalog:
{catalog_text}

If an image is provided, use it only for broad
outfit/color/style coordination.

Do not identify the person.

Return JSON with exactly these keys:
title, description, estimated_total, tips, items, source

items must be a list of objects containing:
name, category, estimated_price, reason, link
"""

    return _generate(
        task,
        image_bytes=image_bytes,
    )