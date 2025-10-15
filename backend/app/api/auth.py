from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from httpx_oauth.clients.google import GoogleOAuth2

from app.core.config import settings
from app.crud import crud_user
from app.schemas.user import UserCreate
from app.api import deps

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
    profile = await google_client.get_profile(token["access_token"])
    
    email = None
    if "emailAddresses" in profile and profile["emailAddresses"]:
        email = profile["emailAddresses"][0].get("value")

    if not email:
        return {"error": "Email not found in Google profile"}

    user = crud_user.get_user_by_email(db, email=email)
    if not user:
        full_name = None
        if "names" in profile and profile["names"]:
            full_name = profile["names"][0].get("displayName")
        
        user_in = UserCreate(email=email, full_name=full_name or email)
        user = crud_user.create_user(db, user_in=user_in)
        
    request.session["user_id"] = user.id
    return {"message": "Login successful"}
