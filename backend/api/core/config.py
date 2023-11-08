from pydantic import BaseSettings, BaseModel

class Settings(BaseSettings):
    PROJECT_NAME: str = 'Container Topology'
    API_V1_STR: str = '/api'

settings = Settings()
