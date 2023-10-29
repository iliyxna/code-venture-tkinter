class Quiz:

    def __init__(self, quiz_id, question, solution, choice_one, choice_two, choice_three, explanation, image):
        self.quiz_id = quiz_id
        self.question = question
        self.solution = solution
        self.choice_one = choice_one
        self.choice_two = choice_two
        self.choice_three = choice_three
        self.explanation = explanation
        self.image = image

    def get_quiz_id(self):
        return self.quiz_id

    def get_question(self):
        return self.question

    def get_solution(self):
        return self.solution

    def get_choice_one(self):
        return self.choice_one

    def get_choice_two(self):
        return self.choice_two

    def get_choice_three(self):
        return self.choice_three

    def get_explanation(self):
        return self.explanation

    def get_image(self):
        return self.image