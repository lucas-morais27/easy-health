from flask import Flask, redirect, request, session, url_for

app = Flask(__name__, template_folder='templates')
app.secret_key = "123"

from services.client_service import client_bp
app.register_blueprint(client_bp)
from services.login_service import login_bp
app.register_blueprint(login_bp)
from services.home_service import home_bp
app.register_blueprint(home_bp)
from services.signup_service import signup_bp
app.register_blueprint(signup_bp)
from services.index_service import index_bp
app.register_blueprint(index_bp)
from services.client_profile_service import client_profile_bp
app.register_blueprint(client_profile_bp)
            
if __name__=='__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)