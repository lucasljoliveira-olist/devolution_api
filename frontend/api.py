from flask import Flask
from flask_restful import Api
from backend.resources.devolution_product_order_resource import DevolutionProductOrderResource
from backend.resources.devolution_reason_resource import DevolutionReasonResource
from backend.resources.devolution_resource import DevolutionResource
from backend.resources.devolution_status_resource import DevolutionStatusResource
from backend.resources.devolution_type_resource import DevolutionTypeResource

app = Flask(__name__)
api = Api(app)

api.add_resource(DevolutionProductOrderResource, '/api/devolution/devolution_product_order/<int:id_>', endpoint='devolution_product_order')
api.add_resource(DevolutionProductOrderResource, '/api/devolution/devolution_product_order', endpoint='devolution_product_orders')

api.add_resource(DevolutionReasonResource, '/api/devolution/devolution_reason/<int:id_>', endpoint='devolution_reason')
api.add_resource(DevolutionReasonResource, '/api/devolution/devolution_reason', endpoint='devolution_reasons')

api.add_resource(DevolutionResource, '/api/devolution/<int:id_>', endpoint='devolution')
api.add_resource(DevolutionResource, '/api/devolution', endpoint='devolutions')

api.add_resource(DevolutionStatusResource, '/api/devolution/devolution_status/<int:id_>', endpoint='devolution_status')
api.add_resource(DevolutionStatusResource, '/api/devolution/devolution_status', endpoint='devolution_statuss')

api.add_resource(DevolutionTypeResource, '/api/devolution/devolution_type/<int:id_>', endpoint='devolution_type')
api.add_resource(DevolutionTypeResource, '/api/devolution/devolution_type', endpoint='devolution_types')
