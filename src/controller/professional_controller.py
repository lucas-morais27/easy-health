from models import db

class ProfessionalController():

    def __init__(self):
        self.con = db

    def create(self, professional):
        try:
            sql = "INSERT INTO professional(home_service, specialty, council_registration, twitter, insta, linkedin, bio, active, name, email, password, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (professional.home_service, professional.specialty, professional.council_registration, professional.twitter, professional.insta, professional.linkedin, professional.bio, 1, professional.name, professional.email, professional.password, professional.phone_number,))
            self.con.commit()
            return 1
        except:
            return 0