from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    api_id: int
    api_hash: str
    session_key: str

    monitor_channels: list[str]
    send_to_channel: str

    class Config:
        env_file = ".env"


settings = Settings()
