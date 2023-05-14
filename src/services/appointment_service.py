from repository.appointment_repository import AppointmentRepository
from models.appointment_model import AppointmentModel
class AppointmentService():
    
    def __init__(self) -> None:
        self.apRep = AppointmentRepository()

    #apenas professional tem acesso
    def create(self, appointment:AppointmentModel)->str:
        msg = ""
        if self.apRep.find_by_professional_and_date(professional_id=appointment.professional_id,
                                                    date=appointment.dateTime):
            msg = "profissional ja possui um horario de consulta com esse mesmo horario e data"
        if self.apRep.create(appointment=appointment):
            msg = "horario de consulta criado"
        msg = "Não foi possivel criar o horario de consulta, erro interno"
        return msg
        
    def find_by_id(self, id):
        return self.apRep.find_by_id(id=id)
            
    
    #apenas client tem acesso
    def appoint(self, id, client_id)->str:
        appointment = self.apRep.find_by_id(id=id)
        if appointment == None:
            return "horario de consulta não existe"
        if self.apRep.find_by_client_and_date(client_id=client_id,date=appointment.dateTime):
             return "você ja possui uma consulta com esse mesmo horario e data"
        if appointment.status == 2:
            return "horario de consulta ja está agendada por outro cliente"
        if appointment.status == 3:
            return "consulta ja concluida"
        if self.apRep.appoint(id=id,client_id=client_id):
            return "consulta agendada com sucesso no horario: %s" % self.apRep.find_by_id(id).dateTime
        return "Não foi possivel agendar o horario de consulta, erro interno"


    #client e professional tem acesso
    def cancel(self, id)->str:
        appointment = self.apRep.find_by_id(id=id)
        if appointment == None:
            return "horario de consulta não existe"
        if appointment.status == 1:
            return "horario de consulta não agendado"
        if appointment.status == 3:
            return "consulta ja concluida"
        if self.apRep.cancel(id=id):
            return "consulta cancelada"
        return "Não foi possivel cancelar a consulta, erro interno"


    #apenas professional tem acesso
    def conclude(self, id):
        appointment = self.apRep.find_by_id(id=id)
        if appointment == None:
            return "horario de consulta não existe"
        if appointment.status == 1:
            return "horario de consulta não agendado"
        if appointment.status == 3:
            return "consulta ja concluida"
        if self.apRep.cancel(id=id):
            return "consulta concluida"
        return "Não foi possivel concluir a consulta, erro interno"

    #apenas professional tem acesso
    def delete(self,id):
        if self.find_by_id(id=id) == 0:
            return "horario de consulta não existe"
        if self.delete(id=id):
            return "harario de consulta excluido"
        return "Não foi possivel excluir o horario de consulta, erro interno"