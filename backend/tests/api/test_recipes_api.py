from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.schemas.recipe import RecipeCreate
from app.crud import crud_user
from app.schemas.user import UserCreate
from tests.utils import random_email, random_lower_string

def test_create_recipe(client: TestClient, db_session: Session):
    email = random_email()
    full_name = random_lower_string()
    user_in = UserCreate(email=email, full_name=full_name)
    user = crud_user.create_user(db_session, user_in=user_in)
    client.get(f"/test-login/{user.id}")

    recipe_title = "test recipe"
    data = {"title": recipe_title}
    response = client.post(f"{settings.API_V1_STR}/recipes/", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == recipe_title
    assert "id" in content
    assert "owner_id" in content

def test_generate_recipe(client: TestClient, db_session: Session):
    email = random_email()
    full_name = random_lower_string()
    user_in = UserCreate(email=email, full_name=full_name)
    user = crud_user.create_user(db_session, user_in=user_in)
    client.get(f"/test-login/{user.id}")

    data = {"ingredients": ["tomato", "cheese"]}
    response = client.post(f"{settings.API_V1_STR}/recipes/generate", json=data)
    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, str)
