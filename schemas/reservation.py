from marshmallow import Schema, fields, post_dump, validate, validates, ValidationError
from schemas.student import StudentSchema
from schemas.teacher import TeacherSchema

class ReservationSchema_A(Schema):
    class Meta:
        ordered = True

    Room_A_id = fields.Integer(dump_only=True)
    Room_A_name = fields.String(required=True, validate=[validate.Length(max=100)])
    Room_A_is_reserved = fields.Boolean(default=False, dump_only=True)
    Room_A_start_time = fields.String(required=True, validate=[validate.Length(max=20)])
    Room_A_end_time = fields.String(required=True, validate=[validate.Length(max=20)])
    Room_A_student = fields.Nested(StudentSchema, attribute='student', dump_only=True, only=['student_id', 'student_username'])
    Room_A_teacher = fields.Nested(TeacherSchema, attribute='teacher', dump_only=True, only=['teacher_id', 'teacher_username'])

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}

        return data


class ReservationSchema_B(Schema):
    class Meta:
        ordered = True

    Room_B_id = fields.Integer(dump_only=True)
    Room_B_name = fields.String(required=True, validate=[validate.Length(max=100)])
    Room_B_is_reserved = fields.Boolean(default=False, dump_only=True)
    Room_B_start_time = fields.String(required=True, validate=[validate.Length(max=20)])
    Room_B_end_time = fields.String(required=True, validate=[validate.Length(max=20)])
    Room_B_student = fields.Nested(StudentSchema, attribute='student', dump_only=True, only=['student_id', 'student_username'])
    Room_B_teacher = fields.Nested(TeacherSchema, attribute='teacher', dump_only=True, only=['teacher_id', 'teacher_username'])

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}

        return data

class ReservationSchema_C(Schema):
    class Meta:
        ordered = True

    Room_C_id = fields.Integer(dump_only=True)
    Room_C_name = fields.String(required=True, validate=[validate.Length(max=100)])
    Room_C_is_reserved = fields.Boolean(default=False, dump_only=True)
    Room_C_start_time = fields.String(required=True, validate=[validate.Length(max=20)])
    Room_C_end_time = fields.String(required=True, validate=[validate.Length(max=20)])
    Room_C_student = fields.Nested(StudentSchema, attribute='student', dump_only=True,only=['student_id', 'student_username'])
    Room_C_teacher = fields.Nested(TeacherSchema, attribute='teacher', dump_only=True,only=['teacher_id', 'teacher_username'])

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}

        return data

class ReservationSchema_D(Schema):
    class Meta:
        ordered = True

    Room_D_id = fields.Integer(dump_only=True)
    Room_D_name = fields.String(required=True, validate=[validate.Length(max=100)])
    Room_D_is_reserved = fields.Boolean(default=False, dump_only=True)
    Room_D_start_time = fields.String(required=True, validate=[validate.Length(max=20)])
    Room_D_end_time = fields.String(required=True, validate=[validate.Length(max=20)])
    Room_D_student = fields.Nested(StudentSchema, attribute='student', dump_only=True,only=['student_id', 'student_username'])
    Room_D_teacher = fields.Nested(TeacherSchema, attribute='teacher', dump_only=True,only=['teacher_id', 'teacher_username'])

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}

        return data

