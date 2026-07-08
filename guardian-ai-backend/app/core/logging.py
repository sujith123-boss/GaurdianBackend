import logging
import structlog
from structlog.contextvars import bind_contextvars, clear_contextvars
from structlog.processors import JSONRenderer, TimeStamper
from structlog.stdlib import add_log_level, filter_by_level
from structlog.threadlocal import merge_threadlocal

from app.core.config import settings

# Configure standard library logging
def configure_logging() -> None:
    """
    Configure logging for the application.
    """
    logging.basicConfig(
        format="%(message)s",
        level=logging.DEBUG if settings.DEBUG else logging.INFO,
    )

    structlog.configure(
        processors=[
            merge_threadlocal,  # Merge thread-local context (e.g., request ID)
            bind_contextvars,  # Bind context variables (e.g., correlation ID)
            add_log_level,  # Add log level to the log entry
            filter_by_level,  # Filter logs by the configured log level
            TimeStamper(fmt="iso", utc=True),  # Add ISO 8601 UTC timestamp
            JSONRenderer(),  # Render logs as JSON
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

# Utility function to configure request and correlation IDs
def setup_request_logging(request_id: str, correlation_id: str = None):
    """
    Bind request ID and correlation ID to the logging context.
    """
    clear_contextvars()
    bind_contextvars(request_id=request_id)
    if correlation_id:
        bind_contextvars(correlation_id=correlation_id)


# Create a global logger instance
logger = structlog.get_logger()