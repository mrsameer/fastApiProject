from fastapi import APIRouter, Depends
from geoalchemy2.shape import to_shape
from shapely.geometry import mapping
from sqlalchemy.orm import Session

from database import get_db
from services.grid_service import get_grid_by_coordinates, get_intersecting_grid_external_ids

router = APIRouter()


@router.get("/grid")
async def get_grid(latitude: float, longitude: float, db: Session = Depends(get_db)):
    grid = get_grid_by_coordinates(db, latitude, longitude)

    # Convert the geometry to a GeoJSON-like dictionary representation
    geometry = to_shape(grid.geom)
    geojson = mapping(geometry)
    grid.geom = geojson

    return grid


@router.post("/grid/intersecting")
async def get_intersecting_grids(request: dict, db: Session = Depends(get_db)):
    external_ids = get_intersecting_grid_external_ids(db, request["polygon"])
    return external_ids
