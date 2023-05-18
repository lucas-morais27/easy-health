from abc import ABC, abstractmethod

class IAppointmentRepository(ABC):
    @abstractmethod
    def create(self, appointment):
        pass
    
    @abstractmethod
    def find_by_id(self, id):
        pass
    
    @abstractmethod
    def find_by_client_and_date(self, client_id, date):
        pass
    
    @abstractmethod
    def find_by_professional_and_date(self, professional_id, date):
        pass
    
    @abstractmethod
    def appoint(self, id, client_id):
        pass
    
    @abstractmethod
    def cancel(self, id):
        pass

    @abstractmethod
    def default(self, id):
        pass
    
    @abstractmethod
    def conclude(self, id):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass
    
    @abstractmethod
    def list_by_professional(self, professional_id):
        pass
    
    @abstractmethod
    def list_avalible_by_professional(self, professional_id):
        pass
    
    @abstractmethod
    def list_by_client(self, client_id):
        pass
