class Quiz:

    def __init__(self, quiz_id, question, solution, choice_one, choice_two, choice_three, choice_four):
        self.quiz_id = quiz_id
        self.questions = question
        self.solution = solution
        self.choice_one = choice_one
        self.choice_two = choice_two
        self.choice_three = choice_three
        self.choice_four = choice_four

    def get_quiz_id(self):
        return self.quiz_id

    def get_questions(self):
        return self.questions

    def get_solution(self):
        return self.solution

    def get_choice_one(self):
        return self.choice_one

    def get_choice_two(self):
        return self.choice_two

    def get_choice_three(self):
        return self.choice_three

    def get_choice_four(self):
        return self.choice_four
