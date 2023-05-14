from pydantic import BaseModel


class TagsBase(BaseModel):
    name: str = None


class TagCreate(TagsBase):
    pass


class TagUpdate(TagsBase):
    id: int
    name: str


class Tag(TagsBase):
    id: int = None
    name: str = None

    class Config:
        orm_mode = True
