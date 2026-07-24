class UserAlreadyExistsException(Exception):
    def __init__(self, email: str):
        self.email = email
        self.message = f"User with email '{email}' already exists"
        super().__init__(self.message)


class InvalidCredentialsException(Exception):
    def __init__(self):
        self.message = "Invalid email or password"
        super().__init__(self.message)