from models import db

class AddressProfessionalController():

    def create(self, professional_id, state, city, street, complement):
        try:
            sql = "INSERT INTO address_professional(professional_id, state, city, street, complement) VALUES (%s, %s, %s, %s, %s)"
            cursor = db.cursor()
            cursor.execute(sql, (professional_id, state, city, street, complement))
            db.commit()
            return True
        except:
            return False
