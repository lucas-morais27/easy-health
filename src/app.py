from flask import Flask

app = Flask(__name__, template_folder='templates')
app.secret_key = "123"

from controllers.client_controller import client_bp
app.register_blueprint(client_bp)
from controllers.index_controller import index_bp
app.register_blueprint(index_bp)
from controllers.professional_controller import professional_bp
app.register_blueprint(professional_bp)
            
if __name__=='__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)