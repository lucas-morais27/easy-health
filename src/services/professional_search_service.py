from flask import render_template, redirect, url_for
from app import app

#sem uso
class ProfessionalSearchService:
        
    @app.route('/professional-search')
    def render_professional_search():
        return render_template('professional-search.html')
    
    