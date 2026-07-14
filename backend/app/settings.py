import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
MODEL_DEEPSEEK_V4_FLASH = os.getenv("MODEL_DEEPSEEK_V4_FLASH", "deepseek/deepseek-v4-flash")

