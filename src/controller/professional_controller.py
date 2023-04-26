from models import db

class ProfessionalController():

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
            usuario = cursor.fetchone() # lastrowid, fetchone, fetchall
            return usuario 
        except:
            return None
        
    def find(self, id):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM professional WHERE id=%s"
            cursor.execute(sql, (id,))
            funcionario = cursor.fetchone()
            return funcionario
        except:
            return 0
        
    def get_professional(self, email):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM professional WHERE email=%s"
            cursor.execute(sql, (email,))
            funcionario = cursor.fetchone()
            return funcionario
        except:
            return 0