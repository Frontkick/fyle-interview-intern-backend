class FyleError(Exception):
    def __init__(self, status_code=None, message="An error occurred"):
        super().__init__(message)
        self.status_code = status_code if status_code is not None else 400
        self.message = message

    def to_dict(self):
        return {'status_code': self.status_code, 'message': self.message}
