import customtkinter

import LoginSystem
from learning_materials.ChallengeManager import ChallengeManager
from learning_materials.ModuleManager import ModuleManager
from users.UserAccount import UserAccount
from utilities.Role import *
from utilities.Rank import *
from rewards.Points import Points
from utilities.ProgressTracker import ProgressTracker

from tkinter import messagebox


class LearnerFrame(customtkinter.CTkFrame):
    def __init__(self, master, parent, user):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        self.master = master
        self.parent = parent
        self.user = user

        welcome_title = customtkinter.CTkLabel(master=self,
                                               text=f'Welcome Back, {self.user.get_firstname()}!',
                                               font=("Fixedsys", 20))
        welcome_title.grid(row=1, columnspan=2, padx=10, pady=10)

        learner_frame_title = customtkinter.CTkLabel(master=self,
                                                     text="Learner Dashboard",
                                                     font=("Fixedsys", 20))
        learner_frame_title.grid(row=2, columnspan=2, padx=10, pady=10)

        logout = customtkinter.CTkButton(master=self, text="Logout", command=self.confirm_logout)
        logout.grid(row=5, columnspan=2, padx=5, pady=10)
        print(f"User in LearnerFrame: {self.user}")

    def back_to_login(self):
        self.master.switch_frame(self.master.login_frame)

    def confirm_logout(self):
        result = messagebox.askyesno("Logout Confirmation", "Are you sure you want to sign out?")
        if result:
            self.back_to_login()


class Learner(UserAccount):
    """
    Learner class that extends the UserAccount class, representing the account for young learners.
    """

    def __init__(self, username, password, firstname, lastname):
        """
        Init method for Learner class
        :param username: account username
        :param password: account password
        :param firstname: learner's first name
        :param lastname: learner's last name
        """
        super().__init__(username, password, firstname, lastname, "Learner")
        self.points = Points(0)
        self.rank = Rank.NOVICE
        self.progress = ProgressTracker(self.get_rank())
        self.module_manager = ModuleManager()
        self.challenge_manager = ChallengeManager()

    def get_points(self):
        """
        Getter method for user points
        :return: the number of points the user has
        """
        return self.points.get_point_value()

    def get_rank(self):
        """
        Getter method for user rank
        :return: the current rank of the user
        """
        return self.rank

    def get_progress_tracker(self):
        """
        Getter method for the progress tracker of the user
        :return: the progress tracker of the user
        """
        return self.progress

    def get_module_manager(self):
        """
        :return:
        """
        return self.module_manager

    def get_challenge_manager(self):
        """
        :return:
        """
        return self.challenge_manager

    def update_progress(self, module=None, challenge=None):
        """
        Update the learner's progress when they complete a module.
        :param challenge:
        :param module: The completed module
        """
        if module is not None:
            self.get_progress_tracker().update_completed_modules(module)
        if challenge is not None:
            self.get_progress_tracker().update_completed_challenges(challenge)
        self.get_progress_tracker().update_rank()

    def display_progress(self):
        """
        Display the learner's progress.
        """
        progress_tracker = self.get_progress_tracker()
        return progress_tracker

    def __str__(self):
        """
        String method to print the object details
        :return: string of user's fullname and username
        """
        return f"Learner's full name: {self.get_firstname()} {self.get_lastname()}\n" \
               f"Learner's username : {self.get_firstname()}\n" \
               f"Current Rank: {self.get_rank().name}\n" \
               f"Current Points: {self.get_points()}\n"
