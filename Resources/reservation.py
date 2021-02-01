from flask import request
from flask_restful import Resource
from http import HTTPStatus
from schemas.reservation import ReservationSchema_A, ReservationSchema_B, ReservationSchema_C, ReservationSchema_D
from models.reservation import Reservation_A, Reservation_B, Reservation_C, Reservation_D
from flask_jwt_extended import get_jwt_identity, jwt_optional, jwt_required


reservation_schema_A = ReservationSchema_A()
reservation_list_schema_A = ReservationSchema_A(many=True)

reservation_schema_B = ReservationSchema_B()
reservation_list_schema_B = ReservationSchema_B(many=True)

reservation_schema_C = ReservationSchema_C()
reservation_list_schema_C = ReservationSchema_C(many=True)

reservation_schema_D = ReservationSchema_D()
reservation_list_schema_D = ReservationSchema_D(many=True)


class ReservationListResource_A(Resource):

    def get(self):

        reservations_A = Reservation_A.get_all_not_reserved()

        return reservation_list_schema_A.dump(reservations_A).data, HTTPStatus.OK


class ReservationResource_A_Students(Resource):
    @jwt_optional
    def get(self, reservation_A_id):

        reservation_A = Reservation_A.get_by_id(Room_A_id=reservation_A_id)

        if reservation_A is None:
            return {'message': 'Room is reserved'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()


        if reservation_A.Room_A_is_reserved == True and current_user != reservation_A.Room_A_student_id:
            return {'message': 'The room is reserved'}, HTTPStatus.FORBIDDEN

        return reservation_A.data(), HTTPStatus.OK

    @jwt_required
    def put(self, reservation_A_id):
        json_data = request.get_json()
        reservation_A = Reservation_A.get_by_id(Room_A_id=reservation_A_id)

        if reservation_A is None:
            return {'message': 'Room is reserved'}, HTTPStatus.FORBIDDEN

        current_user = get_jwt_identity()

        if reservation_A.Room_A_student_id is not None:

            if current_user != reservation_A.Room_A_student_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORBIDDEN

            else:
                reservation_A.Room_A_is_reserved = True
                reservation_A.save()


        else:
            if current_user != reservation_A.Room_A_teacher_id:
                reservation_A.Room_A_is_reserved = True
                reservation_A.Room_A_student_id = current_user


            reservation_A.save()
        return reservation_A.data(), HTTPStatus.OK




class ReservationResource_A_Teachers(Resource):
    @jwt_optional
    def get(self, reservation_A_id):

        reservation_A = Reservation_A.get_by_id(Room_A_id=reservation_A_id)

        if reservation_A is None:
            return {'message': 'Room is reserved'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if reservation_A.Room_A_is_reserved == True and current_user != reservation_A.Room_A_teacher_id:
            return {'message': 'The room is reserved'}, HTTPStatus.FORBIDDEN

        return reservation_A.data(), HTTPStatus.OK

    @jwt_required
    def put(self, reservation_A_id):
        json_data = request.get_json()
        reservation_A = Reservation_A.get_by_id(Room_A_id=reservation_A_id)

        if reservation_A is None:
            return {'message': 'Room is reserved'}, HTTPStatus.FORBIDDEN

        current_user = get_jwt_identity()

        if reservation_A.Room_A_teacher_id is not None:

            if current_user != reservation_A.Room_A_teacher_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORBIDDEN


        else:
            if current_user != reservation_A.Room_A_student_id:
                reservation_A.Room_A_is_reserved = True
                reservation_A.Room_A_teacher_id= current_user

                reservation_A.save()

        return reservation_A.data(), HTTPStatus.OK

class ReservationCacelResource_A_Students(Resource):

    @jwt_required
    def put(self, reservation_A_id):
        json_data = request.get_json()

        reservation_A = Reservation_A.get_by_id(Room_A_id=reservation_A_id)

        if reservation_A is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if reservation_A.Room_A_student_id is not None:

            if current_user != reservation_A.Room_A_student_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORBIDDEN

            else:

                reservation_A.Room_A_is_reserved = False
                reservation_A.Room_A_student_id = None

        else:
            reservation_A.Room_A_is_reserved = False
            reservation_A.Room_A_student_id = None

        reservation_A.save()
        return reservation_A.data(), HTTPStatus.OK


class ReservationCacelResource_A_Teachers(Resource):

    @jwt_required
    def put(self, reservation_A_id):
        json_data = request.get_json()

        reservation_A = Reservation_A.get_by_id(Room_A_id=reservation_A_id)

        if reservation_A is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if reservation_A.Room_A_teacher_id is not None:

            if current_user!=reservation_A.Room_A_teacher_id:
                return {'message':'Room is reserved'}, HTTPStatus.FORBIDDEN

            else:
                reservation_A.Room_A_is_reserved = False
                reservation_A.Room_A_teacher_id = None

        else:
            reservation_A.Room_A_is_reserved = json_data['Room_A_is_reserved']
        reservation_A.save()
        return reservation_A.data(), HTTPStatus.OK


## Defining Reservations for Room B

class ReservationListResource_B(Resource):

    def get(self):
        reservations_B = Reservation_B.get_all_not_reserved()

        return reservation_list_schema_B.dump(reservations_B).data, HTTPStatus.OK


class ReservationResource_B_Students(Resource):
    @jwt_optional
    def get(self, reservation_B_id):

        reservation_B = Reservation_B.get_by_id(Room_B_id=reservation_B_id)

        if reservation_B is None:
            return {'message': 'Room is reserved'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if reservation_B.Room_B_is_reserved == True and current_user != reservation_B.Room_B_student_id:
            return {'message': 'The room is reserved'}, HTTPStatus.FORBIDDEN

        return reservation_B.data(), HTTPStatus.OK

    @jwt_required
    def put(self, reservation_B_id):
        json_data = request.get_json()
        reservation_B = Reservation_B.get_by_id(Room_B_id=reservation_B_id)

        if reservation_B is None:
            return {'message': 'Room is reserved'}, HTTPStatus.FORBIDDEN

        current_user = get_jwt_identity()

        if reservation_B.Room_B_student_id is not None:

            if current_user != reservation_B.Room_B_student_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORBIDDEN


        else:
            if current_user != reservation_B.Room_B_teacher_id:
                reservation_B.Room_B_is_reserved = True
                reservation_B.Room_B_student_id = current_user

            reservation_B.save()
        return reservation_B.data(), HTTPStatus.OK


class ReservationResource_B_Teachers(Resource):
    @jwt_optional
    def get(self, reservation_B_id):

        reservation_B = Reservation_B.get_by_id(Room_B_id=reservation_B_id)

        if reservation_B is None:
            return {'message': 'Room is reserved'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if reservation_B.Room_B_is_reserved == True and current_user != reservation_B.Room_B_teacher_id:
            return {'message': 'The room is reserved'}, HTTPStatus.FORBIDDEN

        return reservation_B.data(), HTTPStatus.OK

    @jwt_required
    def put(self, reservation_B_id):
        json_data = request.get_json()
        reservation_B = Reservation_B.get_by_id(Room_B_id=reservation_B_id)

        if reservation_B is None:
            return {'message': 'Room is reserved'}, HTTPStatus.FORBIDDEN

        current_user = get_jwt_identity()

        if reservation_B.Room_B_teacher_id is not None:

            if current_user != reservation_B.Room_B_teacher_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORBIDDEN
            else:
                return


        else:
            if current_user != reservation_B.Room_B_student_id:
                reservation_B.Room_B_is_reserved = True
                reservation_B.Room_B_teacher_id = current_user

                reservation_B.save()

        return reservation_B.data(), HTTPStatus.OK


class ReservationCacelResource_B_Students(Resource):

    @jwt_required
    def put(self, reservation_B_id):
        json_data = request.get_json()

        reservation_B = Reservation_B.get_by_id(Room_B_id=reservation_B_id)

        if reservation_B is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if reservation_B.Room_B_student_id is not None:

            if current_user != reservation_B.Room_B_student_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORBIDDEN

            else:
                reservation_B.Room_B_is_reserved = False

                reservation_B.Room_B_student_id = None

        else:
            reservation_B.Room_B_is_reserved = False

            reservation_B.Room_B_student_id = None

        reservation_B.save()
        return reservation_B.data(), HTTPStatus.OK


class ReservationCancelResource_B_Teachers(Resource):

    @jwt_required
    def put(self, reservation_B_id):
        json_data = request.get_json()

        reservation_B = Reservation_B.get_by_id(Room_B_id=reservation_B_id)

        if reservation_B is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if reservation_B.Room_B_teacher_id is not None:

            if current_user != reservation_B.Room_B_teacher_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORBIDDEN

            else:
                reservation_B.Room_B_is_reserved = False
                reservation_B.Room_B_teacher_id = None

        else:
            reservation_B.Room_B_is_reserved = False
            reservation_B.Room_B_teacher_id = None

        reservation_B.save()
        return reservation_B.data(), HTTPStatus.OK

## Defining reservations for Room C

class ReservationListResource_C(Resource):

    def get(self):
        reservations_C = Reservation_C.get_all_not_reserved()

        return reservation_list_schema_C.dump(reservations_C).data, HTTPStatus.OK


class ReservationResource_C_Students(Resource):
    @jwt_optional
    def get(self, reservation_C_id):

        reservation_C = Reservation_C.get_Cy_id(Room_C_id=reservation_C_id)

        if reservation_C is None:
            return {'message': 'Room is reserved'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if reservation_C.Room_C_is_reserved == True and current_user != reservation_C.Room_C_student_id:
            return {'message': 'The room is reserved'}, HTTPStatus.FORCIDDEN

        return reservation_C.data(), HTTPStatus.OK

    @jwt_required
    def put(self, reservation_C_id):
        json_data = request.get_json()
        reservation_C = Reservation_C.get_Cy_id(Room_C_id=reservation_C_id)

        if reservation_C is None:
            return {'message': 'Room is reserved'}, HTTPStatus.FORCIDDEN

        current_user = get_jwt_identity()

        if reservation_C.Room_C_student_id is not None:

            if current_user != reservation_C.Room_C_student_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORCIDDEN


        else:
            if current_user != reservation_C.Room_C_teacher_id:
                reservation_C.Room_C_is_reserved = True
                reservation_C.Room_C_student_id = current_user

            reservation_C.save()
        return reservation_C.data(), HTTPStatus.OK


class ReservationResource_C_Teachers(Resource):
    @jwt_optional
    def get(self, reservation_C_id):

        reservation_C = Reservation_C.get_Cy_id(Room_C_id=reservation_C_id)

        if reservation_C is None:
            return {'message': 'Room is reserved'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if reservation_C.Room_C_is_reserved == True and current_user != reservation_C.Room_C_teacher_id:
            return {'message': 'The room is reserved'}, HTTPStatus.FORCIDDEN

        return reservation_C.data(), HTTPStatus.OK

    @jwt_required
    def put(self, reservation_C_id):
        json_data = request.get_json()
        reservation_C = Reservation_C.get_Cy_id(Room_C_id=reservation_C_id)

        if reservation_C is None:
            return {'message': 'Room is reserved'}, HTTPStatus.FORCIDDEN

        current_user = get_jwt_identity()

        if reservation_C.Room_C_teacher_id is not None:

            if current_user != reservation_C.Room_C_teacher_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORCIDDEN
            else:
                return


        else:
            if current_user != reservation_C.Room_C_student_id:
                reservation_C.Room_C_is_reserved = True
                reservation_C.Room_C_teacher_id = current_user

                reservation_C.save()

        return reservation_C.data(), HTTPStatus.OK


class ReservationCacelResource_C_Students(Resource):

    @jwt_required
    def put(self, reservation_C_id):
        json_data = request.get_json()

        reservation_C = Reservation_C.get_Cy_id(Room_C_id=reservation_C_id)

        if reservation_C is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if reservation_C.Room_C_student_id is not None:

            if current_user != reservation_C.Room_C_student_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORCIDDEN

            else:
                reservation_C.Room_C_is_reserved = False

                reservation_C.Room_C_student_id = None

        else:
            reservation_C.Room_C_is_reserved = False

            reservation_C.Room_C_student_id = None

        reservation_C.save()
        return reservation_C.data(), HTTPStatus.OK


class ReservationCancelResource_C_Teachers(Resource):

    @jwt_required
    def put(self, reservation_C_id):
        json_data = request.get_json()

        reservation_C = Reservation_C.get_Cy_id(Room_C_id=reservation_C_id)

        if reservation_C is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if reservation_C.Room_C_teacher_id is not None:

            if current_user != reservation_C.Room_C_teacher_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORCIDDEN

            else:
                reservation_C.Room_C_is_reserved = False
                reservation_C.Room_C_teacher_id = None

        else:
            reservation_C.Room_C_is_reserved = False
            reservation_C.Room_C_teacher_id = None

        reservation_C.save()
        return reservation_C.data(), HTTPStatus.OK

## Defining Reservations for Room D

class ReservationListResource_D(Resource):

    def get(self):
        reservations_D = Reservation_D.get_all_not_reserved()

        return reservation_list_schema_D.dump(reservations_D).data, HTTPStatus.OK


class ReservationResource_D_Students(Resource):
    @jwt_optional
    def get(self, reservation_D_id):

        reservation_D = Reservation_D.get_Dy_id(Room_D_id=reservation_D_id)

        if reservation_D is None:
            return {'message': 'Room is reserved'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if reservation_D.Room_D_is_reserved == True and current_user != reservation_D.Room_D_student_id:
            return {'message': 'The room is reserved'}, HTTPStatus.FORDIDDEN

        return reservation_D.data(), HTTPStatus.OK

    @jwt_required
    def put(self, reservation_D_id):
        json_data = request.get_json()
        reservation_D = Reservation_D.get_Dy_id(Room_D_id=reservation_D_id)

        if reservation_D is None:
            return {'message': 'Room is reserved'}, HTTPStatus.FORDIDDEN

        current_user = get_jwt_identity()

        if reservation_D.Room_D_student_id is not None:

            if current_user != reservation_D.Room_D_student_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORDIDDEN


        else:
            if current_user != reservation_D.Room_D_teacher_id:
                reservation_D.Room_D_is_reserved = True
                reservation_D.Room_D_student_id = current_user

            reservation_D.save()
        return reservation_D.data(), HTTPStatus.OK


class ReservationResource_D_Teachers(Resource):
    @jwt_optional
    def get(self, reservation_D_id):

        reservation_D = Reservation_D.get_Dy_id(Room_D_id=reservation_D_id)

        if reservation_D is None:
            return {'message': 'Room is reserved'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if reservation_D.Room_D_is_reserved == True and current_user != reservation_D.Room_D_teacher_id:
            return {'message': 'The room is reserved'}, HTTPStatus.FORDIDDEN

        return reservation_D.data(), HTTPStatus.OK

    @jwt_required
    def put(self, reservation_D_id):
        json_data = request.get_json()
        reservation_D = Reservation_D.get_Dy_id(Room_D_id=reservation_D_id)

        if reservation_D is None:
            return {'message': 'Room is reserved'}, HTTPStatus.FORDIDDEN

        current_user = get_jwt_identity()

        if reservation_D.Room_D_teacher_id is not None:

            if current_user != reservation_D.Room_D_teacher_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORDIDDEN
            else:
                return


        else:
            if current_user != reservation_D.Room_D_student_id:
                reservation_D.Room_D_is_reserved = True
                reservation_D.Room_D_teacher_id = current_user

                reservation_D.save()

        return reservation_D.data(), HTTPStatus.OK


class ReservationCacelResource_D_Students(Resource):

    @jwt_required
    def put(self, reservation_D_id):
        json_data = request.get_json()

        reservation_D = Reservation_D.get_Dy_id(Room_D_id=reservation_D_id)

        if reservation_D is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if reservation_D.Room_D_student_id is not None:

            if current_user != reservation_D.Room_D_student_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORDIDDEN

            else:
                reservation_D.Room_D_is_reserved = False

                reservation_D.Room_D_student_id = None

        else:
            reservation_D.Room_D_is_reserved = False

            reservation_D.Room_D_student_id = None

        reservation_D.save()
        return reservation_D.data(), HTTPStatus.OK


class ReservationCancelResource_D_Teachers(Resource):

    @jwt_required
    def put(self, reservation_D_id):
        json_data = request.get_json()

        reservation_D = Reservation_D.get_Dy_id(Room_D_id=reservation_D_id)

        if reservation_D is None:
            return {'message': 'Room not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if reservation_D.Room_D_teacher_id is not None:

            if current_user != reservation_D.Room_D_teacher_id:
                return {'message': 'Room is reserved'}, HTTPStatus.FORDIDDEN

            else:
                reservation_D.Room_D_is_reserved = False
                reservation_D.Room_D_teacher_id = None

        else:
            reservation_D.Room_D_is_reserved = False
            reservation_D.Room_D_teacher_id = None

        reservation_D.save()
        return reservation_D.data(), HTTPStatus.OK

