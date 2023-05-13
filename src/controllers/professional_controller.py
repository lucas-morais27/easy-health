from flask import Blueprint, redirect, render_template, request, session
from services.professional_service import ProfessionalService

professional_service = ProfessionalService()
professional_bp = Blueprint('professional', __name__)

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
		msg = ''
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
			
			msg = professional_service.create(professional)
		return render_template("sign-up-professional.html", msg=msg)