from flask import Blueprint, Flask, g, redirect, render_template, request, session, url_for
from models import db

app = Flask(__name__, template_folder='templates')

from services.client_service import client_bp
app.register_blueprint(client_bp)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__=='__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)