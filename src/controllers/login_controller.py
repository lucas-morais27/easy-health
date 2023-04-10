from flask import render_template
from flask_restful import Resource
from services.login_service import LoginService

login_service = LoginService()

class LoginController(Resource):

    def get(self):
        return login_service.authentication
        
    def post(self):
        return

