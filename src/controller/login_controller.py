from flask import Blueprint, redirect, render_template, request, session, url_for

from controller.client_controller import ClientController
from controller.professional_controller import ProfessionalController

login_bp = Blueprint('login', __name__)

class LoginController:

	login_bp.auth = {
		# acao: { perfil:permissao }
		'log-out': {0:1, 1:1},
		'client-profile': {0:1, 1:1},
		'professional-profile': {0:1, 1:1},
		'home-client': {0:1, 1:1},
		'home-professional': {0:1, 1:1},
		'list-professional': {0:1, 1:1},
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
		msg = ''
		if request.method == "POST":
			email = request.form['email']
			password = request.form['password']
			
			client_controller = ClientController().authenticate(email=email, password=password)
			professional_controller = ProfessionalController().authenticate(email=email, password=password)

			if client_controller is not None and client_controller[2] == 1:
				if password == client_controller[5]:
					
					session['logado'] = {
						'id': client_controller[1],
						'nome': client_controller[3],
						'tipo': 'client'
					}
					
					return redirect('home-client')
			elif professional_controller is not None and professional_controller[8] == 1:
				if password == professional_controller[11]:

					session['logado'] = {
						'id': professional_controller[7],
						'nome': professional_controller[9],
						'tipo': 'professional'
					}

					return redirect('home-professional')
			else:
				msg = "Erro ao fazer login. Email ou senha inválida/errada."


		return render_template('log-in.html', msg=msg)
	
