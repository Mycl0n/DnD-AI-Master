import os
from dotenv import load_dotenv

load_dotenv()

# Use safe defaults so module import doesn't crash before .env is loaded.
# In production you should still ensure OPENROUTER_API_KEY is set.
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
MODEL_DEEPSEEK_V4_FLASH = os.getenv("MODEL_DEEPSEEK_V4_FLASH", "deepseek/deepseek-v4-flash")

