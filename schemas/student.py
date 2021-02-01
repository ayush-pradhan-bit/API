from marshmallow import Schema, fields
from utils import hash_password

class StudentSchema(Schema):
    class Meta:
        ordered = True


    student_id = fields.Int(dump_only=True)
    student_username = fields.String(required=True)
    student_password = fields.Method(required=True, deserialize='load_password_student')

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    def load_password_student(self, value):
        return hash_password(value)