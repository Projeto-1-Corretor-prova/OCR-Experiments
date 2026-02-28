from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.chat_models import BaseChatModel

from src.settings import Settings

def get_chat(model: str) -> BaseChatModel:
    match Settings.chat_type:
        case "ollama":
            return ChatOllama(base_url=Settings.chat_url, model=model, temperature=Settings.temperature)
        case "google":
            return ChatGoogleGenerativeAI(
                model=model, 
                api_key=Settings.api_key, 
                temperature=Settings.temperature, 
                max_tokens=None,
                timeout=None,max_retries=2,
                )
        case "openai":
            return ChatOpenAI(model_name=model, api_key=Settings.api_key, temperature=Settings.temperature)
        case _: 
            raise ValueError(f"Unsupported CHAT_TYPE: {Settings.chat_type}")
        
def get_chat_by_env() -> BaseChatModel:
    return get_chat(Settings.model)