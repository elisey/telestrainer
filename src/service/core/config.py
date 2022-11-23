from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    api_id: int
    api_hash: str
    session_name: str

    monitor_channels: list[int]
    send_to_channel: int

    strain_parts: list[str]

    class Config:
        env_file = ".env"


settings = Settings()
