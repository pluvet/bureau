from pydantic import BaseModel

class Bureau(BaseModel):
    id_number: str
    name: str
    lastname: str