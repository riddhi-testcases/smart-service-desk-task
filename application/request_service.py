
from domain.service_request import ServiceRequest
from domain.exceptions import (
    DuplicateRequestError,
    RequestNotFoundError,
    AlreadyResolvedError,
    UnauthorizedError
)


class RequestService:

    def __init__(self, repository):
        self.repository = repository
        self.requests = self.repository.load_requests()

    def create_request(self, request_id, employee_name, issue, priority):

        for request in self.requests:
            if request.request_id == request_id:
                raise DuplicateRequestError(
                    "Request ID already exists."
                )

        new_request = ServiceRequest(
            request_id,
            employee_name,
            issue,
            priority
        )

        self.requests.append(new_request)
        self.repository.save_requests(self.requests)

        return new_request

    def view_requests(self):
        return self.requests

    def search_request(self, request_id):

        for request in self.requests:
            if request.request_id == request_id:
                return request

        raise RequestNotFoundError(
            "Request not found."
        )

    def resolve_request(self, request_id, is_admin):

        if not is_admin:
            raise UnauthorizedError(
                "Only admin can resolve service requests."
            )

        request = self.search_request(request_id)

        request.resolve()

        self.repository.save_requests(self.requests)

        return request

    def get_dashboard_summary(self):

        total = len(self.requests)
        open_requests = sum(
            1 for request in self.requests
            if request.status == "OPEN"
        )
        resolved_requests = sum(
            1 for request in self.requests
            if request.status == "RESOLVED"
        )

        return {
            "total": total,
            "open": open_requests,
            "resolved": resolved_requests
        }
