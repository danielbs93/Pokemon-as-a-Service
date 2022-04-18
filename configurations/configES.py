from pydantic import BaseSettings


class EScredentials(BaseSettings):
    USER_NAME: str
    PASSWORD: str
    CLOUD_ID: str
