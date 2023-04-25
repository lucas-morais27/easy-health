class ClientModel():
    def __init__(self, health_plan, name, email, password, phone_number):
        self.health_plan = health_plan,
        self.active = True,
        self.name = name,
        self.email = email,
        self.password = password,
        self.phone_number = phone_number

    def get_id(self):
        return self.id
