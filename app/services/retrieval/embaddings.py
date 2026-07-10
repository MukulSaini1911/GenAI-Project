import time
import logfire
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.config import settings


BATCH_SIZE = 50
_GEMINI_DIM = 3072
_FALLBACK_DIM = 768     # all-mpnet-base-v2 has 768 dimensions

_active_model = None
_model_type = None

def _probe_gemini():
    """Probe the Gemini API to check if it is available and working. Retruns model or None."""
    return

def _load_fallback():
    return

def _init():
    return

def get_embedding_dim() -> int:
    """Return the vector dimension of the active embedding model. Call after _init()."""
    return 

def _embed_batch(batch: list[str]) -> list[list[float]]:
    """Embed a batch of texts using the active embedding model. Call after _init()."""
    return

def embed_query(query: str) -> list[float]:
    """Embed a single query using the active embedding model. Call after _init()."""
    return

def embed_text(text: str) -> list[float]:
    """Embed a single text using the active embedding model. Call after _init()."""
    return

