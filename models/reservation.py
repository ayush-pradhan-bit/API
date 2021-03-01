from extensions import db

reservation_list_A = []

reservation_list_B = []

reservation_list_C = []

reservation_list_D = []


class Reservation_A(db.Model):

    __tablename__ = 'RoomA_Booking'

    Room_A_id = db.Column(db.Integer, primary_key=True)
    Room_A_name = db.Column(db.String(100), default='Room A')
    Room_A_is_reserved = db.Column(db.Boolean(), default=False)

    #Room_A_date = db.Column(db.DateTime(), nullable=False)

    #ToDo : Check the type of the data in the following statement

    Room_A_start_time = db.Column(db.String(20), nullable=False)
    Room_A_end_time = db.Column(db.String(20), nullable=False)
    Room_A_teacher_id = db.Column(db.Integer(), db.ForeignKey("teacher.teacher_id"))
    Room_A_student_id = db.Column(db.Integer(), db.ForeignKey("student.student_id"))


    def data(self):
        return{
            'Room_A_id': self.Room_A_id,
            'Room_A_name': self.Room_A_name,
            'Room_A_is_reserved': self.Room_A_is_reserved,
            ## TODO: CHeck if we can overcome date field serialization
            #'Room_A_date': self.Room_A_date,
            'Room_A_start_time': self.Room_A_start_time,
            'Room_A_end_time': self.Room_A_end_time,
            'Room_A_teacher_id': self.Room_A_teacher_id,
            'Room_A_student_id': self.Room_A_student_id
        }

    @classmethod
    ### checking all the reservations of the rooms A done by the user
    ### checking all the reservations of the rooms A done by the user
    def get_all_reserved(cls):
        return cls.query.filter_by(Room_A_is_reserved=True).all()

    @classmethod
    ##checking all the rooms with no reservation
    def get_all_not_reserved(cls):
        return cls.query.filter_by(Room_A_is_reserved=False).all()

    @classmethod
    ### getting the reservations of the room by id
    def get_by_id(cls, Room_A_id):
        return cls.query.filter_by(Room_A_id=Room_A_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

#reservation for the room B
class Reservation_B(db.Model):

    __tablename__ = 'RoomB_Booking'

    Room_B_id = db.Column(db.Integer, primary_key=True)
    Room_B_name = db.Column(db.String(100), default='Room B')
    Room_B_is_reserved = db.Column(db.Boolean(), default=False)


    #ToDo : Check the type of the data in the following statement

    Room_B_start_time = db.Column(db.String(20), nullable=False)
    Room_B_end_time = db.Column(db.String(20), nullable=False)
    Room_B_teacher_id = db.Column(db.Integer(), db.ForeignKey("teacher.teacher_id"))
    Room_B_student_id = db.Column(db.Integer(), db.ForeignKey("student.student_id"))


    def data(self):
        return{
            'Room_B_id': self.Room_B_id,
            'Room_B_name': self.Room_B_name,
            'Room_B_is_reserved': self.Room_B_is_reserved,
        ## TODO: CHeck if we can overcome date field serialization
            #'Room_B_date': self.Room_B_date,
            'Room_B_start_time': self.Room_B_start_time,
            'Room_B_end_time': self.Room_B_end_time,
            'Room_B_teacher_id': self.Room_B_teacher_id,
            'Room_B_student_id': self.Room_B_student_id
        }

    @classmethod
    ### checking all the reservations of the rooms B done by the user
    def get_all_reserved(cls):
        return cls.query.filter_by(Room_B_is_reserved=True).all()

    @classmethod
    ##checking all the rooms with no reservation
    def get_all_not_reserved(cls):
        return cls.query.filter_by(Room_B_is_reserved=False).all()

    @classmethod
    ### getting the reservations of the room by id
    def get_by_id(cls, Room_B_id):
        return cls.query.filter_by(Room_B_id=Room_B_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

#reservation for the room C
class Reservation_C(db.Model):

    __tablename__ = 'RoomC_Booking'

    Room_C_id = db.Column(db.Integer, primary_key=True)
    Room_C_name = db.Column(db.String(100), default='Room C')
    Room_C_is_reserved = db.Column(db.Boolean(), default=False)

    #Room_C_date = db.Column(db.DateTime(), nullable=False)

    #ToDo : Check the type of the data in the following statement

    Room_C_start_time = db.Column(db.String(20), nullable=False)
    Room_C_end_time = db.Column(db.String(20), nullable=False)
    Room_C_teacher_id = db.Column(db.Integer(), db.ForeignKey("teacher.teacher_id"))
    Room_C_student_id = db.Column(db.Integer(), db.ForeignKey("student.student_id"))


    def data(self):
        return{
            'Room_C_id': self.Room_C_id,
            'Room_C_name': self.Room_C_name,
            'Room_C_is_reserved': self.Room_C_is_reserved,
            ## TODO: CHeck if we can overcome date field serialization
            #'Room_C_date': self.Room_C_date,
            'Room_C_start_time': self.Room_C_start_time,
            'Room_C_end_time': self.Room_C_end_time,
            'Room_C_teacher_id': self.Room_C_teacher_id,
            'Room_C_student_id': self.Room_C_student_id
        }

    @classmethod
    ### checking all the reservations of the rooms B done by the user
    def get_all_reserved(cls):
        return cls.query.filter_by(Room_C_is_reserved=True).all()

    @classmethod
    ##checking all the rooms with no reservation
    def get_all_not_reserved(cls):
        return cls.query.filter_by(Room_C_is_reserved=False).all()

    @classmethod
    ### getting the reservations of the room by id
    def get_by_id(cls, Room_C_id):
        return cls.query.filter_by(Room_C_id=Room_C_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

#reservation for the room D
class Reservation_D(db.Model):

    __tablename__ = 'RoomD_Booking'

    Room_D_id = db.Column(db.Integer, primary_key=True)
    Room_D_name = db.Column(db.String(100), default='Room A')
    Room_D_is_reserved = db.Column(db.Boolean(), default=False)

    #Room_D_date = db.Column(db.DateTime(), nullable=False)

    #ToDo : Check the type of the data in the following statement

    Room_D_start_time = db.Column(db.String(20), nullable=False)
    Room_D_end_time = db.Column(db.String(20), nullable=False)
    Room_D_teacher_id = db.Column(db.Integer(), db.ForeignKey("teacher.teacher_id"))
    Room_D_student_id = db.Column(db.Integer(), db.ForeignKey("student.student_id"))


    def data(self):
        return{
            'Room_D_id': self.Room_D_id,
            'Room_D_name': self.Room_D_name,
            'Room_D_is_reserved': self.Room_D_is_reserved,
            ## TODO: CHeck if we can overcome date field serialization
            #'Room_D_date': self.Room_D_date,
            'Room_D_start_time': self.Room_D_start_time,
            'Room_D_end_time': self.Room_D_end_time,
            'Room_D_teacher_id': self.Room_D_teacher_id,
            'Room_D_student_id': self.Room_D_student_id
        }

    @classmethod
    ### checking all the reservations of the rooms B done by the user
    def get_all_reserved(cls):
        return cls.query.filter_by(Room_D_is_reserved=True).all()

    @classmethod
    ##checking all the rooms with no reservation
    def get_all_not_reserved(cls):
        return cls.query.filter_by(Room_D_is_reserved=False).all()

    @classmethod
    ### getting the reservations of the room by id
    def get_by_id(cls, Room_D_id):
        return cls.query.filter_by(Room_D_id=Room_D_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()