class AppointmentModel():
    def __init__(self, client_id, professional_id, dateTime, status):
        self.client_id = client_id,
        self.professional_id = professional_id,
        self.dateTime = dateTime,
        self.status = status
        self.description

    def get_id(self):
        return self.id