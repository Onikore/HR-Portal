from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.department import Department, DepartmentCreate, DepartmentCreateByEmail

router = APIRouter()


@router.post('/id', response_model=Department)
def create_department_by_id(obj_in: DepartmentCreate,
                            db: Session = Depends(deps.get_db),
                            current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    Create department by user id
    """
    user = crud.user.is_superuser(user=current_user)
    if not user:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return crud.department.create(db, obj_in=obj_in)


@router.post('/email', response_model=Department)
def create_department_by_email(obj_in: DepartmentCreateByEmail,
                               db: Session = Depends(deps.get_db),
                               current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    Create department by user email
    """
    user = crud.user.is_superuser(user=current_user)
    if not user:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return crud.department.create_by_email(db, obj_in=obj_in)
