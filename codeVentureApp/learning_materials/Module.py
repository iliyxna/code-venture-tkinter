from codeVentureApp.rewards.Points import Points
from codeVentureApp.utilities.Status import Status


class Module:
    def __init__(self, id, educator, module_name, intro, award_points, tutorial_id, module_level):
        self.module_name = module_name
        self.id = id
        self.educator = educator
        self.intro = intro
        self.award_points = Points(award_points)
        self.tutorial_id = tutorial_id

        self.completion_status = Status.NOT_STARTED
        self.discussion_forum = None
        self.module_level = module_level

    def get_module_id(self):
        return self.id

    def get_module_name(self):
        return self.module_name

    def get_intro(self):
        return self.intro

    def get_award_points(self):
        return self.award_points

    def get_tutorial_id(self):
        return self.tutorial_id

    def get_quizzes(self):
        return self.quizzes

    def get_status(self):
        return self.completion_status

    def get_level(self):
        return self.module_level

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

    def mark_complete(self):
        self.completion_status = Status.COMPLETED

    def __str__(self):
        return (f"Module name: {self.get_module_name()}\n"
                f"Completion status: {self.get_status()}\n"
                f"Difficulty: {self.get_level()}\n")
