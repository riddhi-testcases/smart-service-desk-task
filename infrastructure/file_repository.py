
import json
import os

from domain.service_request import ServiceRequest


class FileRepository:

    def __init__(self, file_path="data/requests.json"):
        self.file_path = file_path

        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump([], file)

    def load_requests(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)

                if not isinstance(data, list):
                    raise ValueError("Invalid JSON data format")

                return [
                    ServiceRequest.from_dict(item)
                    for item in data
                ]

        except json.JSONDecodeError:
            return []

    def save_requests(self, requests):
        data = [request.to_dict() for request in requests]

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
