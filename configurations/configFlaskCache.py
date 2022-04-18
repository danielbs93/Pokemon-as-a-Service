from pydantic import BaseSettings


class CacheCredentials(BaseSettings):
    CACHE_DEBUG: str
    CACHE_TYPE: str
    TIMEOUT: int
