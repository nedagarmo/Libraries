class BadRequestException(Exception):

    def __init__(self, data=None):
        self.data = data or {}

    def to_dict(self):
        return self.data
