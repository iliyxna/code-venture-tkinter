from codeVentureApp.users.Educator import Educator
from codeVentureApp.users.Learner import Learner
from codeVentureApp.users.Parent import Parent
from codeVentureApp.users.UserAccount import UserAccount
from codeVentureApp.utilities.Role import Role


class Administrator(UserAccount):
    
    def __init__(self, username, password, firstname, lastname):
        super().__init__(username, password, firstname, lastname, "Admin")
        self.permissions = []


    # def create_user(self):
    #     first_name = input("Enter user's first name: ")
    #     last_name = input("Enter user' last name: ")
    #     username = input("Enter user's username: ")
    #     password = input("Enter user's password: ")
    #
    #     if username not in self.system_storage.existing_usernames:
    #         print("Select user's role:")
    #         print("1. Learner")
    #         print("2. Parent")
    #         print("3. Educator")
    #         print("4. Administrator")
    #
    #         role_choice = int(input("Enter the number for your role: "))
    #
    #         if role_choice == Role.LEARNER.value:
    #             user = Learner(username, password, first_name, last_name)
    #             self.system_storage.add_user(user)
    #
    #         elif role_choice == Role.PARENT.value:
    #             child = input("Enter the child's username: ")
    #             user = Parent(username, password, first_name, last_name, child)
    #             self.system_storage.add_user(user)
    #         elif role_choice == Role.EDUCATOR.value:
    #             user = Educator(first_name, last_name, username, password)
    #             self.system_storage.add_user(user)
    #         elif role_choice == Role.ADMIN.value:
    #             user = Administrator(username, password, first_name, last_name)
    #             self.system_storage.add_user(user)
    #
    #         else:
    #             print("Invalid role selection.")
    #             return
    #         self.system_storage.existing_usernames.append(username)
    #         print("User registration successful!")
    #     else:
    #         print("Username has already exist. User Registration failed.")

    @staticmethod
    def admin_menu():
        """
        Prints the menu options for the learner user
        """
        print("You have the following options:")
        print("\t1. Create new user")
        print("\t2. Reset a user's password")
        print("\t3. Modify a user's role")
        # print("\t4. Manage Admin registration")
        print("\t4. Log out\n")

    @staticmethod
    def admin_main(user):
        while True:
            Administrator.admin_menu()
            user_input = input("Please enter a menu option: ")
            if user_input == "1":
                pritn("Creating a user...")
            elif user_input == "2":
                print("Resetting a user's password...")
            elif user_input == "3":
                print("Modifying a user's role...")
            elif user_input == "4":
                # Log out
                print("Logging out...")
                break
            else:
                print("You have not entered a valid menu option. Please try again.\n")

