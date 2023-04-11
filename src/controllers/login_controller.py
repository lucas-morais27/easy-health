from flask import url_for, redirect
from flask_restful import Resource
from services.login_service import LoginService

login_service = LoginService()

class LoginController(Resource):
    
    def get(self):
        return login_service.render_login()
        
    def post(self):
        if login_service.authentication:
            return redirect(url_for('home'))

