from models import db
from repository.professional_repository_interface import IProfessionalRepository

class ProfessionalRepository(IProfessionalRepository):

    def __init__(self):
        self.con = db

    def create(self, professional):
        try:
            sql = "INSERT INTO professional(provides_home_service, specialty, council_registration, twitter, insta, linkedin, bio, active, name, email, password, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (professional.provides_home_service, professional.specialty, professional.council_registration, professional.twitter, professional.insta, professional.linkedin, professional.bio, 1, professional.name, professional.email, professional.password, professional.phone_number,))
            self.con.commit()
            return 1
        except:
            return 0
        
    def authenticate(self, email, password):
        try:
            sql = "SELECT * FROM professional WHERE email=%s AND password=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (email, password))
            return 1
        except:
            return 0
        
    def find_by_email(self, email):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM professional WHERE email=%s"
            cursor.execute(sql, (email,))
            professional = cursor.fetchone()
            return professional
        except:
            return 0
        
    def find_by_id(self, id):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM professional WHERE id=%s"
            cursor.execute(sql, (id,))
            professional = cursor.fetchone()
            return professional
        except:
            return 0
        
    def get_professional(self, email):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM professional WHERE email=%s"
            cursor.execute(sql, (email,))
            professional = cursor.fetchone()
            return professional
        except:
            return 0
        
    def list(self, id=None):
        try:
            cursor = self.con.cursor()
            if id != None:
                sql = "SELECT * FROM professional WHERE id=%s"
                cursor.execute(sql, (id,))
                professional = cursor.fetchone()
                return professional
            else:
                sql = "SELECT * FROM professional"
                cursor.execute(sql)
                professionals = cursor.fetchall()
                return professionals
        except:
            return None
        
    def create_address(self, address):
        try:
            sql = "INSERT INTO professional_address(professional_id, state, city, street, complement) VALUES (%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (address.professional_id, address.state, address.city, address.street, address.complement,))
            self.con.commit()
            return 1
        except:
            return 0
        
    def get_address_by_id(self, id):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM professional_address WHERE professional_id=%s"
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
        
    def find_address_by_id(self, id):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM professional_address WHERE id=%s"
            cursor.execute(sql, (id,))
            address = cursor.fetchone()
            return address
        except:
            return 0
        
    def find_plan_by_id(self, id):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM health_plan_professional WHERE id=%s"
            cursor.execute(sql, (id,))
            plan = cursor.fetchone()
            return plan
        except:
            return 0
        
    def disable(self, id):
        try:
            sql = "UPDATE professional SET active=0 WHERE id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0