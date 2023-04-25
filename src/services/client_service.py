from models import db


class ClientService():
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
        
    def authenticate(self, email, password):
        try:
            sql = "SELECT * FROM client WHERE email=%s AND password=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (email, password))
            usuario = cursor.fetchone() # lastrowid, fetchone, fetchall
            return usuario 
        except:
            return None
        
    def find(self, id):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM client WHERE id=%s"
            cursor.execute(sql, (id,))
            funcionario = cursor.fetchone()
            return funcionario
        except:
            return 0
        
    def disable(self, id):
        try:
            sql = "UPDATE client SET active=0 WHERE id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0