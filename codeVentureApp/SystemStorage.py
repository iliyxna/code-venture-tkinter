from typing import List

from users.UserAccount import UserAccount


class SystemStorage:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SystemStorage, cls).__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def __init__(self, file_path="C:/Users/User/PycharmProjects/codeVentureApp/user_details"):
        # Initialize storage attributes here
        self.file_path = file_path
        self.users: List[UserAccount] = []
        self.existing_usernames = []
        self.pending_admin_registration = []
        self.all_modules = []
        self.all_challenges = []
        self.load_users()

    def load_users(self):
        """
        Load list of users from the ./data/UserDetails.txt file
        :return: bool (True if successful, False otherwise)
        """
        try:
            with open(self.file_path, "r", encoding="utf8") as users_f:
                users_lines = users_f.readlines()
                for line in users_lines:
                    (username,
                     password,
                     firstname,
                     lastname,
                     role
                     ) = line.strip().split(",")
                    user_obj = UserAccount(username=username,
                                           password=password,
                                           firstname=firstname,
                                           lastname=lastname,
                                           role=role)
                    self.users.append(user_obj)
            return True
        except FileNotFoundError:
            print(f"The file \"{self.file_path}\" does not exist!")
            return False

    def check_existing_username(self, user):
        existing_usernames = []
        try:
            with open(self.file_path, "r", encoding="utf8") as users_f:
                users_lines = users_f.readlines()
                for line in users_lines:
                    (username,
                     password,
                     firstname,
                     lastname,
                     role
                     ) = line.strip().split(",")

                    existing_usernames.append(username)

            if user in existing_usernames:
                return True
            else:
                return False

        except FileNotFoundError:
            print(f"The file \"{self.file_path}\" does not exist!")
            return False

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def update_user_password(self, username, new_password):
        """
        This function is used to update the user password to the system storage.
        :param username: user's username
        :param new_password: user
        :return:
        """
        for user in self.users:
            if user.username == username:
                user.set_password(new_password)

        # Update the text file with the new password
        with open(self.file_path, "w", encoding="utf8") as users_f:
            for user in self.users:
                users_f.write(
                    f"{user.username},{user.password},{user.firstname},{user.lastname},{user.role}\n"
                )
