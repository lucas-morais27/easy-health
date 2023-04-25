from models import db

class AddressClientController():

    def create(self, client_id, state, city, street, complement):
        try:
            sql = "INSERT INTO address_client(client_id, state, city, street, complement) VALUES (%s, %s, %s, %s, %s)"
            cursor = db.cursor()
            cursor.execute(sql, (client_id, state, city, street, complement))
            db.commit()
            return True
        except:
            return False
