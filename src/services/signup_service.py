from flask import Blueprint, redirect, render_template, request

from models.client_model import ClientModel
from models.healthplan_model import HealthPlanModel
from models.professional_model import ProfessionalModel

from services.client_service import ClientService
from services.healthplan_service import HealthPlanService
from services.professional_service import ProfessionalService



class SignupService:
    
    def create_client(self, request):
        msg = 'OLa'
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

            health_plan_controller = HealthPlanService().create(health_plan_model)

            if health_plan_controller > 0:

                client_model = ClientModel(health_plan=health_plan_model.name, name=name, email=email, password=password, phone_number=int(phone_number))
                
                client_controller = ClientService().create(client_model)

                if client_controller > 0:
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

            print(home_service)

            professional_model = ProfessionalModel(provides_home_service=home_service, specialty=specialty, council_registration=int(registration), twitter=twitter, insta=insta, linkedin=linkedin, bio=bio, name=name, email=email, password=password, phone_number=int(phone_number))
            
            professional_controller = ProfessionalService().create(professional_model)

            if professional_controller > 0:
                msg = ("Cadastrado com sucesso!")
            else:
                msg = ("Erro ao cadastrar!")
        return msg
        
