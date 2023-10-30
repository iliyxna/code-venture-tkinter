class Module:
    def __init__(self, id, educator, module_name, intro, award_points, tutorial_id, module_level):
        self.module_name = module_name
        self.id = id
        self.educator = educator
        self.intro = intro
        self.tutorial_id = tutorial_id
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

    def get_level(self):
        return self.module_level

    def __str__(self):
        return (f"Module name: {self.get_module_name()}\n"
                f"Difficulty: {self.get_level()}\n")
