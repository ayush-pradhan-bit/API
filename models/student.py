from extensions import db

class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column(db.Integer, primary_key=True)
    student_username = db.Column(db.String(80), nullable=False, unique=True)
    student_password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    reservations_A = db.relationship('Reservation_A', backref='student')
    reservations_B = db.relationship('Reservation_B', backref='student')
    reservations_C = db.relationship('Reservation_C', backref='student')
    reservations_D = db.relationship('Reservation_D', backref='student')

    @classmethod
    def get_by_student_username(cls, student_username):
        return cls.query.filter_by(student_username=student_username).first()


    def save(self):
        db.session.add(self)
        db.session.commit()