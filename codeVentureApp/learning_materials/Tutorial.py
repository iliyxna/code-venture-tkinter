class Tutorial:
    """
    Class for Tutorial
    """

    def __init__(self, tutorial_id, c1, c2, c3, i1, i2, quiz_one, quiz_two, quiz_three):
        """
        Constructor
        """
        self.tutorial_id = tutorial_id
        self.content = c1
        self.content_two = c2
        self.content_three = c3
        self.image_one = i1
        self.image_two = i2

        self.quiz_one = quiz_one
        self.quiz_two = quiz_two
        self.quiz_three = quiz_three

    def get_tutorial_id(self):
        """
        Method to get tutorial id
        """
        return self.tutorial_id

    def get_i1(self):
        """
        Method to get image 1
        """
        return self.image_one

    def get_i2(self):
        """
        Method to get image 2
        """
        return self.image_two

    def get_quiz_one(self):
        """
        Method to get quiz 1
        """
        return self.quiz_one

    def get_quiz_two(self):
        """
        Method to get quiz 2
        """
        return self.quiz_two

    def get_quiz_three(self):
        """
        Method to get quiz 3
        """
        return self.quiz_three

    def get_c1(self):
        """
        Method to get content 1
        """
        return self.content

    def get_c2(self):
        """
        Method to get content 2
        """
        return self.content_two

    def get_c3(self):
        """
        Method to get content 3
        """
        return self.content_three

    def __str__(self):
        """
        To String method
        """
        return self.content
