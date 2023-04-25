from flask import Blueprint, render_template, session

home_bp = Blueprint('home', __name__)

class HomeService:
        
    @home_bp.route('/home')
    def home():
        nome = session['logado']['nome']
        id = session['logado']['id']
        return render_template('home.html', nome=nome, id=id)
    
    