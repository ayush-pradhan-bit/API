from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from Resources.reservation import ReservationListResource_A, ReservationResource_A_Teachers, \
    ReservationCacelResource_A_Students, ReservationResource_A_Students, ReservationCacelResource_A_Teachers

from Resources.reservation import ReservationListResource_B, ReservationResource_B_Teachers,\
    ReservationCancelResource_B_Teachers, ReservationResource_B_Students, ReservationCacelResource_B_Students

from Resources.reservation import ReservationListResource_C, ReservationResource_C_Teachers, \
    ReservationCacelResource_C_Students, ReservationResource_C_Students, ReservationCancelResource_C_Teachers

from Resources.reservation import ReservationListResource_D, ReservationResource_D_Teachers,\
    ReservationCancelResource_D_Teachers, ReservationResource_D_Students, ReservationCacelResource_D_Students

from config import Config
from extensions import db, jwt

from Resources.student import StudentAddResource, StudentResource
from Resources.teacher import TeacherAddResource, TeacherResource

from Resources.token_teacher import TokenResourceTeacher, RefreshResourceTeacher, RevokeResourceTeacher, \
    black_list_teacher

from Resources.token_student import TokenResourceStudent, RefreshResourceStudent, RevokeResourceStudent, \
    black_list_student




def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app

def register_extensions(app):
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist_student(decrypted_token_students):
        jti = decrypted_token_students['jti']
        return jti in black_list_student

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist_teacher(decrypted_token_teachers):
        jti = decrypted_token_teachers['jti']
        return jti in black_list_teacher

def register_resources(app):
    api = Api(app)
    #checking all non reserved rooms
    #can be accessed by anyone
    api.add_resource(ReservationListResource_A, '/reservations/A')

    #checking for the room Number B
    #can be accessed by anyone
    api.add_resource(ReservationListResource_B, '/reservations/B')

    # checking for the room Number C
    # can be accessed by anyone
    api.add_resource(ReservationListResource_C, '/reservations/C')

    # checking for the room Number D
    # can be accessed by anyone
    api.add_resource(ReservationListResource_D, '/reservations/D')

    #Booking a particular Room using its ID
    #students can access this
    api.add_resource(ReservationResource_A_Students, '/reservations/students/A/<int:reservation_A_id>')
    api.add_resource(ReservationResource_B_Students, '/reservations/students/B/<int:reservation_B_id>')
    api.add_resource(ReservationResource_C_Students, '/reservations/students/C/<int:reservation_C_id>')
    api.add_resource(ReservationResource_D_Students, '/reservations/students/D/<int:reservation_D_id>')


    #teachers can access this
    api.add_resource(ReservationResource_A_Teachers, '/reservations/teachers/A/<int:reservation_A_id>')
    api.add_resource(ReservationResource_B_Teachers, '/reservations/teachers/B/<int:reservation_B_id>')
    api.add_resource(ReservationResource_C_Teachers, '/reservations/teachers/C/<int:reservation_C_id>')
    api.add_resource(ReservationResource_D_Teachers, '/reservations/teachers/D/<int:reservation_D_id>')


    #Canceling the rooms
    #Students
    api.add_resource(ReservationCacelResource_A_Students, '/reservations/students/A/<int:reservation_A_id>/cancel')
    api.add_resource(ReservationCacelResource_B_Students, '/reservations/students/B/<int:reservation_B_id>/cancel')
    api.add_resource(ReservationCacelResource_C_Students, '/reservations/students/C/<int:reservation_C_id>/cancel')
    api.add_resource(ReservationCacelResource_D_Students, '/reservations/students/D/<int:reservation_D_id>/cancel')

    #Teachers
    api.add_resource(ReservationCacelResource_A_Teachers, '/reservations/teachers/A/<int:reservation_A_id>/cancel')
    api.add_resource(ReservationCancelResource_B_Teachers, '/reservations/teachers/B/<int:reservation_B_id>/cancel')
    api.add_resource(ReservationCancelResource_C_Teachers, '/reservations/teachers/C/<int:reservation_C_id>/cancel')
    api.add_resource(ReservationCancelResource_D_Teachers, '/reservations/teachers/D/<int:reservation_D_id>/cancel')


    #Adding the students
    api.add_resource(StudentAddResource, '/students')
    #adding the teachers
    api.add_resource(TeacherAddResource, '/teachers')

    #check on students
    api.add_resource(StudentResource, '/students/<string:student_username>')
    #check on teachers
    api.add_resource(TeacherResource, '/teachers/<string:teacher_username>')

    #token creation
    #students
    api.add_resource(TokenResourceStudent, '/token/students')
    #teachers
    api.add_resource(TokenResourceTeacher, '/token/teachers')

    ##Refresh Tokens
    #student
    api.add_resource(RefreshResourceStudent, '/refresh/students')
    #teachers
    api.add_resource(RefreshResourceTeacher, '/refresh/teachers')

    ##Revoke Tokens
    #student
    api.add_resource(RevokeResourceStudent, '/revoke/students')
    #teachers
    api.add_resource(RevokeResourceTeacher, '/revoke/teachers')




if __name__ == '__main__':
    app = create_app()
    app.run()