from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.grid_service import get_grid_by_coordinates

router = APIRouter()


@router.get("/grid")
async def get_grid(latitude: float, longitude: float, db: Session = Depends(get_db)):
    result = get_grid_by_coordinates(db, latitude, longitude)
    return result
