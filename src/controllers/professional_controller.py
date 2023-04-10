from flask import request
from flask_restful import Resource
from services.professional_service import ProfessionalService


professional_service = ProfessionalService()


class ProfessionalController(Resource):

    def get(self, id=None):
        if id:
            return professional_service.get_professional(id)
        return professional_service.get_all_professionals()

    def post(self):
        professional = professional_service.create_professional(request.json)
        return professional, 201

    def put(self):
        pass

    def delete(self):
        pass
