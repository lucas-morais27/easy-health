from flask_restful import Resource
from controllers.professional_controller import ProfessionalController
from services.client_profile_service import ClientProfileService


client_profile_service = ClientProfileService()

class ClientProfileController(Resource):
    
    def get(self):
        return client_profile_service.render_client_profile()