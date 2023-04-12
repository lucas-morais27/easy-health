from flask import render_template, redirect, url_for
from app import app

class ClientHomeService:
        
    @app.route('/client-home')
    def render_client_home():
        return render_template('client-home.html')
    
    