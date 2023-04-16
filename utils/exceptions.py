import enum


class UserError(enum.Enum):
    EmailUsed = "This email is already used"
    UsernameUsed = "This username is already used"
    EmailNotExist = "This email does not exist"
    PasswordIncorrect = "Password Incorrect"


class UserException(Exception):
    def __init__(self, error: UserError):
        self.message = error.value
