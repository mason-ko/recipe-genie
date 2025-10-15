from sqlalchemy.orm import Session

from app.crud import crud_ingredient, crud_user
from app.schemas.ingredient import IngredientCreate
from app.schemas.user import UserCreate
from tests.utils import random_email, random_lower_string

def create_test_user(db_session: Session):
    email = random_email()
    full_name = random_lower_string()
    user_in = UserCreate(email=email, full_name=full_name)
    return crud_user.create_user(db_session, user_in=user_in)

def test_create_ingredient(db_session: Session):
    user = create_test_user(db_session)
    ingredient_name = random_lower_string()
    ingredient_in = IngredientCreate(name=ingredient_name)
    ingredient = crud_ingredient.create_user_ingredient(
        db_session, ingredient_in=ingredient_in, user_id=user.id
    )
    assert ingredient.name == ingredient_name
    assert ingredient.owner_id == user.id

def test_get_ingredients(db_session: Session):
    user = create_test_user(db_session)
    ingredient_name1 = random_lower_string()
    ingredient_in1 = IngredientCreate(name=ingredient_name1)
    crud_ingredient.create_user_ingredient(
        db_session, ingredient_in=ingredient_in1, user_id=user.id
    )
    ingredient_name2 = random_lower_string()
    ingredient_in2 = IngredientCreate(name=ingredient_name2)
    crud_ingredient.create_user_ingredient(
        db_session, ingredient_in=ingredient_in2, user_id=user.id
    )

    ingredients = crud_ingredient.get_user_ingredients(db_session, user_id=user.id)
    assert len(ingredients) == 2

def test_delete_ingredient(db_session: Session):
    user = create_test_user(db_session)
    ingredient_name = random_lower_string()
    ingredient_in = IngredientCreate(name=ingredient_name)
    ingredient = crud_ingredient.create_user_ingredient(
        db_session, ingredient_in=ingredient_in, user_id=user.id
    )
    
    crud_ingredient.delete_user_ingredient(
        db_session, ingredient_id=ingredient.id, user_id=user.id
    )
    
    ingredients = crud_ingredient.get_user_ingredients(db_session, user_id=user.id)
    assert len(ingredients) == 0
