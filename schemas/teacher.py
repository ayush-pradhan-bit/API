from marshmallow import Schema, fields
from utils import hash_password

class TeacherSchema(Schema):
    class Meta:
        ordered = True


    teacher_id = fields.Int(dump_only=True)
    teacher_username = fields.String(required=True)
    teacher_password = fields.Method(required=True, deserialize='load_password_teacher')

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    def load_password_teacher(self, value):
        return hash_password(value)