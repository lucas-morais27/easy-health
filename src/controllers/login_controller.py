from flask import url_for, redirect
from flask_restful import Resource
from services.login_service import LoginService
from services.home_service import HomeService

login_service = LoginService()
home_service = HomeService()

class LoginController(Resource):
    
    def get(self):
        return login_service.render_login()
        
    def post(self):
        if login_service.authentication:
            return redirect(url_for('home'))

