from flask import Blueprint, redirect, render_template, request, session

professional_bp = Blueprint('professional', __name__)

class ProfessionalController():

    @professional_bp.route('/professional-profile', methods=['GET', 'POST'])
    def professional_profile():
        id = session['logado']['id']
        professional = ProfessionalController().find(id)

        if request.method == "POST":
            disable = request.form['disable']
            if disable:
                professional_disable = ProfessionalController().disable(id)
                if professional_disable:
                    return redirect('index')
                
        return render_template('professional-profile.html', professional=professional, nome=professional[9], id=id)