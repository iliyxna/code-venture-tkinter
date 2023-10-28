class Challenge:

    def __init__(self, challenge_id, challenge_name, intro, difficulty,question , solution):
        self.challenge_id = challenge_id
        self.challenge_name = challenge_name
        self.intro = intro
        self.difficulty = difficulty
        self.question = question
        self.solution = solution

    # def __init__(self, challenge_id, difficulty, question, solution, badge_award, score, points_to_unlock=0):
    #     self.challenge_id = challenge_id
    #     self.difficulty = difficulty
    #     self.question = question
    #     self.badge_award = badge_award
    #     self.score = score
    #     self.points_to_unlock = points_to_unlock
    #     self.solution = solution

    def get_challenge_id(self):
        return self.challenge_id

    def get_question(self):
        return self.question

    def get_solution(self):
        return self.solution

    # def get_badge_award(self):
    #     return self.badge_award
    #
    # def get_score(self):
    #     return self.score
    #
    # def get_points_to_unlock(self):
    #     return self.points_to_unlock

    def get_difficulty(self):
        return self.difficulty

    def get_challenge_name(self):
        return self.challenge_name

    def get_intro(self):
        return self.intro

    # def set_difficulty(self, difficulty):
    #     self.difficulty = difficulty

    # def set_badge_award(self, badge):
    #     self.badge_award = badge
