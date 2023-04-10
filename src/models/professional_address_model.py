from models import db
from models.address_model import AddressModel


class ProfessionalAddressModel(AddressModel):
    __tablename__ = 'professional_address'

    professional_id = db.Column(db.Integer, db.ForeignKey('professional.id'), nullable=False)

