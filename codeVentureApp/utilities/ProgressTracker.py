from codeVentureApp.learning_materials.ChallengeManager import ChallengeManager
from codeVentureApp.learning_materials.ModuleManager import ModuleManager
from codeVentureApp.utilities.Rank import Rank


class ProgressTracker:

    def __init__(self, rank):
        self.badges_earned = []
        self.modules_completed = []
        self.module_manager = ModuleManager()
        self.challenge_completed = []
        self.challenge_manager = ChallengeManager()
        self.rank = rank
        self.recommended_modules = []

    def get_rank(self):
        return self.rank

    def get_badges_earned(self):
        return self.badges_earned

    def get_modules_completed(self):
        return self.modules_completed

    def get_challenges_completed(self):
        return self.challenge_completed

    def update_badges_earned(self, badge):
        self.badges_earned.append(badge)

    def update_completed_modules(self, module):
        self.modules_completed.append(module)

    def update_completed_challenges(self, module):
        self.challenge_completed.append(module)

    def calculate_progress_percentage(self):
        total_modules = len(self.module_manager.get_all_modules())
        completed_modules = len(self.modules_completed)
        if total_modules == 0:
            return 0
        return (completed_modules / total_modules) * 100

    def display_progress(self):
        progress_percentage = self.calculate_progress_percentage()
        return f"Your progress of module completion is {progress_percentage:.2f}% Keep going!"

    def update_rank(self):
        progress_percentage = self.calculate_progress_percentage()

        if progress_percentage >= 80:
            self.rank = Rank.EXPERT
        elif progress_percentage >= 40:
            self.rank = Rank.INTERMEDIATE
        else:
            self.rank = Rank.NOVICE

    def show_completed_modules(self):
        modules = ""
        if len(self.get_modules_completed()) > 0:
            modules += "\n"
            for module in self.get_modules_completed():
                modules += f'{module.get_module_name()}\n'
        else:
            modules = "No completed modules.\n"
        return modules

    def show_enrolled_modules(self):
        modules = ""
        if len(self.get_modules_completed()) > 0:
            modules += "\n"
            for module in self.get_modules_completed():
                modules += f'{module.get_module_name()}\n'
        else:
            modules = "No modules enrolled.\n"
        return modules

    def show_badges(self):
        badges = ""
        if len(self.get_badges_earned()) > 0:
            badges += "\n"
            for badge in self.get_badges_earned():
                badges += f'{badge}\n'
        else:
            badges = "No badges earned yet. Take part in challenges to earn new badges!\n"
        return badges

    def __str__(self):
        return (f"Current rank: {self.get_rank().name}\n"
                f"Badges earned: {self.show_badges()}\n"
                f"Modules completed: {self.show_completed_modules()}\n"
                f"{self.display_progress()}")
