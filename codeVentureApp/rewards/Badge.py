from utilities.DateValidator import *


class Badge:
    def __init__(self, badge_name, description,date=None):
        self.badge_name = badge_name
        self.description = description
        self.date_earned = date

    def get_badge_name(self):
        return self.badge_name

    def get_description(self):
        return self.description

    def get_date_earned(self):
        return self.date_earned

    def set_date_earned(self, date):
        self.date_earned = date

    def __str__(self):
        return (f"Badge name: {self.get_badge_name()}\n"
                f"Description: {self.get_description()}\n"
                f"Date earned: {self.get_date_earned()}")
