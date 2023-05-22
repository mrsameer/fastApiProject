from geoalchemy2 import WKTElement
from sqlalchemy import func
from sqlalchemy.orm import Session
from models.grid import Grid


def fetch_grid_by_coordinates(db: Session, latitude: float, longitude: float):
    query = db.query(Grid).filter(Grid.grid_latitude == latitude, Grid.grid_longitude == longitude)
    result = query.first()
    return result


def get_intersecting_grids(db: Session, polygon: str, grid_type: str):
    wkt_element = WKTElement(polygon, srid=4326)
    return db.query(Grid).filter(func.ST_Intersects(Grid.geom, wkt_element), Grid.grid_type == grid_type).all()
