from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from app.api import deps
from app.models.user import User
from app.services import gemini
from app.schemas.recipe import Recipe, RecipeCreate
from app.crud import crud_recipe, crud_ingredient

router = APIRouter()

class IngredientsInput(BaseModel):
    ingredients: List[str]

@router.post("/generate", response_model=str)
async def generate_recipe(
    *, 
    ingredients_in: IngredientsInput,
    current_user: User = Depends(deps.get_current_user)
):
    """
    Generate a new recipe based on ingredients.
    """
    recipe_text = gemini.generate_recipe(
        ingredients_in.ingredients, 
        current_user.dietary_preferences, 
        current_user.allergies
    )
    return recipe_text

@router.post("/", response_model=Recipe)
async def create_recipe(
    *, 
    db: Session = Depends(deps.get_db), 
    recipe_in: RecipeCreate, 
    current_user: User = Depends(deps.get_current_user)
):
    """
    Create new recipe for the current user.
    """
    recipe = crud_recipe.create_user_recipe(
        db, recipe_in=recipe_in, user_id=current_user.id
    )
    return recipe

@router.get("/", response_model=List[Recipe])
async def read_recipes(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Retrieve recipes for the current user.
    """
    recipes = crud_recipe.get_user_recipes(db, user_id=current_user.id)
    return recipes

@router.get("/{recipe_id}", response_model=Recipe)
async def read_recipe(
    *, 
    db: Session = Depends(deps.get_db), 
    recipe_id: int, 
    current_user: User = Depends(deps.get_current_user)
):
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.get("/{recipe_id}/shopping-list", response_model=List[str])
async def get_shopping_list(
    *,
    db: Session = Depends(deps.get_db),
    recipe_id: int,
    current_user: User = Depends(deps.get_current_user)
):
    """
    Get a shopping list for a specific recipe.
    """
    recipe = crud_recipe.get_recipe(db, recipe_id=recipe_id, user_id=current_user.id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    user_ingredients = crud_ingredient.get_user_ingredients(db, user_id=current_user.id)
    user_ingredient_names = {ingredient.name.lower() for ingredient in user_ingredients}

    recipe_ingredients_str = recipe.ingredients or ""
    recipe_ingredients = {item.strip().lower() for item in recipe_ingredients_str.split(",")}

    shopping_list = [item for item in recipe_ingredients if item not in user_ingredient_names]
    return shopping_list

@router.delete("/{recipe_id}", response_model=Recipe)
async def delete_recipe(
    *, 
    db: Session = Depends(deps.get_db), 
    recipe_id: int, 
    current_user: User = Depends(deps.get_current_user)
):
    """
    Delete a recipe for the current user.
    """
    recipe = crud_recipe.delete_user_recipe(
        db, recipe_id=recipe_id, user_id=current_user.id
    )
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe