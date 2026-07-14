# dndai-vtt
D&D 5e Multiplayer VTT + AI Dungeon Master (DeepSeek v4 Flash via OpenRouter) + Firebase real-time lobby state.

## Local dev
- Backend (FastAPI): `cd backend && python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt && uvicorn app.main:app --reload --port 8000`
- Frontend (Vite): `cd frontend && npm install && npm run dev`

## Environment
- Copy `backend/.env.example` to `backend/.env` and fill in `OPENROUTER_API_KEY`.

## Firebase
- Fill Firebase config in `frontend/src/firebase/firebaseConfig.ts`.

