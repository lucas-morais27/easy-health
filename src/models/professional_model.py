from models import db
from models.user_model import UserModel
from models.subspecialties_model import subspecilaty_professional
from models.health_plan_model import health_plan_professional


class ProfessionalModel(UserModel):
    __tablename__ = 'professional'

    addresses = db.relationship('ProfessionalAddressModel', backref='professional')
    provides_home_service = db.Column(db.Boolean, nullable=False)
    specialty = db.Column(db.String, nullable=False)
    subspecialties = db.relationship('SubspecialtyModel', secondary=subspecilaty_professional, back_populates='professionals', uselist=True)
    accepted_health_plans = db.relationship('HealthPlanModel', secondary=health_plan_professional, back_populates='professionals', uselist=True)
    council_registration = db.Column(db.Integer, nullable=False)
    twitter = db.Column(db.String)
    insta = db.Column(db.String)
    linkedin = db.Column(db.String)
    bio = db.Column(db.String)
