from pydantic import BaseModel

class Check(BaseModel):
    check = bool 
    client_data = dict
    bureau_data = dict