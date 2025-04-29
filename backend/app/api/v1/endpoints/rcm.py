from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ...schemas import rcm as rcm_schema
from ...crud import crud_rcm
from ...api.deps import get_db

router = APIRouter()

@router.get("/status")
def get_status():
    return {"status": "RCM API is running"}

@router.post("/rcms/", response_model=rcm_schema.RCM)
def create_rcm(rcm: rcm_schema.RCMCreate, db: Session = Depends(get_db)):
    return crud_rcm.create_rcm(db=db, rcm=rcm)

@router.get("/rcms/", response_model=list[rcm_schema.RCM])
def read_rcms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_rcm.get_rcms(db=db, skip=skip, limit=limit)

@router.get("/rcms/{rcm_id}", response_model=rcm_schema.RCM)
def read_rcm(rcm_id: int, db: Session = Depends(get_db)):
    db_rcm = crud_rcm.get_rcm(db=db, rcm_id=rcm_id)
    if db_rcm is None:
        raise HTTPException(status_code=404, detail="RCM not found")
    return db_rcm
