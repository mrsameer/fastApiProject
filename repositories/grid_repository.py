from sqlalchemy.orm import Session
from models.grid import Grid


def fetch_grid_by_coordinates(db: Session, latitude: float, longitude: float):
    query = db.query(Grid).filter(Grid.grid_latitude == latitude, Grid.grid_longitude == longitude)
    result = query.first()
    return result
