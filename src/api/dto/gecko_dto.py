from pydantic import BaseModel, Field


class GeckoRequestDto(BaseModel):
    name: str
    price: int = Field(gt=0)
    owner_id: int = Field(gt=0)
