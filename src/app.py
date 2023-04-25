from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

from services.client_service import client_bp
app.register_blueprint(client_bp)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)