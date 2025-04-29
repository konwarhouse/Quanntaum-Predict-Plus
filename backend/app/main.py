from fastapi import FastAPI

from .db.models import Base
from .db.session import engine
from .api.v1.endpoints import rcm

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(rcm.router, prefix="/api/v1")
