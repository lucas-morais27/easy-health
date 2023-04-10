from models import db
from models.address_model import AddressModel


class ClientAddressModel(AddressModel):
    __tablename__ = 'client_address'

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False, unique=True)
