import httpx
import json
from .settings import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, MODEL_DEEPSEEK_V4_FLASH

def _parse_json_from_model(text: str) -> dict:
    # Model must return JSON only; still parse defensively.
    return json.loads(text)

async def call_openrouter(messages: list[dict]) -> dict:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    body = {
        "model": MODEL_DEEPSEEK_V4_FLASH,
        "messages": messages,
        "temperature": 0.6,
    }

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(OPENROUTER_BASE_URL, headers=headers, json=body)
        r.raise_for_status()
        data = r.json()

    content = data["choices"][0]["message"]["content"]
    return _parse_json_from_model(content)

