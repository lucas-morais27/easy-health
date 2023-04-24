from flask_restful import Resource
from services.client_service import ClientService

client_service = ClientService()

class ClientController(Resource):

    def get(self):
        
        return 

    def post(self):
        
        return 

    def put(self):
        pass

    def delete(self, id):
        pass
