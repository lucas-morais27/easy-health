from models import db

class ClientDAO():
    def __init__(self):
        self.con = db

    def create(self, client):
        try:
            sql = "INSERT INTO client(name, email, password, phone_number) VALUES (%s, %s, %s, %s)"
            print("AAAcccccccccccccccccccccccccccccc")

            cursor = self.con.cursor()
            cursor.execute(sql, (client.name, client.email, client.password, client.phone_number,))
            self.con.commit()
            codigo = cursor.lastrowid
            return codigo
        except:
            return 0