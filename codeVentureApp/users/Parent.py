from codeVentureApp.users.UserAccount import UserAccount


class Parent(UserAccount):
    """
    Parent class that extends the UserAccount class, representing the account for parents.
    """
    def __init__(self, username, password, firstname, lastname, ques, ans):
        """
        Init method for Parent class
        :param username: account username
        :param password: account password
        :param firstname: parent's first name
        :param lastname: parent's last name
        :param child_username: child of the parent
        """
        super().__init__(username, password, firstname, lastname, "Parent")
        self.child_username = None
        self.ques = ques
        self.ans = ans

    def view_child_progress(self):
        """
        Method to view the progress of the child associated with the parent
        """
        if self.child_username:
            print(f"Viewing progress for child with username: {self.child_username}")
            # Implement code to display the child's progress here
        else:
            print("No child associated with this account.")

    def __str__(self):
        """
        String method to print the object details
        :return: string of user's fullname, username and child's username
        """
        return f"Parent's full name: {self.firstname} {self.lastname}\n" \
               f"Parent's username : {self.username}\n" \
               f"Child's username : {self.child_username}\n"
