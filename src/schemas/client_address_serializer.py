from schemas import ma
from models.client_address_model import ClientAddressModel


class ClientAddressSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ClientAddressModel
        include_relationships = True
        load_instance = True
