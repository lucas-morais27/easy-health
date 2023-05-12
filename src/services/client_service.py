from models.client_model import ClientModel
from repository.client_repository import ClientRepository
from repository.professional_repository import ProfessionalRepository

class ClientService():

    def create(self, client_model):
        if ClientRepository().find_by_email(email=client_model.email) or ProfessionalRepository().find_by_email(email=client_model.email):
            return 'Já existe um usuário com esse email'
        if ClientRepository().create(client_model):
            return 'Usuário criado'
        return 'Não foi possível criar'
    
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
    
    def get_by_email(self,email):
        try:
            client = ClientRepository().get_client(email=email)
        except NameError as err:
            raise err

        return client
    
    def disable():
        return 0