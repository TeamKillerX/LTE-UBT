import os

from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")
WEB_HEALTH_APP = os.getenv("WEB_HEALTH_APP", "").lower() in {"1", "true", "yes"}
UBT_SECRET = os.getenv("UBT_SECRET")
