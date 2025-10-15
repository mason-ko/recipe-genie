from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.schemas.user import UserUpdate
from app.crud import crud_user
from app.schemas.user import UserCreate
from tests.utils import random_email, random_lower_string

def test_get_users_me(client: TestClient, db_session: Session):
    email = random_email()
    full_name = random_lower_string()
    user_in = UserCreate(email=email, full_name=full_name)
    user = crud_user.create_user(db_session, user_in=user_in)

    client.get(f"/test-login/{user.id}")
    response = client.get(f"{settings.API_V1_STR}/users/me")
    assert response.status_code == 200
    assert response.json()["email"] == email

def test_update_user_me(client: TestClient, db_session: Session):
    email = random_email()
    full_name = random_lower_string()
    user_in = UserCreate(email=email, full_name=full_name)
    user = crud_user.create_user(db_session, user_in=user_in)

    client.get(f"/test-login/{user.id}")
    new_name = "Updated Name"
    user_in_update = UserUpdate(full_name=new_name)
    response = client.put(
        f"{settings.API_V1_STR}/users/me", json=user_in_update.model_dump()
    )
    assert response.status_code == 200
    assert response.json()["full_name"] == new_name