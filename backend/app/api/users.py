from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.schemas.user import User, UserUpdate
from app.crud import crud_user

router = APIRouter()

@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(deps.get_current_user)):
    """
    Get current user.
    """
    return current_user

@router.put("/me", response_model=User)
async def update_user_me(
    *, 
    db: Session = Depends(deps.get_db), 
    user_in: UserUpdate, 
    current_user: User = Depends(deps.get_current_user)
):
    """
    Update own user.
    """
    user = crud_user.update_user(db, db_obj=current_user, obj_in=user_in)
    return user
