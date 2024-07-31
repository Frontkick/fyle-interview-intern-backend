from flask import Blueprint, jsonify
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.teachers import Teacher
from .schema import AssignmentSchema, AssignmentGradeSchema

teacher_assignments_resources = Blueprint('teacher_assignments_resources', __name__)

@teacher_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments"""
    teachers_assignments = Assignment.get_assignments_by_teacher(p.teacher_id)
    teachers_assignments_dump = AssignmentSchema().dump(teachers_assignments, many=True)
    return APIResponse.respond(data=teachers_assignments_dump)

@teacher_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    if(incoming_payload == None):
        print("None")
        return APIResponse.respond(data="status code 400")
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)

# @teacher_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
# def get_all_teachers():
#     """
#     Fetches details of all teachers from the database and returns them as a list of dictionaries.
#     :return: A list of dictionaries containing teacher details
#     """
#     try:
#         # Query all Teacher records
#         teachers = db.session.query(Teacher).all()
#         # Convert Teacher objects to dictionaries
#         teachers_list = [{
#             'id': teacher.id,
#             'user_id': teacher.user_id,
#             'created_at': teacher.created_at.isoformat(),
#             'updated_at': teacher.updated_at.isoformat()
#         } for teacher in teachers]
#         # Return a JSON response
#         return APIResponse.respond(data=teachers_list)
#     except Exception as e:
#         # Handle any exceptions that occur
#         print(f"An error occurred while fetching teachers: {e}")
#         return jsonify({'error': 'An error occurred while fetching teachers.'}), 500


# @teacher_assignments_resources.route('/test', methods=['GET'])
# def test_route():
#     return "Test route is working!"
