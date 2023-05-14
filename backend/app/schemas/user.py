from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr = None
    phone: str = None
    name: str = None
    family_name: str = None
    last_name: str = None
    is_superuser: bool = False


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    pass


class UserProfile(UserBase):
    pass

    class Config:
        orm_mode = True


class User(UserBase):
    id: int = None

    class Config:
        orm_mode = True
