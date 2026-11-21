
from infrastructure.file_repository import FileRepository
from application.request_service import RequestService
from application.auth_service import AuthService

from domain.exceptions import (
    DuplicateRequestError,
    RequestNotFoundError,
    InvalidPriorityError,
    AlreadyResolvedError,
    UnauthorizedError
)


def display_menu():
    print("\n========== SMART SERVICE DESK SYSTEM ==========")
    print("1. Create Service Request")
    print("2. View All Requests")
    print("3. Search Request")
    print("4. Dashboard Summary")
    print("5. Resolve Request (Admin Only)")
    print("6. Exit")
    print("===============================================")


def create_request(service):
    request_id = input("Enter Request ID: ").strip()
    employee_name = input("Enter Employee Name: ").strip()
    issue = input("Enter Issue: ").strip()
    priority = input("Enter Priority (LOW/MEDIUM/HIGH): ").strip()

    if not request_id or not employee_name or not issue:
        print("All fields are required.")
        return

    request = service.create_request(
        request_id,
        employee_name,
        issue,
        priority
    )

    print("\nService Request created successfully.")
    print(f"Request ID: {request.request_id}")


def view_requests(service):
    requests = service.view_requests()

    if not requests:
        print("\nNo service requests available.")
        return

    print("\n========== ALL SERVICE REQUESTS ==========")

    for request in requests:
        print(
            f"{request.request_id} | "
            f"{request.employee_name} | "
            f"{request.issue} | "
            f"{request.priority} | "
            f"{request.status}"
        )


def search_request(service):
    request_id = input("Enter Request ID to search: ").strip()

    request = service.search_request(request_id)

    print("\n========== REQUEST DETAILS ==========")
    print(f"Request ID: {request.request_id}")
    print(f"Employee Name: {request.employee_name}")
    print(f"Issue: {request.issue}")
    print(f"Priority: {request.priority}")
    print(f"Status: {request.status}")


def dashboard(service):
    summary = service.get_dashboard_summary()

    print("\n========== DASHBOARD SUMMARY ==========")
    print(f"Total Requests: {summary['total']}")
    print(f"Open Requests: {summary['open']}")
    print(f"Resolved Requests: {summary['resolved']}")


def resolve_request(service, auth_service):
    print("\n========== ADMIN LOGIN ==========")

    username = input("Enter Admin Username: ").strip()
    password = input("Enter Admin Password: ").strip()

    is_admin = auth_service.authenticate(username, password)

    if not is_admin:
        raise UnauthorizedError("Invalid admin username or password.")

    print("\nAdmin login successful.")

    request_id = input("Enter Request ID to resolve: ").strip()

    request = service.resolve_request(request_id, is_admin)

    print(
        f"\nRequest {request.request_id} "
        "has been successfully resolved."
    )


def main():
    repository = FileRepository()
    service = RequestService(repository)
    auth_service = AuthService()

    print("\nWelcome to Smart Service Desk Management System!")

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                create_request(service)

            elif choice == 2:
                view_requests(service)

            elif choice == 3:
                search_request(service)

            elif choice == 4:
                dashboard(service)

            elif choice == 5:
                resolve_request(service, auth_service)

            elif choice == 6:
                print("\nThank you for using Smart Service Desk!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except DuplicateRequestError as error:
            print(f"Error: {error}")

        except RequestNotFoundError as error:
            print(f"Error: {error}")

        except InvalidPriorityError as error:
            print(f"Error: {error}")

        except AlreadyResolvedError as error:
            print(f"Error: {error}")

        except UnauthorizedError as error:
            print(f"Access Denied: {error}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
