from pydantic import BaseModel


class NewFlipCardResponseModel(BaseModel):
    id_: str
    front: str
    back: str
