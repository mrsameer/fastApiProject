from fastapi import APIRouter, HTTPException

from database import SessionLocal
from models.grid import Grid

router = APIRouter()


@router.get("/grid")
async def get_grid(latitude: float, longitude: float):
    session = SessionLocal()

    try:
        query = session.query(Grid).filter(Grid.grid_latitude == latitude, Grid.grid_longitude == longitude)
        result = query.first()

        if result is None:
            raise HTTPException(status_code=404, detail="Grid not found")

        return result

    finally:
        session.close()
