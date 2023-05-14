from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.tags import TagCreate, Tag

router = APIRouter()


@router.get('/{id}', response_model=Tag)
def get_tag(id: int,
            db: Session = Depends(deps.get_db)):
    tag = crud.tags.get(db, id=id)
    if not tag:
        raise HTTPException(status_code=400, detail="Tag doesn't exists")
    return tag


@router.get('/', response_model=List[Tag])
def get_tags_list(db: Session = Depends(deps.get_db)):
    return crud.tags.get_all(db)


@router.post('/', response_model=Tag)
def create_tag(obj_in: TagCreate,
               db: Session = Depends(deps.get_db),
               current_user: User = Depends(deps.get_current_user)):
    user = crud.user.is_superuser(user=current_user)
    if not user:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return crud.tags.create(db, obj_in=obj_in)
