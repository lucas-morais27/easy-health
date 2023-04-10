from models.client_model import ClientModel
from schemas import ma
from schemas.client_address_serializer import ClientAddressSerializer


class ClientSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ClientModel
        include_relationships = True
        include_fk = True
        load_instance = True

    password = ma.Str(load_only=True)
    address = ma.Nested(ClientAddressSerializer)
