from sqlalchemy.orm import Session
from repositories.grid_repository import fetch_grid_by_coordinates


def get_grid_by_coordinates(db: Session, latitude: float, longitude: float):
    result = fetch_grid_by_coordinates(db, latitude, longitude)
    return result
