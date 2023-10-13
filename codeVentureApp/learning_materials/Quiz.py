class Quiz:

    def __init__(self, quiz_id, questions, score=0, solution=None):
        self.quiz_id = quiz_id
        self.questions = questions
        self.score = score
        self.solution = solution

    def get_quiz_id(self):
        return self.quiz_id

    def get_questions(self):
        return self.questions

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def add_question(self, question):
        self.questions.append(question)

