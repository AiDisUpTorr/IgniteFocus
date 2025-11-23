from app.models.config import settings
import requests 
import json

# Very small wrapper for Ollama local HTTP API
# This assumes Ollama is running locally (default at http://localhost:11434)

def generate_completion(prompt: str, model: str | None = None, max_tokens: int = 512) -> str:
    model = model or settings.OLLAMA_MODEL
    url = f"{settings.OLLAMA_HOST}/v1/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": max_tokens,
    }

    resp = requests.post(url, json=payload, timeout=30)
    resp.raise_for_status()

    data = resp.json()

    # Ollama's response shape may vary; try common fields
    if isinstance(data, dict) and "output" in data:
        # some Ollama builds return {'id':..., 'output': '...'}
        return data.get("output")

    # fallback: return raw JSON string
    return json.dumps(data)
