from codeVentureApp.users.UserAccount import UserAccount
from codeVentureApp.utilities.Role import Role


class Educator(UserAccount):
    """
    Educator class that extends the UserAccount class, representing the account for educators.
    """

    def __init__(self, username, password, firstname, lastname):
        """
        Init method for Educator class
        :param username: account username
        :param password: account password
        :param firstname: educator's first name
        :param lastname: educator's last name
        """
        super().__init__(username, password, firstname, lastname, Role.EDUCATOR)
        self.students = []
        self.modules = []

    def add_modules(self, module):
        """
        Add module to the educator's list of modules.
        """
        self.modules.append(module)

    def add_student(self, student):
        """
        Add student to the educator's list of students.
        """
        self.students.append(student)

    def view_student_progress(self, student_username):
        """
        View the progress of a specific student.
        """
        for student in self.students:
            if student.username == student_username:
                # Implement code to display the student's progress
                print(f"Viewing progress of {student_username}")
                return
        print(f"Student {student_username} not found.")

    def view_class_progress(self):
        """
        View an overview of the class or group's progress.
        """
        print("Class Progress Overview:")
        for student in self.students:
            # Implement code to display an overview of each student's progress
            print(f"{student.username}: Progress overview")

    def __str__(self):
        """
        String method to print the object details
        :return: string of user's fullname and username
        """

        student_list = ""
        if len(self.students) == 0:
            student_list = "No students yet."
        else:
            for student in self.students:
                student_list += f'{student.get_fullname()}\n'

        return f"Educator's full name: {self.firstname} {self.lastname}\n" \
               f"Educator's username : {self.username}\n" \
               f"Current students: \n\n{student_list}"

    @staticmethod
    def educator_menu():
        """
        Prints the menu options for the educator user
        """
        print("You have the following options:")
        print("\t1. View profile")
        print("\t2. View modules")
        print("\t3. View student progress")
        print("\t4. View class progress")
        print("\t5. Add personalised support")
        print("\t6. Log out\n")

    @staticmethod
    def educator_main(user):
        while True:
            Educator.educator_menu()
            print()
            user_input = input("Please enter a menu option: ")
            if user_input == "1":
                print(user)
            elif user_input == "2":
                print("Viewing modules...")
            elif user_input == "3":
                print("Viewing student progress...")
            elif user_input == "4":
                print("Viewing class progress...")
            elif user_input == "5":
                print("Add Personalised support...")
            elif user_input == "6":
                # Log out
                print("Logging out...")
                break
            else:
                print("You have not entered a valid menu option. Please try again.\n")

        print("Thank you for using the CodeVenture")
        print("Hope to see you again soon.")
