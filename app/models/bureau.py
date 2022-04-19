from pydantic import BaseModel

class Bureau(BaseModel):
    check: bool
    client_data: dict
    bureau_data: dict