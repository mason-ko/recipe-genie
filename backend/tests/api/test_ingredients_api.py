from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.schemas.ingredient import IngredientCreate
from app.crud import crud_user
from app.schemas.user import UserCreate
from tests.utils import random_email, random_lower_string

def test_create_ingredient(client: TestClient, db_session: Session):
    email = random_email()
    full_name = random_lower_string()
    user_in = UserCreate(email=email, full_name=full_name)
    user = crud_user.create_user(db_session, user_in=user_in)
    client.get(f"/test-login/{user.id}")

    ingredient_name = "test ingredient"
    data = {"name": ingredient_name}
    response = client.post(f"{settings.API_V1_STR}/ingredients/", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == ingredient_name
    assert "id" in content
    assert "owner_id" in content

def test_read_ingredients(client: TestClient, db_session: Session):
    email = random_email()
    full_name = random_lower_string()
    user_in = UserCreate(email=email, full_name=full_name)
    user = crud_user.create_user(db_session, user_in=user_in)
    client.get(f"/test-login/{user.id}")

    ingredient_name1 = "test ingredient 1"
    data1 = {"name": ingredient_name1}
    client.post(f"{settings.API_V1_STR}/ingredients/", json=data1)

    ingredient_name2 = "test ingredient 2"
    data2 = {"name": ingredient_name2}
    client.post(f"{settings.API_V1_STR}/ingredients/", json=data2)

    response = client.get(f"{settings.API_V1_STR}/ingredients/")
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 2
