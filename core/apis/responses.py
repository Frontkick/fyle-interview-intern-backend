from flask import Response, jsonify, make_response


class APIResponse(Response):
    @classmethod
    def respond(cls, data):
        res = jsonify(data=data)
        return make_response(res)
