
import os
from functools import lru_cache
from dotenv import load_dotenv
load_dotenv()


class Settings:
    def __init__(self):
        # Core
        self.PORT: int = int(os.getenv("PORT", 8000))
        self.DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://root:1234@localhost:32768/nasa_biosc")
        self.CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", "http://localhost:3000")

        # Embeddings / LLM
        self.EMBED_PROVIDER: str = os.getenv("EMBED_PROVIDER", "ollama")  # openai | ollama
        self.EMBED_MODEL: str = os.getenv("EMBED_MODEL", "nomic-embed-text")
        self.OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
        self.GROQ_API_KEY: str | None = os.getenv("GROQ_API_KEY")
        self.GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY")

        self.LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "ollama")      # openai | ollama | groq | gemini
        self.LLM_MODEL: str = os.getenv("LLM_MODEL", "mistral")

        # Paths
        self.INDICES_DIR: str = os.path.abspath(os.path.join(os.getcwd(), "..", "data", "indices"))
        self.UPLOADS_DIR: str = os.path.abspath(os.path.join(os.getcwd(), "..", "uploads"))
        os.makedirs(self.INDICES_DIR, exist_ok=True)
        os.makedirs(self.UPLOADS_DIR, exist_ok=True)

        # LangSmith
        self.LANGCHAIN_TRACING_V2: bool = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() in ("true", "1", "yes")
        self.LANGCHAIN_PROJECT: str | None = os.getenv("LANGCHAIN_PROJECT")
        self.LANGCHAIN_API_KEY: str | None = os.getenv("LANGCHAIN_API_KEY")

@lru_cache
def get_settings():
    s = Settings()
    return s
