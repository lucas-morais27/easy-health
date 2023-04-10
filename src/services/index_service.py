from app import app
from flask import render_template

class IndexService:

    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')
    