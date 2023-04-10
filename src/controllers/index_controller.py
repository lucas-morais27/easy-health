from flask_restful import Resource
from services.index_service import IndexService

index_service = IndexService()

class IndexController(Resource):
    
    def get(self):
        return index_service.render_index()