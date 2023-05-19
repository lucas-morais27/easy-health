from models import db
import MySQLdb
from repository.client_repository_interface import IClientRepository

class ClientRepository(IClientRepository):

    def __init__(self):
        self.con = db

    def create(self, client):
        sql = "INSERT INTO client(health_plan, active, name, email, password, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor = self.con.cursor()
        cursor.execute(sql, (client.health_plan, 1, client.name, client.email, client.password, client.phone_number,))
        self.con.commit()
        
    def authenticate(self, email, password):
        try:
            sql = "SELECT * FROM client WHERE email=%s AND password=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (email, password))
            #usuario = cursor.fetchone() # lastrowid, fetchone, fetchall
            if cursor.fetchone() != None:
                return True
            return False
        except:
            return False
        
    def find_by_id(self, id):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM client WHERE id=%s"
            cursor.execute(sql, (id,))
            client = cursor.fetchone()
            return client
        except:
            Exception("Erro no banco de dados")
        
    def find_by_email(self, email):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM client WHERE email=%s"
            cursor.execute(sql, (email,))
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
        
    def get_client(self, email):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM client WHERE email=%s"
            cursor.execute(sql, (email,))
            funcionario = cursor.fetchone()
            return funcionario
        except:
            return 0
        

    def create_address(self, address):
            sql = "INSERT INTO client_address(client_id, state, city, street, complement) VALUES (%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (address.client_id, address.state, address.city, address.street, address.complement,))
            self.con.commit()
        
        
    def find_address_by_client_id(self, id):
        try:
            sql = "SELECT * FROM client_adress WHERE client_id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id,))
            address = cursor.fetchone()
            return address
        except:
            return 0
    
        
    def create_plan(self, plan):
        try:
            sql = "INSERT INTO health_plan(name) VALUES (%s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (plan.name,))
            self.con.commit()
            return 1
        except:
            return 0
        
    def delete(self, id):
        try:
            sql = "DELETE FROM client WHERE id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id,))
            self.con.commit()
        except:
            raise Exception("Erro no banco de dados")
