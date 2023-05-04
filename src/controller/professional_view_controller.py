from flask import Blueprint, redirect, render_template, request, session
from controller.professional_controller import ProfessionalController

professional_view_bp = Blueprint('professional_view', __name__)

class ClientViewController:
        
    @professional_view_bp.route('/professional-view', methods=['GET', 'POST'])
    def professional_view(id):
        professional = ProfessionalController().find(id)
                
        return render_template('professional-view.html', professional=professional, nome=professional[9], id=id)
    
    