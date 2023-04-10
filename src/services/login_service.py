from flask import render_template, request, redirect, url_for
from models.client_model import ClientModel
from models.professional_model import ProfessionalModel
from app import app

class LoginService:

    def authentication(self):
        email = request.form['email']
        password = request.form['password']

        client = ClientModel.query.filter_by(email=email).first()
        profissional = ProfessionalModel.query.filter_by(email=email).first()

        if client:
            if password == client.password:
                return True
        elif profissional:
            if password == profissional.password:
                return True
        else:
            return False
        
    @app.route('/log-in')
    def render_login():
        return render_template('log-in.html')
    
