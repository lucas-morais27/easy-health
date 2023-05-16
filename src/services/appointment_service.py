import datetime
from repository.appointment_repository import AppointmentRepository
from models.appointment_model import AppointmentModel
from repository.professional_repository import ProfessionalRepository
from repository.client_repository import ClientRepository
class AppointmentService():
    
    def __init__(self) -> None:
        self.apRep = AppointmentRepository()
        self.profRep = ProfessionalRepository()
        self.clintRep = ClientRepository()

    def date_to_str(self,date:datetime.datetime):
        msg = date.strftime('%d/%m/%Y - %H:%M')
        return msg

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
    
    def list_by_professional(self, professional_id):
        if self.profRep.find_by_id(id=professional_id) == 0:
            return "profissional não encontrado"
        return self.apRep.list_by_professional(professional_id=professional_id)
    
    def list_avalible_by_professional(self, professional_id):
        if self.profRep.find_by_id(id=professional_id) == 0:
            return "profissional não encontrado"
        return self.apRep.list_avalible_by_professional(professional_id=professional_id)
        
    
    def list_by_client(self,client_id):
        if self.clintRep.find_by_id(id=client_id) == 0:
            return "cliente não encontrado"
        appointments =  self.apRep.list_by_client(client_id=client_id)
        lista = []
        if appointments != None:
            for i in range(len(appointments)):
                item = [
                    appointments[i].id,
                    self.profRep.find_by_id(appointments[i].professional_id)[9],
                    appointments[i].dateTime,
                    appointments[i].status
                ]
                lista.append(item)
        return lista