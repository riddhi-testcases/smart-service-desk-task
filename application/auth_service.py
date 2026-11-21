
class AuthService:

    ADMIN_USERNAME = "riddhi"
    ADMIN_PASSWORD = "riddhi123"

    def authenticate(self, username, password):
        if (
            username == self.ADMIN_USERNAME
            and password == self.ADMIN_PASSWORD
        ):
            return True

        return False
