from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService


class UserResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass
    
    @classmethod
    def get_data_resource_info(self):
        pass

    @classmethod
    def get_users_info(cls):
        res = RDBService.get_users_profile("users", "Students")
        return res
