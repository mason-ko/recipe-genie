from pydantic import BaseModel, ConfigDict
from typing import Optional

# Shared properties
class RecipeBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    ingredients: Optional[str] = None
    instructions: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "title": "Tomato Soup",
                "description": "A simple and delicious tomato soup.",
                "ingredients": "Tomatoes, Onions, Garlic, Vegetable Broth",
                "instructions": "1. Chop onions and garlic. 2. Sauté in a pot. 3. Add tomatoes and broth. 4. Simmer for 20 minutes."
            }
        }
    )

# Properties to receive on recipe creation
class RecipeCreate(RecipeBase):
    title: str

# Properties to receive on recipe update
class RecipeUpdate(RecipeBase):
    pass

# Properties shared by models stored in DB
class RecipeInDBBase(RecipeBase):
    id: int
    title: str
    owner_id: int

    model_config = ConfigDict(from_attributes=True)

# Properties to return to client
class Recipe(RecipeInDBBase):
    pass

# Properties stored in DB
class RecipeInDB(RecipeInDBBase):
    pass
