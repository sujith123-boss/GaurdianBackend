from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from structlog import get_logger

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import setup_request_logging

log = get_logger()

# Initialize FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    openapi_url="/openapi.json",
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
)

from structlog.contextvars import bind_contextvars, clear_contextvars

def setup_request_logging(request_id: str, correlation_id: str = None):
    """
    Bind request ID and correlation ID to the logging context.
    """
    clear_contextvars()
    bind_contextvars(request_id=request_id)
    if correlation_id:
        bind_contextvars(correlation_id=correlation_id)

# Lifespan events
@app.on_event("startup")
async def on_startup():
    """
    Startup event to initialize resources.
    """
    log.info("Starting application", app_name=settings.APP_NAME, version=settings.APP_VERSION)
    setup_request_logging(request_id="startup")  # Example request ID for startup logs

@app.on_event("shutdown")
async def on_shutdown():
    """
    Shutdown event to clean up resources.
    """
    log.info("Shutting down application", app_name=settings.APP_NAME)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"] if settings.DEBUG else ["yourdomain.com"],  # Replace with your domain
)

# Include the API router
app.include_router(api_router)

# Logging middleware
@app.middleware("http")
async def log_requests(request, call_next):
    """
    Middleware to log incoming requests and responses.
    """
    setup_request_logging(request_id=request.headers.get("X-Request-ID", "unknown"))
    log.info("Request received", method=request.method, url=request.url.path)
    response = await call_next(request)
    log.info("Response sent", status_code=response.status_code)
    return response