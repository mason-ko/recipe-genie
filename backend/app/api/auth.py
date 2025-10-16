from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from httpx_oauth.clients.google import GoogleOAuth2

from app.core.config import settings
from app.crud import crud_user
from app.schemas.user import UserCreate
from app.api import deps

from app.core.security import create_access_token

from jose import jwt

router = APIRouter()

google_client = GoogleOAuth2(
    settings.GOOGLE_CLIENT_ID,
    settings.GOOGLE_CLIENT_SECRET,
)

@router.get("/auth/login")
async def login():
    redirect_uri = settings.GOOGLE_REDIRECT_URI
    url = await google_client.get_authorization_url(
        redirect_uri, scope=["openid", "email", "profile"]
    )
    return RedirectResponse(url)

@router.get("/auth/callback")
async def auth_callback(
    request: Request, code: str, db: Session = Depends(deps.get_db)
):
    token = await google_client.get_access_token(code, settings.GOOGLE_REDIRECT_URI)
    id_token = token["id_token"]
    
    # In a production environment, you should verify the token signature.
    # For this example, we decode it without verification.
    claims = jwt.decode(
        id_token, 
        key=None, 
        options={"verify_signature": False, "verify_at_hash": False},
        audience=settings.GOOGLE_CLIENT_ID
    )
    
    email = claims.get("email")
    if not email:
        return {"error": "Email not found in Google profile"}

    user = crud_user.get_user_by_email(db, email=email)
    if not user:
        full_name = claims.get("name")
        user_in = UserCreate(email=email, full_name=full_name or email)
        user = crud_user.create_user(db, user_in=user_in)
        
    access_token = create_access_token(subject=user.id)
    response = RedirectResponse(url="http://localhost:3001")
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        max_age=1800,  # 30 minutes
        expires=1800,  # 30 minutes
    )
    return response

@router.post("/auth/logout")
async def logout(response: RedirectResponse):
    response.delete_cookie(key="access_token")
    return response
