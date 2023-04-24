from flask import render_template, session
from app import app, get_db

class IndexService:

    @app.route('/')
    @app.route('/index')
    def render_index():
        return render_template('index.html')
    

    @app.route('/index')
    def index():
        dao = PontoDAO(get_db())
        ponto = dao.quantidade(session['logado']['id'])[0]
        nome = session['logado']['nome']
        func_id = session['logado']['id']
        tipo = session['logado']['tipo']
        return render_template("index.html", ponto = ponto, nome=nome, tipo=tipo, func_id=func_id)