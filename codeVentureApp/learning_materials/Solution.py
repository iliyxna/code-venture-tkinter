class Solution:
    def __init__(self, solution_id, solution):
        self.solution_id = solution_id
        self.solution = solution

    def get_solution_id(self):
        return self.solution_id

    def get_solution(self):
        return self.solution

    def __str__(self):
        return self.solution