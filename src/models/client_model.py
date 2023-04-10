from models.user_model import UserModel
from models import db


class ClientModel(UserModel):
    __tablename__ = 'client'

    address = db.relationship('ClientAddressModel', backref='client', uselist=False)
    health_plan = db.Column(db.String, nullable=False)
