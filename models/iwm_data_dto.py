from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class IWMDataDTO(BaseModel):
    parent_entity_uuid: UUID
    location_type: str
    component_type: int
    time_period: str
    event_value_type: int
    sub_time_period: int
    entity_uuid: UUID
    data1: str
    data2: Optional[str] = None
