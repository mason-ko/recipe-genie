from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.models.user import User
from app.models.ingredient import Ingredient
from app.models.recipe import Recipe

from fastapi.middleware.cors import CORSMiddleware

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
origins = [
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

from app.api.api import api_router

app.include_router(api_router, prefix=settings.API_V1_STR)

if settings.TESTING:
    from fastapi import Request

    @app.get("/test-login/{user_id}")
    def test_login(request: Request, user_id: int):
        request.session["user_id"] = user_id
        return {"message": "Test login successful"}