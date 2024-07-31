from flask import Blueprint, jsonify
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.teachers import Teacher
from core.apis.decorators import AuthPrincipal
from core.models.assignments import Assignment
from core.apis.assignments.schema import AssignmentSchema,AssignmentGradeSchema
from .schema import TeacherSchema

principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def get_all_teachers(auth_principal: AuthPrincipal):
    """
    Fetches details of all teachers from the database and returns them as a list of dictionaries.
    :return: A list of dictionaries containing teacher details
    """
    
    teachers = Teacher.all_teachers(auth_principal=AuthPrincipal)
    teachers_dump = TeacherSchema().dump(teachers,many=True)
    return APIResponse.respond(data=teachers_dump)
    # try:
    #     # Query all Teacher records
    #     teachers = db.session.query(Teacher).all()
    #     # Convert Teacher objects to dictionaries
    #     teachers_list = [{
    #         'id': teacher.id,
    #         'user_id': teacher.user_id,
    #         'created_at': teacher.created_at.isoformat(),
    #         'updated_at': teacher.updated_at.isoformat()
    #     } for teacher in teachers]
    #     # Return a JSON response
    #     return APIResponse.respond(data=teachers_list)
    # except Exception as e:
    #     # Handle any exceptions that occur
    #     print(f"An error occurred while fetching teachers: {e}")
    #     return jsonify({'error': 'An error occurred while fetching teachers.'}), 500

@principal_assignments_resources.route('/assignments', methods=['GET'])
@decorators.authenticate_principal
def get_submitted_and_graded_assignments(auth_principal: AuthPrincipal):
    assignments = Assignment.get_submitted_and_graded()
    students_assignments_dump = AssignmentSchema().dump(assignments, many=True)
    return APIResponse.respond(data=students_assignments_dump)
    
# def get_submitted_and_graded_assignments(auth_principal: AuthPrincipal):
#     try:
#         # Use the class method to get assignments that are both submitted and graded
#         assignments = Assignment.get_submitted_and_graded()

#         # Convert the assignments to dictionary format
#         assignments_dict = [assignment.to_dict() for assignment in assignments]

#         return APIResponse.respond(data={
#             'status': 'success',
#             'data': assignments_dict
#         }), 200

#     except Exception as e:
#         return jsonify({
#             'status': 'error',
#             'message': str(e)
#         }), 500

@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    graded_assignment = Assignment.mark_grade_by_principal(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)