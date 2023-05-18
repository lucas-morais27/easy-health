from flask import Blueprint, redirect, render_template, request, session
from services.appointment_service import AppointmentService
from models.appointment_model import AppointmentModel
from services.client_service import ClientService
from services.professional_service import ProfessionalService

client_service = ClientService()
professional_service = ProfessionalService()
client_bp = Blueprint('client', __name__)

appointmentService = AppointmentService()

class ClientController():

	@client_bp.route('/client-profile', methods=['GET','POST'])
	def client_profile():

		id = session['logado']['id']
		client = client_service.find_by_id(id)
		if request.method == "POST":
			disable = request.form['disable']
			if disable:
				client_disable = client_service.disable(id)
				if client_disable:
					return redirect('index')
				
		return render_template('client-profile.html', client=client, nome=client[3], id=id)
	
	@client_bp.route('/list-professional')
	def list():
		lists = professional_service.list()
		id = session['logado']['id']
		address = []
		for prof in lists:
			auxiliar = professional_service.get_address_by_id(id=id)
			address.append(auxiliar)
		return render_template('list-professional.html', lists=lists, id=id, address=address)
	
	@client_bp.route('/professional-view/<id>', methods=['GET', 'POST'])
	def professional_view(id):
		msg = ''
		professional = professional_service.find_by_id(id)
		client_id = session['logado']['id']
		if request.method == "POST":
			disable = request.form['disable']
			bio = request.form['bio']
			datetime = request.form['time']
			if disable:
				appointment = {
					'datetime': datetime,
					'client_id': client_id,
					'professional_id': professional[7],
					'description': bio
				}

				msg = appointmentService.create(appointment=appointment)
				if msg == 'agendamento criado':
					return redirect('../home-client')
				
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
				'phone_number': int(phone_number),
				'state': state,
				'city': city,
				'street': street,
				'complement': complement,
				'health_plan': health_plan
				}
			
			msg = client_service.create(client)
			if msg == 'Usuário criado':
				return redirect('/log-in')
		return render_template("sign-up-client.html", msg=msg)
	
	@client_bp.route('/client/appointment-<id>', methods=['GET', 'POST'])
	def view_appointment(id):
		msg = ''
		appointment = appointmentService.find_by_id(id=id)
		professional = professional_service.find_by_id(appointment.professional_id)
		client = client_service.find_by_id(appointment.client_id)

		if appointment == None:
			msg = "Horário de consulta não existe"
		return render_template("appointments-detail-client.html", msg=msg, appointment=appointment, professional=professional, client=client)

	@client_bp.route('/client/appointments')
	def list_appointments():
		id = session['logado']['id']
		tipo = session['logado']['tipo']
		appointments = appointmentService.list_by_client(id)
		return render_template('appointments-view-client.html', list=appointments, id=id, tipo=tipo)