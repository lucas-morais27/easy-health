from models.client_model import ClientModel
from models.healthplan_model import HealthPlanModel
from models.professional_model import ProfessionalModel
from models.address_client_model import AddressClientModel
from models.address_professional_model import AddressProfessionalModel

from controller.client_controller import ClientController
from services.healthplan_service import HealthPlanService
from controller.professional_controller import ProfessionalController
from controller.client_address_controller import ClientAddressController
from controller.professional_address_controller import ProfessionalAddressController

class SignupService:
    
    def create_client(self, request):
        msg = ''
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            phone_number = request.form['phone_number']
            state = request.form['state']
            city = request.form['city']
            street = request.form['street']
            complement = request.form['complement']
            health_plan = request.form['health_plan']

            health_plan_model = HealthPlanModel(name=health_plan)
            health_plan_service = HealthPlanService().create(health_plan_model)

            if health_plan_service > 0:

                client_model = ClientModel(health_plan=health_plan_model.name, name=name, email=email, password=password, phone_number=int(phone_number))
                client_controller = ClientController().create(client_model)

                if client_controller > 0:

                    client = ClientController().get_client(client_model.email)
                    
                    id = client[1]

                    address_model = AddressClientModel(client_id=id, state=state, city=city, street=street, complement=complement)
                    address_controller = ClientAddressController().create(address_model)

                    if address_controller > 0:
                        msg = ("Cadastrado com sucesso!")
                    else:
                        msg = ("Erro ao cadastrar!")
        return msg
        
    
    
    def create_professional(self, request):
        msg = ''
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            phone_number = request.form['phone_number']
            home_service = request.form['home_service']
            specialty = request.form['specialty']
            registration = request.form['registration']
            twitter = request.form['twitter']
            insta = request.form['insta']
            linkedin = request.form['linkedin']
            bio = request.form['bio']
            state = request.form['state']
            city = request.form['city']
            street = request.form['street']
            complement = request.form['complement']

            if home_service == 'S':
                home_service = 1
            else:
                home_service = 0

            professional_model = ProfessionalModel(provides_home_service=home_service, specialty=specialty, council_registration=int(registration), twitter=twitter, insta=insta, linkedin=linkedin, bio=bio, name=name, email=email, password=password, phone_number=int(phone_number))
            
            professional_controller = ProfessionalController().create(professional_model)

            if professional_controller > 0:

                professional = ProfessionalController().get_professional(professional_model.email)
                
                id = professional[7]

                address_model = AddressProfessionalModel(professional_id=id, state=state, city=city, street=street, complement=complement)
                address_controller = ProfessionalAddressController().create(address_model)

                if address_controller > 0:
                    msg = ("Cadastrado com sucesso!")
                else:
                    msg = ("Erro ao cadastrar!")
        return msg
        
