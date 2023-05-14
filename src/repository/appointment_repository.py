from models import db
from models.appointment_model import AppointmentModel

class AppointmentRepository():

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
        
    def find_by_id(self, id:int):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM appointment WHERE id=%s"
            cursor.execute(sql, (id,))
            result = cursor.fetchone()
            appointment = AppointmentModel(id=result[0],client_id=result[1],professional_id=result[2],
                                           dateTime=result[3],status=result[4])
            return appointment
        except:
            return None
    
    def find_by_client_and_date(self, client_id, date):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM appointment WHERE client_id=%s and dateTime=STR_TO_DATE(%s,'%m-%\d-%Y %H:%\i:%\s')"
            cursor.execute(sql, (client_id,date,))
            appointment = cursor.fetchone()
            return appointment
        except:
            return 0
        
    def find_by_professional_and_date(self, professional_id, date):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM appointment WHERE professional_id=%s and dateTime=STR_TO_DATE(%s,'%m-%\d-%Y %H:%\i:%\s')"
            cursor.execute(sql, (professional_id,date,))
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
        
    def delete(self,id):
        try:
            sql = "DELETE FROM appointment WHERE id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0