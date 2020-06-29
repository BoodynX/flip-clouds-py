from pydantic import BaseModel


class NewFlipCardRequestModel(BaseModel):
    front: str
    back: str
