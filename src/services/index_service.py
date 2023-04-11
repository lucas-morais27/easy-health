from flask import render_template
from app import app

class IndexService:

    @app.route('/')
    @app.route('/index')
    def render_index():
        return render_template('index.html')
    