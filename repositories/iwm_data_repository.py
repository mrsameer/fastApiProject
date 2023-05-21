from cassandra.cluster import Cluster
from typing import List
from uuid import UUID

from models.iwm_data_dto import IWMDataDTO


class IWMDataRepository:
    def __init__(self):
        self.cluster = Cluster(['localhost'])  # Replace with your Cassandra cluster address
        self.session = self.cluster.connect('cass_business_data_od')  # Replace with your keyspace name

    def get_iwm_data(self, parent_entity_uuid: UUID) -> List[IWMDataDTO]:
        query = "SELECT * FROM iwm_data WHERE parent_entity_uuid = %s LIMIT 1 ALLOW FILTERING"
        result_set = self.session.execute(query, [parent_entity_uuid])
        return [IWMDataDTO(**row._asdict()) for row in result_set]
