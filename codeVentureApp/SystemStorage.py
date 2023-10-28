import sqlite3

from codeVentureApp.learning_materials.Challenge import Challenge
from codeVentureApp.learning_materials.Module import Module
from codeVentureApp.learning_materials.Tutorial import Tutorial
from codeVentureApp.users.Administrator import Administrator
from codeVentureApp.users.Educator import Educator
from codeVentureApp.users.Learner import Learner
from codeVentureApp.users.Parent import Parent


class SystemStorage:  # change to system storage later
    """
    This class is the overall system storage that stores all the data of the application
    1) Table that stores user credentials, firstname, lastname, role
    2) Table that stores the learner's current points and rank
    3) Table that stores the parent's child's usernames
    4)
    5)
    """

    def __init__(self):
        # Connect to sqlite
        self.connection = sqlite3.connect('system_storage.db')
        self.cursor = self.connection.cursor()

        self.create_user_table()

    def create_user_table(self):
        """
        Table 1
        """
        table_create_query = '''CREATE TABLE IF NOT EXISTS User_Data
                                (
                                username TEXT UNIQUE,
                                password TEXT,
                                firstname TEXT,
                                lastname TEXT,
                                role TEXT
                                )
                              '''
        # Execute the query
        self.connection.execute(table_create_query)
        self.connection.commit()

        """
        Table 2
        """
        table_create_query = '''CREATE TABLE IF NOT EXISTS Learner_Progress
                                (
                                username TEXT UNIQUE,
                                points INTEGER,
                                rank TEXT,
                                percentage_completion REAL
                                )
                                '''
        self.connection.execute(table_create_query)
        self.connection.commit()

        """
        Table 3
        """
        table_create_query = '''CREATE TABLE IF NOT EXISTS Parent_Data
                                (
                                username TEXT UNIQUE,
                                child_username TEXT UNIQUE 
                                )
                                '''
        self.connection.execute(table_create_query)
        self.connection.commit()

        """
        Table 4
        """
        table_create_query = '''CREATE TABLE IF NOT EXISTS Module_Completion_Data
                                (
                                id INTEGER PRIMARY KEY,
                                username TEXT,
                                module TEXT,
                                completion_date TEXT
                                )
                                '''
        self.connection.execute(table_create_query)
        self.connection.commit()

        """
        Table 5
        """
        table_create_query = '''CREATE TABLE IF NOT EXISTS Challenge_Completion_Data
                                (
                                id INTEGER PRIMARY KEY,
                                username TEXT,
                                badge_earned TEXT,
                                completion_date TEXT
                                )
                                '''
        self.connection.execute(table_create_query)
        self.connection.commit()

        """
        Table 6
        """
        table_create_query = '''CREATE TABLE IF NOT EXISTS All_Modules
                                (
                                id INTEGER PRIMARY KEY,
                                educator_username TEXT UNIQUE,
                                module_name TEXT UNIQUE,
                                intro TEXT,
                                award_points INTEGER,
                                tutorial_id INTEGER,
                                difficulty TEXT
                                )
                                '''
        self.connection.execute(table_create_query)
        self.connection.commit()

        """
        Table 7
        """
        table_create_query = '''CREATE TABLE IF NOT EXISTS All_Challenges
                                               (
                                               id INTEGER PRIMARY KEY,
                                               challenge_name TEXT UNIQUE,
                                               intro TEXT,
                                               difficulty TEXT,
                                               question TEXT,
                                               solution TEXT
                                               )
                                               '''
        self.connection.execute(table_create_query)
        self.connection.commit()

        """
        Table 8
        """
        table_create_query = '''CREATE TABLE IF NOT EXISTS All_Quizzes
                                                       (
                                                       id INTEGER PRIMARY KEY,
                                                       question TEXT,
                                                       solution TEXT,
                                                       choice_one TEXT,
                                                       choice_two TEXT,
                                                       choice_three TEXT,
                                                       choice_four TEXT
                                                       )
                                                       '''
        self.connection.execute(table_create_query)
        self.connection.commit()

        """
        Table 9
        """
        table_create_query = '''CREATE TABLE IF NOT EXISTS All_Tutorials
                                (
                                tute_id INTEGER UNIQUE,
                                content_one TEXT,
                                content_two TEXT,
                                content_three TEXT,
                                img_one TEXT,
                                img_two TEXT,
                                quiz_one_id INTEGER,
                                quiz_two_id INTEGER,
                                quiz_three_id INTEGER
                                )
                                '''

        self.connection.execute(table_create_query)
        self.connection.commit()

    def insert_user_data(self, user):
        """
        Query to insert user data into the User_Data and Learner_Progress table
        """
        self.cursor.execute('''
                    INSERT INTO User_Data (username, password, firstname, lastname, role)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
            user.get_username(), user.get_password(), user.get_firstname(), user.get_lastname(), user.get_role()))
        self.connection.commit()

        if user.get_role() == "Learner":
            self.cursor.execute('''
                                       INSERT INTO Learner_Progress (username, points, rank, percentage_completion)
                                       VALUES (?, ?, ?, ?)
                                    ''', (
                # new learners are set to default (0 points, NOVICE, 0% completion)
                user.get_username(), user.get_points(), user.get_rank().name, user.get_percentage_completion()))

            self.connection.commit()

    def insert_child_username(self, parent, child):
        """
        Query to link child's username to parent account
        """
        self.cursor.execute('''
                            INSERT INTO Parent_Data (username, child_username)
                            VALUES (?, ?)
                            ''', (parent.get_username(), child.get_username()))
        self.connection.commit()

    def get_user(self, username, password):
        """
        Query to get user
        """
        self.cursor.execute('SELECT * FROM User_Data WHERE username = ? AND password = ?', (username, password))
        user_data = self.cursor.fetchone()
        if user_data:
            username, password, firstname, lastname, role = user_data
            if role == "Learner":
                return Learner(username, password, firstname, lastname)
            elif role == "Parent":
                return Parent(username, password, firstname, lastname)
            elif role == "Educator":
                return Educator(username, password, firstname, lastname)
            elif role == "Admin":
                return Administrator(username, password, firstname, lastname)
        return None

    def get_user_by_username(self, username):
        """
        Query to get user only by username
        """
        self.cursor.execute('SELECT * FROM User_Data WHERE username = ?', (username,))
        user_data = self.cursor.fetchone()
        if user_data:
            username, password, firstname, lastname, role = user_data
            if role == "Learner":
                return Learner(username, password, firstname, lastname)
            elif role == "Parent":
                return Parent(username, password, firstname, lastname)
            elif role == "Educator":
                return Educator(username, password, firstname, lastname)
            elif role == "Admin":
                return Administrator(username, password, firstname, lastname)
        return None

    def update_user_password(self, username, new_password):
        """
        Query to update user password during password recovery
        """
        self.cursor.execute(
            'UPDATE User_Data SET password = ? WHERE username = ?', (new_password, username))
        self.connection.commit()

    def check_parent_child(self, parent_username):
        """
        Query to check if parent account is already linked to child account
        """
        self.cursor.execute('SELECT * FROM Parent_Data WHERE username = ?', (parent_username,))
        user_data = self.cursor.fetchone()
        if user_data:
            return True
        return False

    def get_learner_progress(self, learner_username):
        """
        Query to get the learner's progress data
        """
        self.cursor.execute('SELECT * FROM Learner_Progress WHERE username = ?', (learner_username,))
        learner_data = self.cursor.fetchone()
        if learner_data:
            username, points, rank, percentage_completion = learner_data
            return username, points, rank, percentage_completion

    def update_learner_rank(self, username, rank):
        """
        Query to update user rank
        """
        self.cursor.execute(
            'UPDATE Learner_Progress SET rank = ? WHERE username = ?', (rank, username))
        self.connection.commit()

    def update_learner_percentage(self, username, percentage):
        """
        Query to update user percentage
        """
        self.cursor.execute(
            'UPDATE Learner_Progress SET percentage_completion = ? WHERE username = ?', (percentage, username))
        self.connection.commit()

    def update_learner_points(self, username, points):
        """
        Query to update user earned points
        """
        self.cursor.execute(
            'UPDATE Learner_Progress SET points = ? WHERE username = ?', (points, username))
        self.connection.commit()

    def get_parent_data(self, parent_username):
        """
        Query to get the parent's data (parent and child username only)
        """
        self.cursor.execute('SELECT * FROM Parent_Data WHERE username = ?', (parent_username,))
        parent_data = self.cursor.fetchone()
        if parent_data:
            parent_username, child_username = parent_data
            return parent_username, child_username
        return None

    def get_module_data(self, id):
        """
        Query to get the module data
        """
        self.cursor.execute('SELECT * FROM All_Modules WHERE id = ?', (id,))
        data = self.cursor.fetchone()
        if data:
            module_id, educator_username, module_name, intro, award_points, tutorial_id, difficulty = data
            module = Module(module_id, educator_username, module_name, intro, award_points, tutorial_id, difficulty)
            return module
        return None

    def get_tutorial_data(self, id):
        """
        Query to get the module data
        """
        self.cursor.execute('SELECT * FROM All_Tutorials WHERE tute_id = ?', (id,))
        data = self.cursor.fetchone()
        if data:
            tutorial_id, c1, c2, c3, i1, i2, quiz_one, quiz_two, quiz_three = data
            tutorial = Tutorial(tutorial_id, c1, c2, c3, i1, i2, quiz_one, quiz_two, quiz_three)
            return tutorial
        return None

    def get_challenge_data(self, id):
        """
        Query to get the challenge data
        """
        self.cursor.execute('SELECT * FROM All_Challenges WHERE id = ?', (id,))
        data = self.cursor.fetchone()
        if data:
            challenge_id, challenge_name, intro, difficulty, question, solution = data
            challenge = Challenge(challenge_id, challenge_name, intro, difficulty, question, solution)
            return challenge
        return None
