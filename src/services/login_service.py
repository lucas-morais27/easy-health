from flask import Blueprint, redirect, render_template, request
from controller.client_controller import ClientController

login_bp = Blueprint('login', __name__)

class LoginService:

    @login_bp.route('/log-in', methods=['GET', 'POST'])
    def login():
        msg = '#'
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']
            
            client_controller = ClientController().authenticate(email=email, password=password)

            if client_controller is not None:
                if password == client_controller[5]:
                    return redirect('home')
            else:
                msg = "Erro ao fazer login. Email ou senha inválida/errada."


        return render_template('log-in.html', msg=msg)
    
