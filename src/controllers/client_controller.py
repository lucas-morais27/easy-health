from flask import Blueprint, redirect, render_template, request, session
from services.client_service import ClientService
from services.professional_service import ProfessionalService

clientService = ClientService()
professionalService = ProfessionalService()

client_bp = Blueprint('client', __name__)

class ClientController():

    @client_bp.route('/client-profile', methods=['GET','POST'])
    def client_profile():

        id = session['logado']['id']
        client = clientService.find_by_id(id)
        

        if request.method == "POST":
            disable = request.form['disable']
            if disable:
                client_disable = clientService.disable(id)
                if client_disable:
                    return redirect('index')
                
        return render_template('client-profile.html', client=client, nome=client[3], id=id)
    
    @client_bp.route('/list-professional')
    def list():
        lists = professionalService.list()
        id = session['logado']['id']
        return render_template('list-professional.html', lists=lists, id=id)
    
    @client_bp.route('/professional-view/<id>', methods=['GET', 'POST'])
    def professional_view(id):
        professional = professionalService.find_by_id(id)
        return render_template('professional-view.html', professional=professional, nome=professional[9], id=id)
    
    