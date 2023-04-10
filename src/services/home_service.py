from flask import render_template, redirect, url_for
from app import app

class HomeService:
        
    @app.route('/home')
    def render_home():
        return render_template('home.html')
    
    