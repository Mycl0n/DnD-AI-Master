from typing import Any, Literal, Optional
from pydantic import BaseModel

class ChatMessage(BaseModel):
    author: Literal["PLAYER", "DM", "SYSTEM"]
    text: str
    playerId: Optional[str] = None

class ChatRequest(BaseModel):
    lobby_id: str
    player_id: str
    player_name: str
    player_ac: int
    player_max_hp: int
    player_passive_perception: int

    current_state: dict[str, Any]
    chat_history: list[ChatMessage]

    message: str
    action_type: Literal["Investigate", "Talk", "Attack", "Custom"] = "Custom"

class ChatResponse(BaseModel):
    dm_message: str
    raw_json: dict[str, Any]

