class CompletedChallenge:
    """
    Class for challenges that have been completed by user
    """

    def __init__(self, challenge_id, user, badge_name, completion_date):
        """
        Constructor
        """
        self.challenge_id = challenge_id
        self.user = user
        self.badge_name = badge_name
        self.completion_date = completion_date

    def get_challenge_id(self):
        """
        Method to get challenge id
        """
        return self.challenge_id

    def get_user(self):
        """
        Method to get user who completed the challenge
        """
        return self.user

    def get_badge_award(self):
        """
        Method to get the award user received
        """
        return self.badge_name

    def get_completion_date(self):
        """
        Method to get date of completion
        """
        return self.completion_date
