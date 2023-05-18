from abc import ABC, abstractmethod

class IProfessionalRepository(ABC):
    @abstractmethod
    def create(self, professional):
        pass
    
    @abstractmethod
    def authenticate(self, email, password):
        pass
    
    @abstractmethod
    def find_by_email(self, email):
        pass
    
    @abstractmethod
    def find_by_id(self, id):
        pass
    
    @abstractmethod
    def get_professional(self, email):
        pass
    
    @abstractmethod
    def list(self, id=None):
        pass
    
    @abstractmethod
    def create_address(self, address):
        pass

    @abstractmethod
    def get_address_by_id(self, address):
        pass
    
    @abstractmethod
    def create_plan(self, plan):
        pass
    
    @abstractmethod
    def find_address_by_id(self, id):
        pass
    
    @abstractmethod
    def find_plan_by_id(self, id):
        pass
    
    @abstractmethod
    def disable(self, id):
        pass
