
class DuplicateRequestError(Exception):
    pass


class RequestNotFoundError(Exception):
    pass


class InvalidPriorityError(Exception):
    pass


class AlreadyResolvedError(Exception):
    pass


class UnauthorizedError(Exception):
    pass
