from abc import ABC


class UserAccount(ABC):
    """
    UserAccount class that is a parent class for all the user accounts, holding all the main attributes
    required by every role (e.g. Young Learner, Educator, Parents, Admin).
    """
    def __init__(self, username, password, firstname, lastname, role=None):
        """
        Init method for Learner class
        :param username: account username
        :param password: account password
        :param firstname: user's first name
        :param lastname: user's last name
        """
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.role = role

    def get_fullname(self):
        """
        Getter method for user's fullname
        :return: the user's full name
        """
        return f'{self.get_firstname()} {self.get_lastname()}'

    def get_username(self):
        """
        Getter method for user's username
        :return: the user's username
        """
        return self.username

    def get_password(self):
        """
        Getter method for the user's password
        :return: the user's password
        """
        return self.password

    def get_firstname(self):
        """
        Getter method for the user's first name
        :return: the user's first name
        """
        return self.firstname

    def get_lastname(self):
        """
        Getter method for the user's last name
        :return: the user's last name
        """
        return self.lastname

    def get_role(self):
        """
        Getter method for the user's role
        :return: the user's role
        """
        return self.role

    def set_username(self, username):
        """
        Setter method to set the user's username
        :param username: new username
        """
        self.username = username

    def set_password(self, password):
        """
        Setter method to set the user's password
        :param password: new password
        """
        self.password = password

