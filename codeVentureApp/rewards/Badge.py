class Badge:
    """
    Badge class
    """
    def __init__(self, badge_name, description,date=None):
        """
        Constructor
        """
        self.badge_name = badge_name
        self.description = description
        self.date_earned = date

    def get_badge_name(self):
        """
        Get badge name
        """
        return self.badge_name

    def get_description(self):
        """
        Get description of the badge
        """
        return self.description

    def get_date_earned(self):
        """
        Get date earned
        """
        return self.date_earned

    def __str__(self):
        """
        To string method
        """
        return (f"Badge name: {self.get_badge_name()}\n"
                f"Description: {self.get_description()}\n"
                f"Date earned: {self.get_date_earned()}")
