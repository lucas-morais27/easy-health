from models import db
from models.appointment_model import AppointmentModel
from repository.appointment_repository_interface import IAppointmentRepository

class AppointmentRepository(IAppointmentRepository):

    def __init__(self):
        self.con = db
    
    #cria um appointment com referencia ao proficional, status aberto e sem client
    def create(self, appointment):
        try:
            sql = "INSERT INTO appointment(client_id, professional_id, dateTime, status, description) VALUES (%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (appointment.client_id, appointment.professional_id, appointment.dateTime, appointment.status, appointment.description,))
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
            appointment = AppointmentModel(id=result[0], client_id=result[1], professional_id=result[2],
                                            dateTime=result[3], status=result[4], description=result[5])
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
    
    def default(self, id):
        try:
            sql = "UPDATE appointment SET status=1 WHERE id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0
        
    #define um client apara um appointment ja existente
    def appoint(self, id, client_id):
        try:
            sql = "UPDATE appointment SET status=2 WHERE id=%s and client_id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id, client_id,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0
        
    def conclude(self, id):
        try:
            sql = "UPDATE appointment SET status=3 WHERE id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0
        
    def cancel(self, id):
        try:
            sql = "UPDATE appointment SET status=0 WHERE id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0
        
    def delete(self,id):
        try:
            sql = "DELETE FROM appointment WHERE id=%s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0
    
    def list_by_professional(self,professional_id):
        try:
            cursor = self.con.cursor()
            sql = f"SELECT id, client_id, professional_id, DATE_FORMAT(dateTime,'%d/%m/%Y - %H:%i'), status, description FROM appointment WHERE professional_id={professional_id} ORDER BY dateTime asc"
            cursor.execute(sql)
            results = cursor.fetchall()
            appointments = []
            for result in results:
                appointment = AppointmentModel(id=result[0], client_id=result[1],professional_id=result[2],
                                           dateTime=result[3],status=result[4], description=result[5])
                appointments.append(appointment)
            return appointments
        except:
            return None
        
    def list_avalible_by_professional(self,professional_id):
        try:
            cursor = self.con.cursor()
            sql = f"SELECT id, client_id, professional_id, DATE_FORMAT(dateTime,'%d/%m/%Y - %H:%i'), status FROM appointment WHERE professional_id={professional_id} ORDER BY dateTime asc"
            cursor.execute(sql)
            results = cursor.fetchall()
            appointments = []
            for result in results:
                appointment = AppointmentModel(id=result[0],client_id=result[1],professional_id=result[2],
                                           dateTime=result[3],status=result[4])
                appointments.append(appointment)
            return appointments
        except:
            return None


    def list_by_client(self, client_id):
        try:
            cursor = self.con.cursor()
            sql = f"SELECT id, client_id, professional_id, DATE_FORMAT(dateTime,'%d/%m/%Y - %H:%i'), status, description FROM appointment WHERE client_id={client_id} AND status!='aberto' ORDER BY dateTime asc"
            cursor.execute(sql)
            results = cursor.fetchall()
            appointments = []
            for result in results:
                appointment = AppointmentModel(id=result[0], client_id=result[1],professional_id=result[2],
                                           dateTime=result[3],status=result[4], description=result[5])
                appointments.append(appointment)
            return appointments
        except NameError as err:
            raise err