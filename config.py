from pydantic import BaseSettings, SecretStr
import os


class Settings(BaseSettings): 
    auth_secret : SecretStr = os.environ.get("APPLICATION_SECRET")
    current_host: str = os.environ.get("CURRENT_HOST")
    privateMode: bool = os.environ.get("PRIVATE_MODE")


settings = Settings()

print("hosts", settings.privateMode)