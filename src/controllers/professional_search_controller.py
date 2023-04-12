from flask_restful import Resource
from controllers.professional_controller import ProfessionalController
from services.professional_search_service import ProfessionalSearchService


professional_search_service = ProfessionalSearchService()

class ProfessionalSearchController(Resource):
    
    def get(self):
        return professional_search_service.render_professional_search()