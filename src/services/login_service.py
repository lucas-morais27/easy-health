from flask import request, redirect, url_for
from models.client_model import ClientModel
from models.professional_model import ProfessionalModel
from app import app


class LoginService:

    @app.route('/log-in', methods=['GET', 'POST'])
    def authentication():
    
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']

            client = ClientModel.query.filter_by(email=email).first()
            profissional = ProfessionalModel.query.filter_by(email=email).first()

            if client:
                if password == client.password:
                    return redirect(url_for())
            elif profissional:
                if password == profissional.password:
                    return redirect(url_for())
            else:
                return {'message': 'Erro ao fazer login'}, 401