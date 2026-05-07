from fastapi import APIRouter

router = APIRouter()


@router.post("/analyze")
async def analyze():
    return {"message": "분석 엔드포인트 준비 중"}
