from fastapi.middleware.cors import CORSMiddleware

from .schemas import ChatRequest, ChatResponse
from .prompts.system_prompt import SYSTEM_PROMPT
from .openrouter_client import call_openrouter

app = FastAPI(title="DND AI DM Backend")

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat", response_model=ChatResponse)
async def api_chat(req: ChatRequest):
    system_message = {"role": "system", "content": SYSTEM_PROMPT}

    # Convert history into OpenAI-style roles:
    history_messages = []
    for m in req.chat_history:
        role = "user" if m.author == "PLAYER" else "assistant"
        history_messages.append({"role": role, "content": m.text})

    state_context = {
        "lobby_id": req.lobby_id,
        "player": {
            "id": req.player_id,
            "name": req.player_name,
            "ac": req.player_ac,
            "max_hp": req.player_max_hp,
            "passive_perception": req.player_passive_perception,
        },
        "current_state": req.current_state,
        "action_type": req.action_type,
    }

    user_message = {
        "role": "user",
        "content": (
            "CURRENT GAME STATE CONTEXT (JSON):\n"
            f"{state_context}\n\n"
            "CHAT HISTORY (latest):\n"
            f"{[h.text for h in req.chat_history][-20:]}\n\n"
            "LATEST PLAYER MESSAGE:\n"
            f"{req.message}\n\n"
            "Return JSON only following the schema."
        ),
    }

    result = await call_openrouter([system_message] + history_messages + [user_message])

    dm_message = result.get("dm_message", "")
    return ChatResponse(dm_message=dm_message, raw_json=result)

