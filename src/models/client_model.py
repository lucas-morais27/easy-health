import copy
from models import address_client_model, healthplan_model

class ClientModel():
    def __init__(self, health_plan, name, email, password, phone_number, address):
        self.health_plan = health_plan,
        self.name = name,
        self.email = email,
        self.password = password,
        self.phone_number = phone_number,
        self.address = copy.copy(address)

    def get_id(self):
        return self.id
