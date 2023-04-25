from flask import Blueprint, redirect, render_template, request, session, url_for

from services.client_service import ClientService
from services.professional_service import ProfessionalService

login_bp = Blueprint('login', __name__)

class LoginController:

    login_bp.auth = {
        # acao: { perfil:permissao }
        'index': {0:1, 1:1},
        'home': {0:1, 1:1},
        'login': {0:1, 1:1},
        'signup': {0:1, 1:1},
        'client_profile': {0:1, 1:1},
    }

    @login_bp.before_request
    def authorization():
        acao = request.path[1:]
        acao = acao.split('/')
        if len(acao)>=1:
            acao = acao[0]

        acoes = login_bp.auth.keys()
        if acao in list(acoes):
            if session.get('logado') is None:
                return redirect('login')
            else:
                tipo = session['logado']['tipo']
                if login_bp.auth[acao][tipo] == 0:
                    return redirect('home')

    @login_bp.route('/log-in', methods=['GET', 'POST'])
    def login():
        msg = '#'
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']
            
            client_controller = ClientService().authenticate(email=email, password=password)
            professional_controller = ProfessionalService().authenticate(email=email, password=password)

            if client_controller is not None and client_controller[2] == 1:
                if password == client_controller[5]:
                    
                    session['logado'] = {
                        'id': client_controller[1],
                        'nome': client_controller[3]
                    }
                    
                    return redirect('home')
            elif professional_controller is not None:
                if password == professional_controller[11]:
                    return redirect('home')
            else:
                msg = "Erro ao fazer login. Email ou senha inválida/errada."


        return render_template('log-in.html', msg=msg)
    
