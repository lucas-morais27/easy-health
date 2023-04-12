from flask import render_template, redirect, url_for
from app import app

class ClientProfileService:
        
    @app.route('/client-profile')
    def render_client_profile():
        return render_template('client-profile.html')
    
    