class Points:

    def __init__(self, value):
        self.point_value = value  # initial value for each learner will be 0

    def get_point_value(self):
        return self.point_value

    def add_points(self, points):
        self.point_value += points

    def minus_points(self, points):
        self.point_value -= points

