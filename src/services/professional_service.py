from models import db
from models.professional_model import ProfessionalModel
from schemas.professional_serializer import ProfessionalSerializer

professional_serializer = ProfessionalSerializer()
professionals_serializer = ProfessionalSerializer(many=True)


class ProfessionalService:

    def create_professional(self, obj):
        professional = professional_serializer.load(obj)
        db.session.add(professional)
        db.session.commit()
        return professional_serializer.dump(professional)

    def get_professional(self, id):
        query = ProfessionalModel.query.get(id)
        return professional_serializer.dump(query)

    def get_all_professionals(self):
        query = ProfessionalModel.query.all()
        return professionals_serializer.dump(query)
