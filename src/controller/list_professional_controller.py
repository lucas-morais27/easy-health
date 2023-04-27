from flask import Blueprint, render_template, session
from controller.professional_controller import ProfessionalController

list_professional_bp = Blueprint('list_professional', __name__)

class ListProfessionalService:
        
    @list_professional_bp.route('/list-professional')
    def list():
        lists = ProfessionalController().list()
        id = session['logado']['id']
        return render_template('list-professional.html', lists=lists, id=id)
    
    