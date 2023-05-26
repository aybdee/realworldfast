import enum


class UserError(enum.Enum):
    EmailUsed = "This email is already used"
    UsernameUsed = "This username is already used"
    EmailNotExist = "This email does not exist"
    PasswordIncorrect = "Password Incorrect"


class UserException(Exception):
    def __init__(self, error: UserError):
        self.message = error.value


class ProfileError(enum.Enum):
    AlreadyFollowed = "you are already following this person"
    NotFollowing = "you are not following this person"
        
class ProfileException(Exception):
    def __init__(self, error: ProfileError):
        self.message = error.value

class ArticleError(enum.Enum):
    ArticleNotExist = "this article does not exist"
    NotAllowedToEdit = "you are not allowed to edit this article"

    
class ArticleException(Exception):
    def __init__(self, error: ArticleError):
        self.message = error.value
