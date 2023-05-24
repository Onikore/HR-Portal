from pydantic import BaseModel


class SummaryBase(BaseModel):
    user_id: int = None
    ready_to_move: bool = None
    car_license: bool = None
    only_remote: bool = None
    ready_for_trips: bool = None
    pref_salary: float = None
    pref_position: str = None
    skills: str = None
    pref_city: str = None
    citizenship: str = None
    education: str = None
    busyness: str = None


class SummaryCreate(SummaryBase):
    pass


class SummaryUpdate(SummaryBase):
    id: int


class Summary(SummaryBase):
    id: int

    class Config:
        orm_mode = True
