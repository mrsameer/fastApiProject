from sqlalchemy.orm import Session
from repositories.grid_repository import fetch_grid_by_coordinates, get_intersecting_grids
from shapely.wkt import loads as wkt_loads


def get_grid_by_coordinates(db: Session, latitude: float, longitude: float):
    result = fetch_grid_by_coordinates(db, latitude, longitude)
    return result


def get_intersecting_grid_external_ids(db: Session, polygon, grid_type):

    # Query the grids that intersect with the given polygon
    intersecting_grids = get_intersecting_grids(db, polygon, grid_type)

    # Extract the external IDs of the intersecting grids
    external_ids = [grid.external_id for grid in intersecting_grids]

    return external_ids
