class Tutorial:

    def __init__(self, tutorial_id, c1, c2, c3, i1, i2, quiz_one, quiz_two, quiz_three):
        self.tutorial_id = tutorial_id
        self.content = c1
        self.content_two = c2
        self.content_three = c3
        self.image_one = i1
        self.image_two = i2
        # self.image_name = image_name
        self.quiz_one = quiz_one
        self.quiz_two = quiz_two
        self.quiz_three = quiz_three

    def get_tutorial_id(self):
        return self.tutorial_id

    def get_i1(self):
        return self.image_one

    def get_i2(self):
        return self.image_two

    def get_quiz_one(self):
        return self.quiz_one

    def get_quiz_two(self):
        return self.quiz_two

    def get_quiz_three(self):
        return self.quiz_three

    def get_c1(self):
        return self.content

    def get_c2(self):
        return self.content_two

    def get_c3(self):
        return self.content_three

    def __str__(self):
        return self.content
