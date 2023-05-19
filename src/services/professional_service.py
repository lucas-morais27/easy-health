from MySQLdb import DataError
from models.address_professional_model import AddressProfessionalModel
from models.professional_model import ProfessionalModel
from repository.client_repository import ClientRepository
from repository.professional_repository import ProfessionalRepository
import services.serviceExceptions as serviceExceptions

class ProfessionalService():

	def __init__(self) -> None:
		self.profRep = ProfessionalRepository()
		self.clientRep = ClientRepository()

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
		
		if self.profRep.find_by_email(email=professional_model.email) or self.clientRep.find_by_email(email=professional_model.email):
			raise serviceExceptions.EmailIndisponivel
		
		try:
			self.clientRep.create(professional_model)
		except DataError:
			raise serviceExceptions.ErroNoBanco(fonte="dados do profissional")
		
		professional_aux = self.find_by_email(professional['email'])
		address_model = AddressProfessionalModel(professional_id=professional_aux[7], state=professional['state'], city=professional['city'], street=professional['street'], complement=professional['complement'])
		try:	
			self.create_address(address=address_model)
		except DataError:
			self.profRep.delete(id=professional_aux[7])
			raise serviceExceptions.ErroNoBanco(fonte="dados do endereço")

	
	def authenticate(self, email, password):
		if not ProfessionalRepository().find_by_email(email=email):
			raise serviceExceptions.EmailInexistente
		elif not ProfessionalRepository().get_professional(email=email)[9]:
			raise serviceExceptions.UsuarioDesativado
		elif not ProfessionalRepository().authenticate(email=email, password=password):
			raise serviceExceptions.SenhaIncorreta
	
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
		self.profRep.create_address(address=address)
		
	
	def get_address_by_id(self, id):
		try:
			address_aux = ProfessionalRepository().get_address_by_id(id=id)
			address = ""
			address = address_aux[4]+ ", "+ address_aux[5]+ ", "+ address_aux[3]+ " - "+ address_aux[2]  
		except NameError as err:
			raise err
		
		return address
	
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