from flask import Blueprint, redirect, render_template, request, session
from services.signup_service import SignupService

signup = SignupService()

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
	
	@professional_bp.route('/sign-up/professional', methods=['GET', 'POST'])
	def create_professional():
		msg = signup.create_professional(request)
		return render_template("sign-up-professional.html", msg=msg)