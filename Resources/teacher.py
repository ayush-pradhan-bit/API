from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.teacher import Teacher

from flask_jwt_extended import jwt_optional, get_jwt_identity
from schemas.teacher import TeacherSchema

teacher_schema = TeacherSchema()
teacher_public_schema = TeacherSchema(exclude=('teacher_id', ))


class TeacherAddResource(Resource):

    def post(self):
        json_data = request.get_json()

        data, errors =teacher_schema.load(data=json_data)

        if errors:
            return {'message': 'Validation Errors', 'errors': errors}, HTTPStatus.BAD_REQUEST


        if Teacher.get_by_teacher_username(data.get('teacher_username')):
            return {'message': 'Teacher already exists'}, HTTPStatus.BAD_REQUEST

        teacher = Teacher(**data)

        teacher.save()


        return teacher_schema.dump(teacher).data, HTTPStatus.CREATED

class TeacherResource(Resource):

    @jwt_optional
    def get(self, teacher_username):
        teacher = Teacher.get_by_teacher_username(teacher_username=teacher_username)

        if teacher is None:
            return {'message': 'teacher does not exist'}, HTTPStatus.NOT_FOUND

        current_teacher = get_jwt_identity()

        if current_teacher == teacher.teacher_id:
            data = teacher_schema.dump(teacher).data

        else:
            data = teacher_public_schema.dump(teacher).data

        return data, HTTPStatus.OK