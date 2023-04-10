from schemas.client_serializer import ClientSerializer
from models.client_model import ClientModel
from models import db


client_serializer = ClientSerializer()
clients_serializer = ClientSerializer(many=True)

class ClientService:

    def create_client(self, obj):
        client = client_serializer.load(obj)
        db.session.add(client)
        db.session.commit()
        return client_serializer.dump(client)

    def get_client(self, id):
        query = ClientModel.query.get(id)
        return client_serializer.dump(query)

    def get_all_clients(self):
        query = ClientModel.query.all()
        return clients_serializer.dump(query)
