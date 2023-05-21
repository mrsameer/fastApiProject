from typing import List
from uuid import UUID

from fastapi import APIRouter

from models.iwm_data_dto import IWMDataDTO
from repositories.iwm_data_repository import IWMDataRepository
from services.iwm_data_service import IWMDataService

router = APIRouter()
repository = IWMDataRepository()
service = IWMDataService(repository)


@router.get("/iwm_data/{parent_entity_uuid}", response_model=List[IWMDataDTO])
async def get_iwm_data(parent_entity_uuid: UUID):
    return service.get_iwm_data(parent_entity_uuid)
