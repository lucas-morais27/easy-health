from marshmallow import validates, ValidationError
from models.professional_model import ProfessionalModel
from schemas.subspecialty_serializer import SubspecialtySerializer
from schemas.professional_address_serializer import ProfessionalAddressSerializer
from schemas.health_plan_serializer import HealthPlanSerializer
from schemas import ma


class ProfessionalSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProfessionalModel
        include_relationships = True
        include_fk = True
        load_instance = True
    password = ma.Str(load_only=True)
    subspecialties = ma.Pluck(SubspecialtySerializer, 'name',many=True)
    addresses = ma.Nested(ProfessionalAddressSerializer, many=True)
    accepted_health_plans = ma.Pluck(HealthPlanSerializer, 'name', many=True)

    @validates('specialty')
    def is_valid_specialty(self, specialty):
        valid_specialties = {
            'medicina', 'nutricao', 'veterinaria',
            'fisioterapia', 'psicologia', 'terapia_ocupacional',
            'educacao_fisica', 'odontologia', 'enfermagem', 
            'farmacia', 'biomedicina'
        }
        if specialty not in valid_specialties:
            raise ValidationError('Not a valid specialty')
