from flask import Blueprint, render_template, request
from models.client_model import ClientModel
from models.healthplan_model import HealthPlanModel
from controller.client_controller import ClientController
from controller.healthplan_controller import HealthPlanController

#class ClientService:
    
    # @client_bp.route('/sign-up', methods=['GET', 'POST'])
    # def create_client():
    #     msg = ''
    #     if request.method == 'POST':
    #         name = request.form['name']
    #         email = request.form['email']
    #         password = request.form['password']
    #         phone_number = request.form['phone_number']

    #         state = request.form['state']
    #         city = request.form['city']
    #         street = request.form['street']
    #         complement = request.form['complement']

    #         health_plan = request.form['health_plan']

    #         health_plan_model = HealthPlanModel(name=health_plan)

    #         health_plan_controller = HealthPlanController().create(health_plan_model)

    #         if health_plan_controller > 0:

    #             client_model = ClientModel(health_plan=health_plan_model.name, name=name, email=email, password=password, phone_number=int(phone_number))
                
    #             client_controller = ClientController().create(client_model)

    #             if client_controller > 0:
    #                 msg = ("Cadastrado com sucesso!")
    #             else:
    #                 msg = ("Erro ao cadastrar!")

    #     return render_template("sign-up.html", msg=msg)
