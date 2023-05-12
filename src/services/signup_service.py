from flask import request, session
from models.address_client_model import AddressClientModel
from models.client_model import ClientModel
from models.healthplan_model import HealthPlanModel
from models.professional_model import ProfessionalModel
from repository.client_repository import ClientRepository
from repository.professional_repository import ProfessionalRepository
from services.client_service import ClientService
from services.professional_service import ProfessionalService

class SignupService:
	
	def create_client(self, client):
		if client is not None:
			client_model = ClientModel(health_plan=client['health_plan'], name=client['name'], email=client['email'], password=client['password'], phone_number=int(client['phone_number']), address='')
			msg = ClientService().create(client_model)

		if msg == 'Usuário criado':
			client_aux = ClientService().find_by_email(client['email'])
			address_model = AddressClientModel(client_id=client_aux[1], state=client['state'], city=client['city'], street=client['street'], complement=client['complement'])
			address = ClientService().create_address(address=address_model)

			if address == 'Endereço criado':
				msg = 'Usuário criado'

		return msg
	
	def create_professional(self):
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

			professional_model = ProfessionalModel(provides_home_service=home_service, specialty=specialty, council_registration=int(registration), twitter=twitter, insta=insta, linkedin=linkedin, bio=bio, name=name, email=email, password=password, phone_number=int(phone_number))

			msg = ProfessionalService().create(professional_model)
				
			#address_model = AddressProfessionalModel(professional_id=id, state=state, city=city, street=street, complement=complement)
		return msg
		

	# def authenticate_user(self, email, password):
	# 	client_service = ClientService().authenticate(email=email, password=password)
	# 	professional_service = ProfessionalService().authenticate(email=email, password=password)

	# 	if not client_service == 'Email inexistente':
	# 		if client_service == 'Ok':
	# 			client = ClientRepository().find_by_email(email=email)
	# 			return client
	# 		else:
	# 			return client_service
	# 	elif not professional_service == 'Email inexistente':
	# 		if professional_service == 'Ok':
	# 			professional = ProfessionalRepository().find_by_email(email=email)
	# 			return professional
	# 		else:
	# 			return professional_service
	# 	else:
	# 		return 'Usuário não cadastrado'
