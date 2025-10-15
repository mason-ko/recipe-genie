from sqlalchemy.orm import Session
from typing import List

from app.models.recipe import Recipe
from app.schemas.recipe import RecipeCreate

def get_user_recipes(db: Session, *, user_id: int) -> List[Recipe]:
    return db.query(Recipe).filter(Recipe.owner_id == user_id).all()

def get_recipe(db: Session, *, recipe_id: int, user_id: int) -> Recipe:
    return db.query(Recipe).filter(Recipe.id == recipe_id, Recipe.owner_id == user_id).first()

def create_user_recipe(db: Session, *, recipe_in: RecipeCreate, user_id: int) -> Recipe:
    db_recipe = Recipe(**recipe_in.model_dump(), owner_id=user_id)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def delete_user_recipe(db: Session, *, recipe_id: int, user_id: int) -> Recipe:
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id, Recipe.owner_id == user_id).first()
    if db_recipe:
        db.delete(db_recipe)
        db.commit()
    return db_recipe
