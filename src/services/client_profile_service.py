from flask import Blueprint, redirect, render_template, request
from controller.client_controller import ClientController

client_profile_bp = Blueprint('client_profile', __name__)

class ClientProfileService:
        
    @client_profile_bp.route('/client-profile-<id>', methods=['GET', 'POST'])
    def client_profile(id):
        client = ClientController().find(id)

        if request.method == "POST":
            disable = request.form['disable']
            if disable:
                client_disable = ClientController().disable(id)
                if client_disable:
                    return redirect('index')
                
        return render_template('client-profile.html', client=client, nome=client[3], id=id)
    
    