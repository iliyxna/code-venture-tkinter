class Quiz:
    """
    Class for Quiz
    """

    def __init__(self, quiz_id, question, solution, choice_one, choice_two, choice_three, explanation, image):
        """
        Constructor
        """
        self.quiz_id = quiz_id
        self.question = question
        self.solution = solution
        self.choice_one = choice_one
        self.choice_two = choice_two
        self.choice_three = choice_three
        self.explanation = explanation
        self.image = image

    def get_quiz_id(self):
        """
        Method to get quiz id
        """
        return self.quiz_id

    def get_question(self):
        """
        Method to get question
        """
        return self.question

    def get_solution(self):
        """
        Method to get solution
        """
        return self.solution

    def get_choice_one(self):
        """
        Method to get the first answer choice
        """
        return self.choice_one

    def get_choice_two(self):
        """
        Method to get the second answer choice
        """
        return self.choice_two

    def get_choice_three(self):
        """
        Method to get the third answer choice
        """
        return self.choice_three

    def get_explanation(self):
        """
        Method to get explanation
        """
        return self.explanation

    def get_image(self):
        """
        Method to get question snippet
        """
        return self.image
