from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    dietary_preferences: Optional[str] = None
    allergies: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "email": "user@example.com",
                "full_name": "John Doe",
                "is_active": True,
                "dietary_preferences": "Vegan",
                "allergies": "Peanuts"
            }
        }
    )

# Properties to receive on user creation
class UserCreate(UserBase):
    email: EmailStr

# Properties to receive on user update
class UserUpdate(UserBase):
    pass

# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: int
    email: EmailStr
    full_name: Optional[str]

    model_config = ConfigDict(from_attributes=True)

# Properties to return to client
class User(UserInDBBase):
    pass

# Properties stored in DB
class UserInDB(UserInDBBase):
    pass
