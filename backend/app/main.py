from fastapi import FastAPI
from .api.v1.endpoints import rcm

app = FastAPI(
    title="Quanntaum Predict RCM Analysis API",
    version="0.1.0"
)

# Include the RCM router
app.include_router(rcm.router, prefix="/api/v1/rcm")
