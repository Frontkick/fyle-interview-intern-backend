# from flask import Blueprint, request, jsonify
# from core.apis.decorators import AuthPrincipal
# from core.models.assignments import Assignment, AssignmentStateEnum
# from core.models.principals import Principal
# from core.libs.helpers import get_utc_now
# from .principal import principal_assignments_resources
# from core.apis.decorators import AuthPrincipal
# from core.apis import decorators
# from core.apis.responses import APIResponse

# @principal_assignments_resources.route('/assignments', methods=['GET'])
# @decorators.authenticate_principal
# def get_submitted_and_graded_assignments(auth_principal: AuthPrincipal):
#     try:
#         # Query assignments that are both SUBMITTED and GRADED
#         assignments = Assignment.filter(
#             Assignment.state.in_([AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED])
#         ).all()

#         # Filter assignments to ensure that they are both submitted and graded
#         filtered_assignments = [a for a in assignments if a.state == AssignmentStateEnum.GRADED]

#         return APIResponse(data={
#             'status': 'success',
#             'data': [a.to_dict() for a in filtered_assignments]
#         }), 200

#     except Exception as e:
#         return jsonify({
#             'status': 'error',
#             'message': str(e)
#         }), 500