from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.vacancy import Vacancy, VacancyCreate

router = APIRouter()


@router.get('/', response_model=List[Vacancy])
def read_vacancy(skip: int = 0,
                 limit: int = 5,
                 db: Session = Depends(deps.get_db)) -> Any:
    return crud.vacancy.get_multi(db, skip=skip, limit=limit)


@router.post('/', response_model=Vacancy)
def create_vacancy(obj_in: VacancyCreate,
                   db: Session = Depends(deps.get_db),
                   current_user: User = Depends(deps.get_current_user)) -> Any:
    check = crud.department.is_allowed(db, obj_in=current_user)
    if not check:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return crud.vacancy.create(db, obj_in=obj_in)
