from sqlalchemy.orm import Session

from app.crud import crud_recipe, crud_user
from app.schemas.recipe import RecipeCreate
from app.schemas.user import UserCreate
from tests.utils import random_email, random_lower_string

def create_test_user(db_session: Session):
    email = random_email()
    full_name = random_lower_string()
    user_in = UserCreate(email=email, full_name=full_name)
    return crud_user.create_user(db_session, user_in=user_in)

def test_create_recipe(db_session: Session):
    user = create_test_user(db_session)
    recipe_title = random_lower_string()
    recipe_in = RecipeCreate(title=recipe_title)
    recipe = crud_recipe.create_user_recipe(
        db_session, recipe_in=recipe_in, user_id=user.id
    )
    assert recipe.title == recipe_title
    assert recipe.owner_id == user.id

def test_get_recipes(db_session: Session):
    user = create_test_user(db_session)
    recipe_title1 = random_lower_string()
    recipe_in1 = RecipeCreate(title=recipe_title1)
    crud_recipe.create_user_recipe(db_session, recipe_in=recipe_in1, user_id=user.id)
    recipe_title2 = random_lower_string()
    recipe_in2 = RecipeCreate(title=recipe_title2)
    crud_recipe.create_user_recipe(db_session, recipe_in=recipe_in2, user_id=user.id)

    recipes = crud_recipe.get_user_recipes(db_session, user_id=user.id)
    assert len(recipes) == 2

def test_delete_recipe(db_session: Session):
    user = create_test_user(db_session)
    recipe_title = random_lower_string()
    recipe_in = RecipeCreate(title=recipe_title)
    recipe = crud_recipe.create_user_recipe(
        db_session, recipe_in=recipe_in, user_id=user.id
    )
    
    crud_recipe.delete_user_recipe(
        db_session, recipe_id=recipe.id, user_id=user.id
    )
    
    recipes = crud_recipe.get_user_recipes(db_session, user_id=user.id)
    assert len(recipes) == 0
