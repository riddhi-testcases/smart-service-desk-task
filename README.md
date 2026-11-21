# Smart Service Desk Management System

## 1. Project Overview

I developed this project as part of Hands on Assignment to manage IT support requests submitted by employees in an organization.

Earlier, service requests were maintained manually. To make this process easier, I created this Smart Service Desk Management System that allows users to create, view, search and track service requests.

I used OOP, exception handling, JSON file handling, SOLID principles and basic Domain-Driven Design (DDD) to develop this application.

I also implemented admin authentication so that only an authenticated administrator can resolve service requests.

## 2. Features Implemented

I implemented the following features:

1. **Create Service Request:** Users can enter Request ID, Employee Name, Issue Description and Priority.
2. **Duplicate Request Validation:** The system does not allow two requests with the same Request ID.
3. **View All Requests:** Displays all saved requests with their details and status.
4. **Search Request:** Allows searching for a request using its Request ID.
5. **Resolve Request:** Only an authenticated admin can resolve an open request.
6. **Admin Authentication:** Admin login is required before resolving a request.
7. **Dashboard Summary:** Displays total requests, open requests and resolved requests.
8. **JSON Persistence:** All requests are stored in a JSON file and remain available after restarting the application.
9. **Exception Handling:** Custom exceptions handle duplicate IDs, invalid priorities, missing requests, already resolved requests and unauthorized access.

### Admin Login Credentials

- Username: riddhi
- Password: riddhi123


## 3. Technologies Used

- Python
- JSON
- Object-Oriented Programming
- Git and GitHub
- VS Code

## 4. Project Folder Structure

```text
smart-service-desk/
│
├── domain/
│   ├── __init__.py
│   ├── service_request.py
│   └── exceptions.py
│
├── application/
│   ├── __init__.py
│   ├── request_service.py
│   └── auth_service.py
│
├── infrastructure/
│   ├── __init__.py
│   └── file_repository.py
│
├── data/
│   └── requests.json
│
├── main.py
├── README.md
└── .gitignore
```

## 5. Implementation Process (Step by Step)

### Step 1: Project Setup

First, I created the main project folder named `smart-service-desk`.

I separated the application into three main layers: Domain, Application and Infrastructure.

I also created the data folder to store the JSON file and added the main.py file as the starting point of the application.

### Step 2: Created Custom Exceptions

I created `domain/exceptions.py` to define custom exceptions.

I implemented:
- DuplicateRequestError
- RequestNotFoundError
- InvalidPriorityError
- AlreadyResolvedError
- UnauthorizedError

These exceptions help display meaningful error messages instead of allowing the application to terminate unexpectedly.

### Step 3: Implemented the ServiceRequest Class

Next, I created `domain/service_request.py`.

I implemented the ServiceRequest class with the following attributes:

- request_id
- employee_name
- issue
- priority
- status

I used a constructor to initialize the request details.

I added priority validation to allow only LOW, MEDIUM and HIGH.

The status is automatically initialized as OPEN.

I also implemented the resolve() method to change the status from OPEN to RESOLVED.

Additionally, I created to_dict() and from_dict() methods to convert between Python objects and dictionaries for JSON persistence.

### Step 4: Implemented JSON File Handling

I created `infrastructure/file_repository.py`.

Here, I implemented the FileRepository class with two main methods:

- load_requests(): Reads the JSON file and converts the stored data into ServiceRequest objects.
- save_requests(): Converts the request objects into dictionaries and saves them in JSON format.

I also handled missing and empty JSON files so that the application can start safely.

### Step 5: Implemented Admin Authentication

I created `application/auth_service.py`.

I implemented an AuthService class to verify the admin's username and password.

The application checks the admin credentials before allowing a service request to be resolved.

### Step 6: Implemented RequestService

I created `application/request_service.py` to handle the main application operations.

Implemented:

- create_request()
- view_requests()
- search_request()
- resolve_request()
- get_dashboard_summary()

I connected the RequestService with the FileRepository through dependency injection.

I also implemented duplicate Request ID validation and checked admin authorization before resolving a request.

### Step 7: Developed the Main Menu

Next implemented `main.py` to handle user interaction.

I created a menu-driven interface that allows users to:

1. Create Service Request
2. View All Requests
3. Search Request
4. Dashboard Summary
5. Resolve Request (Admin Only)
6. Exit

I used functions to keep the menu operations separate and handled custom exceptions to display friendly error messages.

### Step 8: Tested the Application

After completing the implementation, I tested the application using different scenarios.

I performed the following tests:

1. Created a service request with ID SR101 and HIGH priority.
2. Tried creating SR101 again to check duplicate ID validation.
3. Viewed all saved service requests.
4. Searched for SR101 and checked its details.
5. Logged in as admin and resolved SR101.
6. Tried resolving SR101 again to verify already-resolved handling.
7. Exited and restarted the application.
8. Searched for SR101 again and verified that its RESOLVED status was preserved.

All these core test scenarios worked successfully.

## 6. Concepts Used

### OOP

I used a ServiceRequest class to represent service requests.

I used constructors, attributes and methods to organize the request data and behavior.

### Exception Handling

I created custom exceptions to handle expected errors such as duplicate requests, invalid priorities and unauthorized operations.

### File Handling

I used Python's JSON module to store and retrieve request information.

### SOLID Principles

I followed the Single Responsibility Principle by separating domain logic, application operations, file handling and user interaction.

I also followed Dependency Inversion by passing the repository object into RequestService instead of making the application service directly handle file operations.

### Domain-Driven Design

I separated the application into:

- Domain Layer: Contains business entities, validation and business rules.
- Application Layer: Contains application operations and authentication.
- Infrastructure Layer: Contains JSON file handling.
- Presentation Layer: Contains the menu and user interaction in main.py.

### Git/GitHub

I used Git for version control and maintained two branches:

- main
- development

I performed development work in the development branch, committed changes in multiple stages, tested the application and merged the development branch into main.

## 7. How to Run the Application

## 8. Git Branching and Merging Process

I used the development branch for implementing the application.

Created separate commits for the project structure, domain model, JSON repository, application services and CLI implementation.

After completing and testing the application, I merged the development branch into main.

The final working version is maintained in the main branch.

## 9. Conclusion

Through this project, I implemented a simple Smart Service Desk Management System using Python.

I learned how to structure an application using basic DDD, implement OOP concepts, handle exceptions, store information using JSON and maintain code using Git branches and commits.

The application successfully supports service request creation, viewing, searching, admin-only resolution and persistent storage.
