import sys
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    redis_url: str = "redis://localhost:6379"

    model_config = {"env_file": ".env"}


def get_settings() -> Settings:
    try:
        return Settings()
    except Exception:
        print("[ERROR] 필수 환경변수가 설정되지 않았습니다. .env 파일에 OPENAI_API_KEY를 입력하세요.")
        sys.exit(1)


settings = get_settings()
