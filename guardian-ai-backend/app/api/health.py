from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["health"])
async def health_check():
    return {"status": "healthy"}

@router.get("/version", tags=["version"])
async def version():
    return {"version": "1.0.0"}