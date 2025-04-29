from pydantic import BaseModel

class RCM(BaseModel):
    id: int
    name: str
    description: str
