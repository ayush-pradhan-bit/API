from extensions import db

class Teacher(db.Model):
    __tablename__ = 'teacher'

    teacher_id = db.Column(db.Integer, primary_key=True)
    teacher_username = db.Column(db.String(80), nullable=False, unique=True)
    teacher_password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    reservations_A = db.relationship('Reservation_A', backref='teacher')
    reservations_B = db.relationship('Reservation_B', backref='teacher')
    reservations_C = db.relationship('Reservation_C', backref='teacher')
    reservations_D = db.relationship('Reservation_D', backref='teacher')

    @classmethod
    def get_by_teacher_username(cls, teacher_username):
        return cls.query.filter_by(teacher_username=teacher_username).first()


    def save(self):
        db.session.add(self)
        db.session.commit()