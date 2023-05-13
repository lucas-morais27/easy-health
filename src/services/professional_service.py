from models.address_professional_model import AddressProfessionalModel
from models.professional_model import ProfessionalModel
from repository.client_repository import ClientRepository
from repository.professional_repository import ProfessionalRepository

class ProfessionalService():

	def create(self, professional):
		
		professional_model = ProfessionalModel(
			provides_home_service=int(professional['home_service']),
			specialty=professional['specialty'],
			council_registration=int(professional['registration']),
			twitter=professional['twitter'],
			insta=professional['insta'], 
			linkedin=professional['linkedin'], 
			bio=professional['bio'], 
			name=professional['name'], 
			email=professional['email'], 
			password=professional['password'], 
			phone_number=int(professional['phone_number'])
			)
		
		if ProfessionalRepository().find_by_email(email=professional_model.email) or ClientRepository().find_by_email(email=professional_model.email):
			return 'Já existe um usuário com esse email'
		
		if ProfessionalRepository().create(professional_model):
			professional_aux = ProfessionalService().find_by_email(professional['email'])

		if not professional_aux:
			return 'Erro ao criar profissional'
			
		address_model = AddressProfessionalModel(professional_id=professional_aux[7], state=professional['state'], city=professional['city'], street=professional['street'], complement=professional['complement'])
		address = ProfessionalService().create_address(address=address_model)

		if not address:
			return 'Endereço não criado'
		
		return 'Usuário criado'
	
	def authenticate(self, email, password):
		if not ProfessionalRepository().find_by_email(email=email):
			return 'Email inexistente'
		if not ProfessionalRepository().get_professional(email=email)[9]:
			return 'Usuário desativo'
		elif ProfessionalRepository().authenticate(email=email, password=password):
			return 'ok'
		else:
			return 'Senha incorreta'
	
	def find_by_email(self, email):
		try:
			professional = ProfessionalRepository().find_by_email(email=email)
		except NameError as err:
			raise err
		return professional
	
	def find_by_id(self,id):
		try:
			professional = ProfessionalRepository().find_by_id(id=id)
		except NameError as err:
			raise err
		return professional
	
	def create_address(self, address):
		try:
			address_aux = ProfessionalRepository().create_address(address=address)
		except NameError as err:
			raise err
		
		return 'Endereço criado'
	
	def disable(self, id):
		try:
			ProfessionalRepository().disable(id)
		except NameError as err:
			raise err
		
		return 'disable'
	
	def list(self,id=None):
		try:
			professionals = ProfessionalRepository().list()
		except NameError as err:
			raise err
		return professionals