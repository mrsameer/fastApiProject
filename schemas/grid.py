from pydantic import BaseModel


class GridBase(BaseModel):
    grid_latitude: float
    grid_longitude: float


class GridCreate(GridBase):
    grid_type: str
    external_id: str


class Grid(GridBase):
    grid_id: float
    grid_uuid: str
    insert_ts: float
    update_ts: float
    deleted: float

    class Config:
        orm_mode = True
