from flask import Blueprint, redirect, render_template, request, session
from services.client_service import ClientService
from services.professional_service import ProfessionalService
from services.signup_service import SignupService

client = ClientService()
professional = ProfessionalService()
signup = SignupService()

index_bp = Blueprint('index', __name__)

class IndexController:

	@index_bp.route('/')
	@index_bp.route('/index')
	def index():
		return render_template('index.html')
	
	@index_bp.route('/home-client')
	def home_client():
		nome = session['logado']['nome']
		id = session['logado']['id']
		tipo = session['logado']['tipo']
		return render_template('home-client.html', nome=nome, id=id, tipo=tipo)
	
	@index_bp.route('/home-professional')
	def home_professional():
		nome = session['logado']['nome']
		id = session['logado']['id']
		tipo = session['logado']['tipo']
		return render_template('home-professional.html', nome=nome, id=id, tipo=tipo)
	
	index_bp.auth = {
		# acao: { perfil:permissao }
		'log-out': {0:1, 1:1},
		'client-profile': {0:1, 1:1},
		'professional-profile': {0:1, 1:1},
		'home-client': {0:1, 1:1},
		'home-professional': {0:1, 1:1},
		'list-professional': {0:1, 1:1},
	}

	@index_bp.before_request
	def authorization():
		acao = request.path[1:]
		acao = acao.split('/')
		if len(acao)>=1:
			acao = acao[0]
		
		acoes = index_bp.auth.keys()
		if acao in list(acoes):
			if session.get('logado') is None:
				return redirect('login')
			else:
				tipo = session['logado']['tipo']
				print(index_bp.auth[acao][tipo])
				if index_bp.auth[acao][tipo] == 0:
					return redirect('home')
		

	@index_bp.route('/log-in', methods=['GET','POST'])
	def login():
		msg = ''
		if request.method == "POST":
			email = request.form['email']
			password = request.form['password']
			
			client = SignupService().authenticate_user(email=email, password=password)
			if client:
				session['logado'] = {
					'id': client[1],
					'nome': client[3],
					'tipo': 0
				}
				return redirect('home-client')
			
			professional = SignupService().authenticate_user(email=email, password=password)
			if professional:
				session['logado'] = {
					'id': professional[7],
					'nome': professional[9],
					'tipo': 1
				}
				return redirect('home-professional')

		return render_template('log-in.html', msg=msg)
	
	@index_bp.route('/sign-up', methods=['GET', 'POST'])
	def singup():
		if request.method == "POST":
			user = request.form['user']
			if user == 'client':
				return redirect('sign-up/client')
			elif user == 'professional':
				return redirect('sign-up/professional')
		return render_template('sign-up.html')
	
	@index_bp.route('/sign-up/client', methods=['GET', 'POST'])
	def create_client():
		msg = signup.create_client(request)
		return render_template("sign-up-client.html", msg=msg)
	
	@index_bp.route('/sign-up/professional', methods=['GET', 'POST'])
	def create_professional():
		msg = signup.create_professional(request)
		return render_template("sign-up-professional.html", msg=msg)
	
	@index_bp.route('/log-out')
	def logout():
		session['logado'] = None
		session.clear()
		return redirect('index')