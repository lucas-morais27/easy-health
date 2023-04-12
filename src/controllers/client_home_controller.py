from flask_restful import Resource
from services.client_home_service import ClientHomeService


client_home_service = ClientHomeService()

class ClientHomeController(Resource):
    
    def get(self):
        return client_home_service.render_client_home()