class Challenge:
    """
    Class for challenge
    """

    def __init__(self, challenge_id, challenge_name, intro, difficulty,question , solution, badge_award):
        """
        Constructor
        """
        self.challenge_id = challenge_id
        self.challenge_name = challenge_name
        self.intro = intro
        self.difficulty = difficulty
        self.question = question
        self.solution = solution
        self.badge_award = badge_award

    def get_challenge_id(self):
        """
        Get challenge id
        """
        return self.challenge_id

    def get_question(self):
        """
        Get question
        """
        return self.question

    def get_solution(self):
        """
        Get solution
        """
        return self.solution

    def get_badge_award(self):
        """
        Get badge
        """
        return self.badge_award

    def get_difficulty(self):
        """
        Get difficulty
        """
        return self.difficulty

    def get_challenge_name(self):
        """
        Get challenge
        """
        return self.challenge_name

    def get_intro(self):
        """
        Get intro
        """
        return self.intro

