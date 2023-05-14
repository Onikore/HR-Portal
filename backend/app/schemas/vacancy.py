from pydantic import BaseModel

from app.schemas.department import Department


class VacancyBase(BaseModel):
    department_id: Department = None
    name: str = None
    experience: str = None
    city: str = None
    address: str = None
    min_salary: float = None
    max_salary: float = None
    description: str = None


class VacancyCreate(VacancyBase):
    department_id: int


class VacancyUpdate(VacancyBase):
    department_id: int


class Vacancy(VacancyBase):
    id: int
    department_id: int

    class Config:
        orm_mode = True
