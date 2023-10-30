from codeVentureApp.users.Educator import Educator
from codeVentureApp.users.Learner import Learner
from codeVentureApp.users.Parent import Parent
from codeVentureApp.users.UserAccount import UserAccount


class Administrator(UserAccount):
    """
    Admin class
    """
    def __init__(self, username, password, firstname, lastname, ques, ans):
        """
        Constructor
        """
        super().__init__(username, password, firstname, lastname, "Admin")
        self.permissions = []
        self.ques = ques
        self.ans = ans
