from flask import redirect, url_for
from flask_restful import Resource
from services.signup_service import SignupService
from services.client_service import ClientService

clint = ClientService()

signup = SignupService()

class SignupController(Resource):
    
    def get(self):
        pass
    
    def post(self):
        if signup.register:
            redirect(url_for('client-home'))
       
