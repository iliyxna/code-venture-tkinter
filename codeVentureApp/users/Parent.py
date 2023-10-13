from users.UserAccount import UserAccount
from utilities.Role import *


class Parent(UserAccount):
    """
    Parent class that extends the UserAccount class, representing the account for parents.
    """

    def __init__(self, username, password, firstname, lastname, child_username):
        """
        Init method for Parent class
        :param username: account username
        :param password: account password
        :param firstname: parent's first name
        :param lastname: parents's last name
        :param child_username: child of the parent
        """
        super().__init__(username, password, firstname, lastname, Role.PARENT)
        self.child_username = child_username

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

    @staticmethod
    def parent_menu():
        """
        Prints the menu options for the parent user
        """
        print("You have the following options:")
        print("\t1. View profile")
        print("\t2. View child progress")
        print("\t3. View child modules")
        print("\t4. Log out\n")

    @staticmethod
    def parent_main(user):
        while True:
            Parent.parent_menu()
            print()
            user_input = input("Please enter a menu option: ")
            if user_input == "1":
                print(user)
            elif user_input == "2":
                print("Viewing child progress...")
            elif user_input == "3":
                print("Viewing child modules...")
            elif user_input == "4":
                # Log out
                print("Logging out...")
                break
            else:
                print("You have not entered a valid menu option. Please try again.\n")

        print("Thank you for using the CodeVenture")
        print("Hope to see you again soon.")

