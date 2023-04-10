from flask_restful import Resource, request
from services.client_service import ClientService


client_service = ClientService()


class ClientController(Resource):

    def get(self, id=None):
        if id:
            return client_service.get_client(id)
        return client_service.get_all_clients()

    def post(self):
        client = client_service.create_client(request.json)
        return client, 201
        

    def put(self):
        pass

    def delete(self, id):
        pass
