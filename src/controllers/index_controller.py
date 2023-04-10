from flask import render_template
from flask_restful import Resource

class IndexController(Resource):

    def get(self):
        return render_template("index.html")

    def post(self):
        return render_template("index.html")