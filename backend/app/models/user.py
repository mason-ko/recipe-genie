from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    dietary_preferences = Column(String, nullable=True)
    allergies = Column(String, nullable=True)

    ingredients = relationship("Ingredient", back_populates="owner")
    recipes = relationship("Recipe", back_populates="owner")
