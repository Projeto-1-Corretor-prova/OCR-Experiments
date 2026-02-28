from dotenv import load_dotenv

from os import getenv

load_dotenv()

class Settings:
    tesseract_language = getenv("TESSERACT_LANGUAGE")
    tesseract_configuration = getenv("TESSERACT_CONFIGURATION")
    chat_url: str = getenv("CHAT_URL")
    model: str = getenv("MODEL")
    api_key: str = getenv("API_KEY")
    chat_type: str = getenv("CHAT_TYPE")
    temperature: int = int(getenv("TEMPERATURE")) if getenv("TEMPERATURE") else None