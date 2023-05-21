from typing import List
from uuid import UUID

from models.iwm_data_dto import IWMDataDTO
from repositories.iwm_data_repository import IWMDataRepository


class IWMDataService:
    def __init__(self, repository: IWMDataRepository):
        self.repository = repository

    def get_iwm_data(self, parent_entity_uuid: UUID) -> List[IWMDataDTO]:
        return self.repository.get_iwm_data(parent_entity_uuid)
