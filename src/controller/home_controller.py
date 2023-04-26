from flask import Blueprint, render_template, session

home_client_bp = Blueprint('home_client', __name__)
home_professional_bp = Blueprint('home_professional', __name__)

class HomeController:
        
    @home_client_bp.route('/home-client')
    def home():
        nome = session['logado']['nome']
        id = session['logado']['id']
        return render_template('home-client.html', nome=nome, id=id)
    
    @home_professional_bp.route('/home-professional')
    def home():
        nome = session['logado']['nome']
        id = session['logado']['id']
        return render_template('home-professional.html', nome=nome, id=id)
    
    