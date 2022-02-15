from pydantic import BaseModel

# Example of Schemas for req-res:

class Test_input(BaseModel):
    message: str
    class Config:
        orm_mode = True