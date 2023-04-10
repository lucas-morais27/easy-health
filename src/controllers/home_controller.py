from flask_restful import Resource
from services.home_service import HomeService

home_service = HomeService()

class HomeController(Resource):
    
    def get(self):
        return home_service.render_home()