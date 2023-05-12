from repository.client_repository import ClientRepository
from repository.professional_repository import ProfessionalRepository

class ProfessionalService():

    def create(self, client_model):
        if ProfessionalRepository().find_by_email(email=client_model.email) or ClientRepository().find_by_email(email=client_model.email):
            return 'Já existe um usuário com esse email'
        if ProfessionalRepository().create(client_model):
            return 'Usuário criado'
        return 'Não foi possível criar'
    
    def authenticate(self, email, password):
        if not ProfessionalRepository().find_by_email(email=email):
            return 'Email inexistente'
        if not ProfessionalRepository().get_professional(email=email)[9]:
            return 'Usuário desativo'
        elif ProfessionalRepository().authenticate(email=email, password=password):
            return 'ok'
        else:
            return 'Senha incorreta'
    
    def find_by_id(self,id):
        try:
            professional = ProfessionalRepository().find_by_id(id=id)
        except NameError as err:
            raise err
            
        return professional
    
    def get_by_email(self,email):
        try:
            professional = ProfessionalRepository().find_by_email(email=email)
        except NameError as err:
            raise err
            
        return professional
    
    def disable():
        return 0
    
    def list(self,id=None):
        try:
            professionals = ProfessionalRepository().list()
        except NameError as err:
            raise err
        return professionals