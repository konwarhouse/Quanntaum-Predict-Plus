import os

POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "rcm_db")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "db")
