from flask import Blueprint, redirect, render_template, request, session
from services.client_service import ClientService
from services.professional_service import ProfessionalService
from services.signup_service import SignupService

clientService = ClientService()
professionalService = ProfessionalService()
signup = SignupService()

client_bp = Blueprint('client', __name__)

class ClientController():

	@client_bp.route('/client-profile', methods=['GET','POST'])
	def client_profile():

		id = session['logado']['id']
		client = clientService.find_by_id(id)
		if request.method == "POST":
			disable = request.form['disable']
			if disable:
				client_disable = clientService.disable(id)
				if client_disable:
					return redirect('index')
				
		return render_template('client-profile.html', client=client, nome=client[3], id=id)
	
	@client_bp.route('/list-professional')
	def list():
		lists = professionalService.list()
		id = session['logado']['id']
		return render_template('list-professional.html', lists=lists, id=id)
	
	@client_bp.route('/professional-view', methods=['GET', 'POST'])
	def professional_view(id):
		professional = professionalService.find(id)
		return render_template('professional-view.html', professional=professional, nome=professional[9], id=id)
	
	@client_bp.route('/sign-up/client', methods=['GET', 'POST'])
	def create_client():
		msg = ''
		if request.method == 'POST':
			name = request.form['name']
			email = request.form['email']
			password = request.form['password']
			phone_number = request.form['phone_number']
			state = request.form['state']
			city = request.form['city']
			street = request.form['street']
			complement = request.form['complement']
			health_plan = request.form['health_plan']

			client = {
				'name': name,
				'email': email,
				'password': password,
				'phone_number': phone_number,
				'state': state,
				'city': city,
				'street': street,
				'complement': complement,
				'health_plan': health_plan
				}
			
			msg = signup.create_client(client)
		return render_template("sign-up-client.html", msg=msg)
	