from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/status")
def get_status():
    return {"status": "RCM API is running"}
