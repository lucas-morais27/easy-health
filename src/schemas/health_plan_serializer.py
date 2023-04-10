from schemas import ma
from models.health_plan_model import HealthPlanModel


class HealthPlanSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HealthPlanModel
        include_relationships = True
        include_fk = True
        load_instance = True