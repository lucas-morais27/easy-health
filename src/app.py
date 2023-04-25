from flask import Flask, redirect, request, session, url_for

app = Flask(__name__, template_folder='templates')
app.secret_key = "123"

# from services.client_service import client_bp
# app.register_blueprint(client_bp)
from controller.login_controller import login_bp
app.register_blueprint(login_bp)
from controller.home_controller import home_bp
app.register_blueprint(home_bp)
from controller.signup_controller import signup_bp
app.register_blueprint(signup_bp)
from controller.index_controller import index_bp
app.register_blueprint(index_bp)
from controller.client_profile_controller import client_profile_bp
app.register_blueprint(client_profile_bp)
            
if __name__=='__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)