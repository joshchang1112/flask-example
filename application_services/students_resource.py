from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService


class StudentsResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    def get_data_resource_info(cls):
        pass

    @classmethod
    def get_by_name_prefix(cls, name_prefix):
        if not name_prefix:
            name_prefix = ''
        res = RDBService.get_by_prefix("users", "Students",
                                      "FirstName", name_prefix)
        return res