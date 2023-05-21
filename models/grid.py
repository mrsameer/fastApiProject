from geoalchemy2 import Geometry
from sqlalchemy import Column, Float, String
from database import Base


class Grid(Base):
    __tablename__ = "grid"

    grid_id = Column(Float, primary_key=True)
    grid_uuid = Column(String(45))
    grid_latitude = Column(Float, nullable=False)
    grid_longitude = Column(Float, nullable=False)
    grid_type = Column(String(45), nullable=False)
    external_id = Column(String(45))
    insert_ts = Column(Float, nullable=False)
    update_ts = Column(Float)
    deleted = Column(Float)
    geom = Column(Geometry('POLYGON', srid=4326))
