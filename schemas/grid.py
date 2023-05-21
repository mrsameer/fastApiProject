from geoalchemy2.elements import WKBElement
from pydantic import BaseModel


class GridBase(BaseModel):
    grid_latitude: float
    grid_longitude: float
    geom: WKBElement


class GridCreate(GridBase):
    grid_type: str
    external_id: str


class Grid(GridBase):
    grid_id: float
    grid_uuid: str
    insert_ts: float
    update_ts: float
    deleted: float
