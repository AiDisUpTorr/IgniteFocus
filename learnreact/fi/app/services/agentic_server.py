# placeholder for higher-level agent orchestration (chaining LLM calls, tools, etc.)
from typing import Any
from app.services.llm_server import generate_completion


class Agent:
    def __init__(self, model: str | None = None):
        self.model = model


def ask(self, prompt: str) -> str:
# orchestrate multiple calls or tool use here
    return generate_completion(prompt, model=self.model)