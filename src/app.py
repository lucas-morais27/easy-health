from flask import Flask, redirect, request, session

app = Flask(__name__, template_folder='templates')
app.secret_key = "123"

from controller.login_controller import login_bp
app.register_blueprint(login_bp)
from controller.home_controller import home_client_bp, home_professional_bp
app.register_blueprint(home_client_bp)
app.register_blueprint(home_professional_bp)
from controller.signup_controller import signup_bp
app.register_blueprint(signup_bp)
from controller.index_controller import index_bp
app.register_blueprint(index_bp)
from controller.client_profile_controller import client_profile_bp
app.register_blueprint(client_profile_bp)
from controller.professional_profile_controller import professional_profile_bp
app.register_blueprint(professional_profile_bp)
from controller.list_professional_controller import list_professional_bp
app.register_blueprint(list_professional_bp)
from services.logout_service import logout_bp
app.register_blueprint(logout_bp)
            
if __name__=='__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)