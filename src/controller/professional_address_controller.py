from models import db

class ProfessionalAddressController():

    def __init__(self):
        self.con = db

    def create(self, address):
        try:
            sql = "INSERT INTO professional_address(professional_id, state, city, street, complement) VALUES (%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (address.professional_id, address.state, address.city, address.street, address.complement,))
            self.con.commit()
            return 1
        except:
            return 0