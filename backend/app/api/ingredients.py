from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api import deps
from app.schemas.ingredient import Ingredient, IngredientCreate
from app.crud import crud_ingredient
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[Ingredient])
async def read_ingredients(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Retrieve ingredients for the current user.
    """
    ingredients = crud_ingredient.get_user_ingredients(db, user_id=current_user.id)
    return ingredients

@router.post("/", response_model=Ingredient)
async def create_ingredient(
    *, 
    db: Session = Depends(deps.get_db), 
    ingredient_in: IngredientCreate, 
    current_user: User = Depends(deps.get_current_user)
):
    """
    Create new ingredient for the current user.
    """
    ingredient = crud_ingredient.create_user_ingredient(
        db, ingredient_in=ingredient_in, user_id=current_user.id
    )
    return ingredient

@router.delete("/{ingredient_id}", response_model=Ingredient)
async def delete_ingredient(
    *, 
    db: Session = Depends(deps.get_db), 
    ingredient_id: int, 
    current_user: User = Depends(deps.get_current_user)
):
    """
    Delete an ingredient for the current user.
    """
    ingredient = crud_ingredient.delete_user_ingredient(
        db, ingredient_id=ingredient_id, user_id=current_user.id
    )
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient
