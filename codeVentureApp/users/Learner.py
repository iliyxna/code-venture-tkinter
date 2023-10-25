from codeVentureApp.learning_materials.ChallengeManager import ChallengeManager
from codeVentureApp.learning_materials.ModuleManager import ModuleManager
from codeVentureApp.rewards.Points import Points
from codeVentureApp.users.UserAccount import UserAccount
from codeVentureApp.utilities.ProgressTracker import ProgressTracker
from codeVentureApp.utilities.Rank import Rank


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
        self.percentage_completion = 0.0

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

    def get_percentage_completion(self):
        return self.get_progress_tracker().calculate_progress_percentage()

    def __str__(self):
        """
        String method to print the object details
        :return: string of user's fullname and username
        """
        return f"Learner's full name: {self.get_firstname()} {self.get_lastname()}\n" \
               f"Learner's username : {self.get_firstname()}\n" \
               f"Current Rank: {self.get_rank().name}\n" \
               f"Current Points: {self.get_points()}\n"

    def get_learner(self):
        return self

