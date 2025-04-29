from sqlalchemy.orm import Session
from ..db import models
from ..schemas import rcm as rcm_schema

def get_rcm(db: Session, rcm_id: int):
    return db.query(models.RCM).filter(models.RCM.id == rcm_id).first()

def get_rcms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RCM).offset(skip).limit(limit).all()

def create_rcm(db: Session, rcm: rcm_schema.RCMCreate):
    db_rcm = models.RCM(name=rcm.name, description=rcm.description)
    db.add(db_rcm)
    db.commit()
    db.refresh(db_rcm)
    return db_rcm
