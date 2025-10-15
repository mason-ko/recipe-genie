from pydantic import BaseModel, ConfigDict
from typing import Optional

# Shared properties
class IngredientBase(BaseModel):
    name: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "name": "Tomato"
            }
        }
    )

# Properties to receive on ingredient creation
class IngredientCreate(IngredientBase):
    name: str

# Properties to receive on ingredient update
class IngredientUpdate(IngredientBase):
    pass

# Properties shared by models stored in DB
class IngredientInDBBase(IngredientBase):
    id: int
    name: str
    owner_id: int

    model_config = ConfigDict(from_attributes=True)

# Properties to return to client
class Ingredient(IngredientInDBBase):
    pass

# Properties stored in DB
class IngredientInDB(IngredientInDBBase):
    pass
