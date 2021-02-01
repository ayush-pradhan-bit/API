from http import HTTPStatus
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity, jwt_required, get_raw_jwt

from utils import check_password
from models.teacher import Teacher

black_list_teacher = set()

class TokenResourceTeacher(Resource):

    # post method
    def post(self):
        json_data = request.get_json()
        teacher_username = json_data.get('teacher_username')
        teacher_password = json_data.get('teacher_password')

        teacher = Teacher.get_by_teacher_username(teacher_username=teacher_username)

        if not teacher or not check_password(teacher_password, teacher.teacher_password):
            return {'message': 'username or password is incorrect'}, HTTPStatus.UNAUTHORIZED

        teacher_access_token = create_access_token(identity=teacher.teacher_id, fresh=True)
        teacher_refresh_token = create_refresh_token(identity=teacher.teacher_id)
        return {'teacher_access_token': teacher_access_token, 'teacher_refresh_token': teacher_refresh_token}, HTTPStatus.OK


class RefreshResourceTeacher(Resource):

    @jwt_refresh_token_required
    def post(self):
        current_teacher = get_jwt_identity()

        teacher_access_token = create_access_token(identity=current_teacher, fresh=False)
        return {'teacher_access_token': teacher_access_token}, HTTPStatus.OK


class RevokeResourceTeacher(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']

        black_list_teacher.add(jti)
        return {'message': 'Successfully logged out'}, HTTPStatus.OK
