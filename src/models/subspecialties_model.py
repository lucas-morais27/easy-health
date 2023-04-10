from models import db


subspecilaty_professional = db.Table(
    'subspecilaty_professional',
    db.Column('subspecialty_id', db.String, db.ForeignKey('subspecialty.name')),
    db.Column('professional_id', db.Integer, db.ForeignKey('professional.id'))
)


class SubspecialtyModel(db.Model):
    __tablename__ = 'subspecialty'

    name = db.Column(db.String, primary_key=True)
    professionals = db.relationship('ProfessionalModel', secondary=subspecilaty_professional, back_populates='subspecialties')
