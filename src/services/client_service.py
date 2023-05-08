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
            return 'Ok'
        else:
            return 'Senha incorreta'


    def find_by_id(self, id):
        if ClientRepository().find_by_id(id):
            return 'Encontrado'
        else:
            return 'Não encontrado'
    
    def disable():
        return 0