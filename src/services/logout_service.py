from flask import Blueprint, redirect, session

logout_bp = Blueprint('logout', __name__)

class LogOutService():

    @logout_bp.route('/log-out')
    def logout():
        session['logado'] = None
        session.clear()
        return redirect('index')