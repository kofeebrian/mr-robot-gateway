from pydantic import BaseModel

# Example of Schemas for req-res:

class Fuzzing_Result(BaseModel):
    message: str
    total: int
    data: list
    class Config:
        orm_mode = True