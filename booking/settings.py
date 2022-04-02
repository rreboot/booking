from typing import List, Optional

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    # API_V1_STR: str = "/api/v1"
    # openssl rand -hex 32
    SECRET_KEY: str = "b754fb924e13b7ae288f4c5a9e437759d52066003d24d1935a12204094af85e3"
    ALGORITHM: str = "HS256"

    # 60 minutes * 24 hours = 1 day
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # @validator("BACKEND_CORS_ORIGINS", pre=True)
    # def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
    #     if isinstance(v, str) and not v.startswith("["):
    #         return [i.strip() for i in v.split(",")]
    #     elif isinstance(v, (list, str)):
    #         return v
    #     raise ValueError(v)

    DATABASE_URI: Optional[str] = 'postgresql://postgres:postgres@localhost:5432/booking'

    # FIRST_SUPERUSER: EmailStr = "admin@recipeapi.com"
    # FIRST_SUPERUSER_PW: str = "CHANGEME"

    class Config:
        case_sensitive = True


settings = Settings()
