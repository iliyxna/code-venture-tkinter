class Module:
    """
    Class for Module
    """
    def __init__(self, id, educator, module_name, intro, award_points, tutorial_id, difficulty):
        """
        Constructor
        """
        self.module_name = module_name
        self.id = id
        self.educator = educator
        self.intro = intro
        self.tutorial_id = tutorial_id
        self.discussion_forum = None
        self.module_level = difficulty
        # self.difficulty = difficulty

    def get_module_id(self):
        """
        Method to get the module id
        """
        return self.id

    def get_module_name(self):
        """
        Method to get module name
        """
        return self.module_name

    def get_intro(self):
        """
        Method to get the introduction of the module
        """
        return self.intro

    def get_tutorial_id(self):
        """
        Method to get the tutorial
        """
        return self.tutorial_id

    def get_level(self):
        """
        Method to get the difficulty level
        """
        return self.module_level

    def __str__(self):
        """
        To String method for module
        """
        return (f"Module name: {self.get_module_name()}\n"
                f"Difficulty: {self.get_level()}\n")
