from models.address_client_model import AddressClientModel
from models.client_model import ClientModel
from repository.client_repository import ClientRepository
from repository.professional_repository import ProfessionalRepository
import services.serviceExceptions as serviceExceptions
from MySQLdb._exceptions import DataError

class ClientService():

	def __init__(self) -> None:
		self.profRep = ProfessionalRepository()
		self.clientRep = ClientRepository()

	def create(self, client):
		client_model = ClientModel(
			health_plan=client['health_plan'], 
			name=client['name'], 
			email=client['email'],
			password=client['password'], 
			phone_number=int(client['phone_number']), 
			address=''
			)
		
		if self.clientRep.find_by_email(email=client_model.email) or self.profRep.find_by_email(email=client_model.email):
			raise serviceExceptions.EmailIndisponivel
		
		try:
			self.clientRep.create(client_model)
		except DataError:
			raise serviceExceptions.ErroNoBanco(fonte="dados de cliente")
		
		client_aux = self.find_by_email(client['email'])
		address_model = AddressClientModel(client_id=client_aux[1], state=client['state'], city=client['city'], street=client['street'], complement=client['complement'])
		
		try:
			self.create_address(address=address_model)
		except  DataError:
			self.clientRep.delete(id=client_aux[1])
			raise serviceExceptions.ErroNoBanco(fonte="dados do endereço")

	
	def authenticate(self, email, password):
		if not self.clientRep.find_by_email(email=email):
			raise serviceExceptions.EmailInexistente
		elif not self.clientRep.get_client(email=email)[2]:
			raise serviceExceptions.UsuarioDesativado
		elif not self.clientRep.authenticate(email=email, password=password):
			raise serviceExceptions.SenhaIncorreta


	def find_by_id(self, id):
		try:
			client = self.clientRep.find_by_id(id)
			
		except NameError as err:
			raise err
		
		return client
	
	def find_by_email(self, email):
		try:
			client = self.clientRep.find_by_email(email)
			
		except NameError as err:
			raise err
		
		return client
	
	def create_address(self, address):
			self.clientRep.create_address(address=address)
		
		#return 'Endereço criado'
	
	def disable(self, id):
		try:
			self.clientRep.disable(id)
		except NameError as err:
			raise err
		
		return 'disable'