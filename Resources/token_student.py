from http import HTTPStatus
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity, jwt_required, get_raw_jwt

from utils import check_password
from models.student import Student

black_list_student = set()

class TokenResourceStudent(Resource):

    # post method
    def post(self):
        json_data = request.get_json()
        student_username = json_data.get('student_username')
        student_password = json_data.get('student_password')

        student = Student.get_by_student_username(student_username=student_username)

        if not student or not check_password(student_password, student.student_password):
            return {'message': 'username or password is incorrect'}, HTTPStatus.UNAUTHORIZED

        student_access_token = create_access_token(identity=student.student_id, fresh=True)
        student_refresh_token = create_refresh_token(identity=student.student_id)
        return {'student_access_token': student_access_token, 'student_refresh_token': student_refresh_token}, HTTPStatus.OK


class RefreshResourceStudent(Resource):

    @jwt_refresh_token_required
    def post(self):
        current_student = get_jwt_identity()

        student_access_token = create_access_token(identity=current_student, fresh=False)
        return {'student_access_token': student_access_token}, HTTPStatus.OK


class RevokeResourceStudent(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']

        black_list_student.add(jti)
        return {'message': 'Successfully logged out'}, HTTPStatus.OK
