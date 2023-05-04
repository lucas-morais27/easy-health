from flask import Blueprint, redirect, render_template, request, url_for
from services.signup_service import SignupService
service = SignupService()
signup_bp = Blueprint('signup', __name__)
class SignUpController:
    

    @signup_bp.route('/sign-up', methods=['GET', 'POST'])
    def singup():
        if request.method == "POST":
            user = request.form['user']
            if user == 'client':
                return redirect('sign-up/client')
            elif user == 'professional':
                return redirect('sign-up/professional')
        return render_template('sign-up.html')

    @signup_bp.route('/sign-up/client', methods=['GET', 'POST'])
    def create_client():
        msg = service.create_client(request)
        return render_template("sign-up-client.html", msg=msg)
    
    @signup_bp.route('/sign-up/professional', methods=['GET', 'POST'])
    def create_professional():
        msg = service.create_professional(request)
        return render_template("sign-up-professional.html", msg=msg)