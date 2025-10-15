from fastapi import APIRouter

from app.api import auth, users, ingredients, recipes

api_router = APIRouter()
api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(ingredients.router, prefix="/ingredients", tags=["ingredients"])
api_router.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
