from fastapi import FastAPI
from app.api.routes.analyze import router as analyze_router

app = FastAPI(
    title="Vibe Security",
    description="비전공자도 이해할 수 있는 보안 취약점 분석 서비스",
    version="0.1.0",
)

app.include_router(analyze_router)
