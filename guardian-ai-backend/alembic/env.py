from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from app.database.session import get_async_engine

config = context.config

fileConfig(config.config_file_name)

target_metadata = None  # Set this to your model's MetaData object

def run_migrations_online():
    connectable = get_async_engine()

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_bind_param=True,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
    )
    context.run_migrations()
else:
    run_migrations_online()