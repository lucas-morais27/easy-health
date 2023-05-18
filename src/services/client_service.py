from models.address_client_model import AddressClientModel
from models.client_model import ClientModel
from repository.client_repository import ClientRepository
from repository.professional_repository import ProfessionalRepository

class ClientService():

	def create(self, client):
		client_model = ClientModel(
			health_plan=client['health_plan'], 
			name=client['name'], 
			email=client['email'],
			password=client['password'], 
			phone_number=int(client['phone_number']), 
			address=''
			)
		
		if ClientRepository().find_by_email(email=client_model.email) or ProfessionalRepository().find_by_email(email=client_model.email):
			raise Exception('Já existe um usuário com esse email')
		
		try:
			ClientRepository().create(client_model)
		except NameError as err:
			raise "Erro ao criar cliente: " + err
		
		client_aux = ClientService().find_by_email(client['email'])

		try:
			address_model = AddressClientModel(client_id=client_aux[1], state=client['state'], city=client['city'], street=client['street'], complement=client['complement'])
			ClientService().create_address(address=address_model)
		except:
			ClientRepository().delete(id=client_aux[1])
			raise Exception("Erro ao criar endereço: campo(s) com formato diferente do exigido")

	
	def authenticate(self, email, password):
		if not ClientRepository().find_by_email(email=email):
			return 'Email inexistente'
		if not ClientRepository().get_client(email=email)[2]:
			return 'Usuário desativo'
		elif ClientRepository().authenticate(email=email, password=password):
			return 'ok'
		else:
			return 'Senha incorreta'


	def find_by_id(self, id):
		try:
			client = ClientRepository().find_by_id(id)
			
		except NameError as err:
			raise err
		
		return client
	
	def find_by_email(self, email):
		try:
			client = ClientRepository().find_by_email(email)
			
		except NameError as err:
			raise err
		
		return client
	
	def create_address(self, address):
		try:
			ClientRepository().create_address(address=address)
		except NameError as err:
			raise err
		
		#return 'Endereço criado'
	
	def disable(self, id):
		try:
			ClientRepository().disable(id)
		except NameError as err:
			raise err
		
		return 'disable'