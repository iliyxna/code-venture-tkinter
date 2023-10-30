from codeVentureApp.users.UserAccount import UserAccount
from codeVentureApp.utilities.ProgressTracker import ProgressTracker
from codeVentureApp.utilities.Rank import Rank


class Learner(UserAccount):
    """
    Learner class that extends the UserAccount class, representing the account for young learners.
    """
    def __init__(self, username, password, firstname, lastname, ques, ans):
        """
        Init method for Learner class
        :param username: account username
        :param password: account password
        :param firstname: learner's first name
        :param lastname: learner's last name
        """
        super().__init__(username, password, firstname, lastname, "Learner")
        self.rank = Rank.NOVICE
        self.progress = ProgressTracker(self.get_rank())
        self.percentage_completion = 0.0
        self.current_module_score = 0
        self.answered_count = 0
        self.ques = ques
        self.ans = ans

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
        """
        Get
        """
        return self.get_progress_tracker().calculate_progress_percentage()

    def get_current_module_score(self):
        """
        Get current module score
        """
        return self.current_module_score

    def increment_score(self):
        """
        Increment the score by one
        """
        self.current_module_score += 1

    def get_answered_count(self):
        """
        Method to get the number of answered questions
        """
        return self.answered_count

    def increment_answered(self):
        """
        Method to increment the number of answered questions
        """
        self.answered_count += 1

    def __str__(self):
        """
        String method to print the object details
        :return: string of user's fullname and username
        """
        return f"Learner's full name: {self.get_firstname()} {self.get_lastname()}\n" \
               f"Learner's username : {self.get_username()}\n" \
               f"Current Rank: {self.get_rank().name}\n" \
               f"Current Points: {self.get_points()}\n"

    def get_learner(self):
        return self

