from sqlalchemy.orm import Session
from typing import List

from app.models.ingredient import Ingredient
from app.schemas.ingredient import IngredientCreate

def get_user_ingredients(db: Session, *, user_id: int) -> List[Ingredient]:
    return db.query(Ingredient).filter(Ingredient.owner_id == user_id).all()

def create_user_ingredient(db: Session, *, ingredient_in: IngredientCreate, user_id: int) -> Ingredient:
    db_ingredient = Ingredient(**ingredient_in.model_dump(), owner_id=user_id)
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient

def delete_user_ingredient(db: Session, *, ingredient_id: int, user_id: int) -> Ingredient:
    db_ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id, Ingredient.owner_id == user_id).first()
    if db_ingredient:
        db.delete(db_ingredient)
        db.commit()
    return db_ingredient
