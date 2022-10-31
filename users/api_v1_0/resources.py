from app.common.error_handling import ObjectNotFound
from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import usersSchema, agentSchema, perfiles
from ..models import agent, UsersPrv, perfiles

users_v1_0_bp = Blueprint('users_v1_0_bp', __name__)

users_schema = usersSchema()

api = Api(users_v1_0_bp)

class userListResource(Resource):
    def get(self):
        users = UsersPrv.get_all()
        result = users_schema.dump(users, many=True)
        return result
    def post(self):
        data = request.get_json()
        users_dict = users_schema.load(data)
        user = UsersPrv(users_dict)
        user.save()
        resp = users_schema.dump(user)
        return resp, 201

class userResource(Resource):
    def get(self, user_id):
        user = UsersPrv.get_by_id(user_id)
        if user is None:
            raise ObjectNotFound("Usuario no existe")
        resp = users_schema.dump(user)
        return resp        

api.add_resource(userListResource, '/api/v1.0/users/', endpoint='users_list_resource')
api.add_resource(userResource, '/api/v1.0/users/<int:users_id>', endpoint='users_resource')