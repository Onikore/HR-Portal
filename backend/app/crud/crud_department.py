from sqlalchemy.orm import Session

from app import crud
from app.crud.base import CRUDBase
from app.models.department import Department
from app.models.user import User
from app.schemas.department import DepartmentCreate, DepartmentUpdate, DepartmentCreateByEmail


class CRUDDepartment(CRUDBase[Department, DepartmentCreate, DepartmentUpdate]):
    def is_allowed(self, db, *, obj_in: User) -> bool:
        is_superuser = crud.user.is_superuser(obj_in)
        is_head = db.query(Department).filter(Department.user_id == obj_in.id)
        if not is_superuser and not is_head:
            return False
        else:
            return True

    def create_by_email(self, db: Session, *, obj_in: DepartmentCreateByEmail):
        user = crud.user.get_by_email(db,email=obj_in.email)
        if not user:
            return None
        db_obj = Department(name=obj_in.name, user_id=user.id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


department = CRUDDepartment(Department)
