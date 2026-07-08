# README.md

# Guardian AI Backend

This is the backend foundation for the Guardian AI project, built using Python 3.13+, FastAPI, SQLAlchemy 2.0 (async), PostgreSQL, Alembic, Pydantic v2, Docker, Docker Compose, structlog, and Redis. This project provides a clean architecture with a focus on maintainability and scalability.

## Project Structure

```
guardian-ai-backend
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── logging.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── health.py
│   │   └── router.py
│   └── database
│       ├── __init__.py
│       ├── base.py
│       └── session.py
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── requirements.txt
└── alembic
    ├── env.py
    ├── README
    ├── versions
    │   └── __init__.py
    └── __init__.py
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd guardian-ai-backend
   ```

2. **Create a `.env` file:**
   Copy the `.env.example` file to `.env` and fill in the required environment variables.

3. **Build and run the application using Docker Compose:**
   ```bash
   docker-compose up --build
   ```

4. **Access the API:**
   The FastAPI application will be available at `http://localhost:8000`.

## API Endpoints

- **Health Check**
  - `GET /health`: Returns the health status of the application.

- **Version**
  - `GET /version`: Returns the current version of the API.

## Logging

Structured logging is implemented using `structlog`. Logs will be output to the console and can be configured in `app/core/logging.py`.

## Database Migrations

Database migrations are managed using Alembic. To create a new migration, run:
```bash
docker-compose exec app alembic revision --autogenerate -m "migration_message"
```

To apply migrations, run:
```bash
docker-compose exec app alembic upgrade head
```

## Dependencies

The project dependencies are listed in `requirements.txt`. Make sure to install them before running the application.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.