from models import db

class AppointmentService():

    def __init__(self):
        self.con = db
    
    #cria um appointment com referencia ao proficional, status aberto e sem client
    def create(self, appointment):
        try:
            sql = "INSERT INTO appointment(professional_id, dateTime , status) VALUES(%s,STR_TO_DATE(%s,'%m-%\d-%Y %H:%\i:%\s'),'aberto');"
            cursor = self.con.cursor()
            cursor.execute(sql, (appointment.profession_id, appointment.dateTime))
            self.con.commit()
            return 1
        except:
            return 0
        
    def find(self, id):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM appointment WHERE id=%s"
            cursor.execute(sql, (id,))
            appointment = cursor.fetchone()
            return appointment
        except:
            return 0
        
    #define um client apara um appointment ja existente
    def appoint(self, id, client_id):
        try:
            sql = "UPDATE appointment SET status=2, client_id=%s WHERE id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id,client_id))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0
        
    def cancel(self, id):
        try:
            sql = "UPDATE appointment SET status=1, WHERE id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0
        
    def conclude(self, id):
        try:
            sql = "UPDATE appointment SET status=3, WHERE id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0