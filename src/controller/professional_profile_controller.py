from flask import Blueprint, redirect, render_template, request
from controller.professional_controller import ProfessionalController

professional_profile_bp = Blueprint('professional_profile', __name__)

class ClientProfileController:
        
    @professional_profile_bp.route('/professional-profile-<id>', methods=['GET', 'POST'])
    def professional_profile(id):
        professional = ProfessionalController().find(id)

        if request.method == "POST":
            disable = request.form['disable']
            if disable:
                professional_disable = ProfessionalController().disable(id)
                if professional_disable:
                    return redirect('index')
                
        return render_template('professional-profile.html', professional=professional, nome=professional[9], id=id)
    
    