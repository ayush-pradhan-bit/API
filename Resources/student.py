from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.teacher import Teacher
from utils import hash_password
from models.student import Student

from flask_jwt_extended import jwt_optional, get_jwt_identity
from schemas.student import StudentSchema

student_schema = StudentSchema()
student_public_schema = StudentSchema(exclude=('student_id', ))


class StudentAddResource(Resource):

    def post(self):
        json_data = request.get_json()

        data, errors =student_schema.load(data=json_data)

        if errors:
            return {'message': 'Validation Errors', 'errors': errors}, HTTPStatus.BAD_REQUEST


        if Student.get_by_student_username(data.get('student_username')):
            return {'message': 'Student already exists'}, HTTPStatus.BAD_REQUEST

        student = Student(**data)

        student.save()


        return student_schema.dump(student).data, HTTPStatus.CREATED

class StudentResource(Resource):

    @jwt_optional
    def get(self, student_username):
        student = Student.get_by_student_username(student_username=student_username)

        if student is None:
            return {'message': 'student does not exist'}, HTTPStatus.NOT_FOUND

        current_student = get_jwt_identity()

        if current_student == student.student_id:
            data = student_schema.dump(student).data

        else:
            data = student_public_schema.dump(student).data

        return data, HTTPStatus.OK