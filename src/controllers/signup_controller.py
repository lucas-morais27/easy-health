from flask import redirect, url_for
from flask_restful import Resource
from services.signup_service import SignupService
from services.client_service import ClientService
from services.professional_service import ProfessionalService
from requests import get, post

client = ClientService()
prof = ProfessionalService()
signup = SignupService()

class SignupController(Resource):
    
    def get(self):
        return signup.render_signup()
    
    def post(self):
        signup.authentication()
        return 'A'
