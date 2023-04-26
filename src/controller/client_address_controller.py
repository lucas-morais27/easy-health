from models import db

class ClientAddressController():

    def __init__(self):
        self.con = db

    def create(self, address):
        try:
            sql = "INSERT INTO client_address(client_id, state, city, street, complement) VALUES (%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (address.client_id, address.state, address.city, address.street, address.complement,))
            self.con.commit()
            return 1
        except:
            return 0