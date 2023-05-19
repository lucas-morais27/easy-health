from flask import Blueprint, redirect, render_template, request, session
from services.professional_service import ProfessionalService
from services.appointment_service import AppointmentService
from services.client_service import ClientService

professional_service = ProfessionalService()
client_service = ClientService()
professional_bp = Blueprint('professional', __name__)
appointmentService = AppointmentService()

class ProfessionalController():

	@professional_bp.route('/professional-profile', methods=['GET', 'POST'])
	def professional_profile():
		id = session['logado']['id']
		professional = ProfessionalService().find_by_id(id)

		if request.method == "POST":
			disable = request.form['disable']
			if disable:
				professional_disable = ProfessionalService().disable(id)
				if professional_disable:
					return redirect('index')
				
		return render_template('professional-profile.html', professional=professional, nome=professional[9], id=id)
	
	@professional_bp.route('/sign-up/professional', methods=['GET', 'POST'])
	def create_professional():
		if request.method == 'GET':
			return render_template("sign-up-professional.html", msg='')
		if request.method == 'POST':
			name = request.form['name']
			email = request.form['email']
			password = request.form['password']
			phone_number = request.form['phone_number']
			home_service = request.form['home_service']
			specialty = request.form['specialty']
			registration = request.form['registration']
			twitter = request.form['twitter']
			insta = request.form['insta']
			linkedin = request.form['linkedin']
			bio = request.form['bio']
			state = request.form['state']
			city = request.form['city']
			street = request.form['street']
			complement = request.form['complement']

			if home_service == 'S':
				home_service = 1
			else:
				home_service = 0

			professional = {
				'name': name,
				'email': email,
				'password': password,
				'phone_number': int(phone_number),
				'home_service': int(home_service),
				'specialty': specialty,
				'registration': int(registration),
				'twitter': twitter,
				'insta': insta,
				'linkedin': linkedin,
				'bio': bio,
				'state': state,
				'city': city,
				'street': street,
				'complement': complement
				}
			
			try:
				professional_service.create(professional)
			except Exception as exception:
				return render_template("sign-up-professional.html", msg=exception)
			return redirect('/log-in')
		
	
	@professional_bp.route('/professional/appointment-<id>', methods=['GET', 'POST'])
	def view_appointment(id):
		msg = ''
		appointment = appointmentService.find_by_id(id=id)
		professional = professional_service.find_by_id(appointment.professional_id)
		client = client_service.find_by_id(appointment.client_id)

		if request.method == 'POST':
			status = request.form['status']
			if status == 'agendado':
				appointmentService.appoint(id=id, client_id=appointment.client_id)
			elif status == 'concluido':
				appointmentService.conclude(id=id)
			elif status == 'cancelado':
				appointmentService.cancel(id=id)
			else:
				appointmentService.default(id=id)

			return redirect('/professional/appointments')

		return render_template("appointments-detail-professional.html", msg=msg, appointment=appointment, professional=professional, client=client)
	
	@professional_bp.route('/professional/appointments')
	def list_appointments():
		id = session['logado']['id']
		tipo = session['logado']['tipo']
		appointments = appointmentService.list_by_professional(id)
		return render_template('appointments-view-professional.html', list=appointments, id=id, tipo=tipo)