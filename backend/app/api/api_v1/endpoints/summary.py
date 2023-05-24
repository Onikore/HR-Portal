from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.summary import Summary, SummaryCreate

router = APIRouter()


@router.get('/', response_model=Summary)
def read_summary(current_user: User = Depends(deps.get_current_user),
                 db: Session = Depends(deps.get_db)) -> Any:
    summ_id = crud.summary.get_resume_id(db, user_id=current_user.id)
    if not summ_id:
        raise HTTPException(status_code=404, detail="User doesn't have summary")
    summary = crud.summary.get(db, id=summ_id)
    return summary


@router.put('/', response_model=Summary)
def update_summary(obj_in: SummaryCreate,
                   current_user: User = Depends(deps.get_current_user),
                   db: Session = Depends(deps.get_db)) -> Any:
    summ_id = crud.summary.get_resume_id(db, user_id=current_user.id)
    if not summ_id:
        raise HTTPException(status_code=404, detail="User doesn't have summary")
    summary = crud.summary.get(db, id=summ_id)

    return crud.summary.update(db, db_obj=summary, obj_in=obj_in)


@router.post('/', response_model=Summary)
def create_summary(obj_in: SummaryCreate,
                   db: Session = Depends(deps.get_db),
                   current_user: User = Depends(deps.get_current_user)) -> Any:
    obj_in.user_id = current_user.id
    return crud.summary.create(db, obj_in=obj_in)
