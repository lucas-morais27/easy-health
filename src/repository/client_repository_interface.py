from abc import ABC, abstractmethod

class IClientRepository(ABC):
    @abstractmethod
    def create(self, client):
        pass
    
    @abstractmethod
    def authenticate(self, email, password):
        pass
    
    @abstractmethod
    def find_by_id(self, id):
        pass
    
    @abstractmethod
    def find_by_email(self, email):
        pass
    
    @abstractmethod
    def disable(self, id):
        pass
    
    @abstractmethod
    def get_client(self, email):
        pass
    
    @abstractmethod
    def create_address(self, address):
        pass
    
    @abstractmethod
    def find_address_by_client_id(self, id):
        pass
    
    @abstractmethod
    def create_plan(self, plan):
        pass

    @abstractmethod
    def delete(self, id):
        pass
