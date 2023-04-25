from models import db

class ClientController():

    def __init__(self):
        self.con = db

    def create(self, client):
        try:
            sql = "INSERT INTO client(health_plan, active, name, email, password, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (client.health_plan, 1, client.name, client.email, client.password, client.phone_number,))
            self.con.commit()
            return 1
        except:
            return 0