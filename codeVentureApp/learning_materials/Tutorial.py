class Tutorial:

    def __init__(self, tutorial_id, content):
        self.tutorial_id = tutorial_id
        self.content = content

    def get_tutorial_id(self):
        return self.tutorial_id

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def __str__(self):
        return self.content
