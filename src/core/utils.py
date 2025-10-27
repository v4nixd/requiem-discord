import os

from dotenv import load_dotenv

load_dotenv()

def fetch_token() -> str:
    return os.getenv("TOKEN")