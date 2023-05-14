from pydantic import BaseModel

from app.schemas.user import UserProfile


class DepartmentBase(BaseModel):
    name: str = None
    user_id: UserProfile = None


class DepartmentCreate(DepartmentBase):
    name: str
    user_id: int


class DepartmentCreateByEmail(BaseModel):
    name: str
    email: str


class DepartmentUpdate(DepartmentBase):
    name: str
    user_id: int


class Department(DepartmentBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
