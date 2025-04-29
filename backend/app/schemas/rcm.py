from pydantic import BaseModel

class RCMBase(BaseModel):
    name: str
    description: str

class RCMCreate(RCMBase):
    pass

class RCM(RCMBase):
    id: int

    class Config:
        orm_mode = True
