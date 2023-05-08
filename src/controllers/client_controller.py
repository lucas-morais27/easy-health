from flask import Blueprint, redirect, render_template, request, session
from services.client_service import ClientService
from services.professional_service import ProfessionalService

client = ClientService()
professional = ProfessionalService()

client_bp = Blueprint('client', __name__)

class ClientController():

    @client_bp.route('/client-profile', methods=['GET','POST'])
    def client_profile():

        id = session['logado']['id']
        client.find_by_id(id)
        disable = request.form['disable']
        if disable:
            client_disable = client.disable(id)
            if client_disable:
                return redirect('index')
                
        return render_template('client-profile.html', client=client, nome=client[3], id=id)
    
    @client_bp.route('/list-professional')
    def list():
        lists = professional.list()
        id = session['logado']['id']
        return render_template('list-professional.html', lists=lists, id=id)
    
    @client_bp.route('/professional-view', methods=['GET', 'POST'])
    def professional_view(id):
        professional = ProfessionalService().find(id)
        return render_template('professional-view.html', professional=professional, nome=professional[9], id=id)
    
    