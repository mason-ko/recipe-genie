from sqlalchemy.orm import Session

from app.crud import crud_user
from app.schemas.user import UserCreate, UserUpdate
from tests.utils import random_email, random_lower_string

def test_create_user(db_session: Session):
    email = random_email()
    full_name = random_lower_string()
    user_in = UserCreate(email=email, full_name=full_name)
    user = crud_user.create_user(db_session, user_in=user_in)
    assert user.email == email
    assert user.full_name == full_name

def test_get_user(db_session: Session):
    email = random_email()
    full_name = random_lower_string()
    user_in = UserCreate(email=email, full_name=full_name)
    user = crud_user.create_user(db_session, user_in=user_in)
    user2 = crud_user.get_user(db_session, user_id=user.id)
    assert user2
    assert user.email == user2.email
    assert user.full_name == user2.full_name

def test_get_user_by_email(db_session: Session):
    email = random_email()
    full_name = random_lower_string()
    user_in = UserCreate(email=email, full_name=full_name)
    user = crud_user.create_user(db_session, user_in=user_in)
    user2 = crud_user.get_user_by_email(db_session, email=user.email)
    assert user2
    assert user.email == user2.email
    assert user.full_name == user2.full_name

def test_update_user(db_session: Session):
    email = random_email()
    full_name = random_lower_string()
    user_in = UserCreate(email=email, full_name=full_name)
    user = crud_user.create_user(db_session, user_in=user_in)
    new_full_name = random_lower_string()
    user_in_update = UserUpdate(full_name=new_full_name)
    crud_user.update_user(db_session, db_obj=user, obj_in=user_in_update)
    user2 = crud_user.get_user(db_session, user_id=user.id)
    assert user2
    assert user.email == user2.email
    assert user.full_name == new_full_name
