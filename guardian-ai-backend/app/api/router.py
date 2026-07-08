from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.api.health import router as health_router

# Create the main API router
api_router = APIRouter()

# Include health-related routes
api_router.include_router(health_router, prefix="/health", tags=["Health"])

@api_router.get("/", response_class=JSONResponse, tags=["Root"])
async def root():
    """
    Root endpoint to indicate the service is running.
    """
    return {"message": "Guardian is up and running"}