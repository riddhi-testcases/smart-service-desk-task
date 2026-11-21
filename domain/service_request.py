
from domain.exceptions import InvalidPriorityError, AlreadyResolvedError


class ServiceRequest:

    ALLOWED_PRIORITIES = ["LOW", "MEDIUM", "HIGH"]

    def __init__(self, request_id, employee_name, issue, priority):
        priority = priority.upper()

        if priority not in self.ALLOWED_PRIORITIES:
            raise InvalidPriorityError(
                "Priority must be LOW, MEDIUM or HIGH"
            )

        self.request_id = request_id
        self.employee_name = employee_name
        self.issue = issue
        self.priority = priority
        self.status = "OPEN"

    def resolve(self):
        if self.status == "RESOLVED":
            raise AlreadyResolvedError(
                "This request is already resolved."
            )

        self.status = "RESOLVED"

    def to_dict(self):
        return {
            "request_id": self.request_id,
            "employee_name": self.employee_name,
            "issue": self.issue,
            "priority": self.priority,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        request = cls(
            data["request_id"],
            data["employee_name"],
            data["issue"],
            data["priority"]
        )

        request.status = data["status"]
        return request
