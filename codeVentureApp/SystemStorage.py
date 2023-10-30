import sqlite3
from datetime import datetime

from codeVentureApp.learning_materials.Challenge import Challenge
from codeVentureApp.learning_materials.CompletedChallenge import CompletedChallenge
from codeVentureApp.learning_materials.Module import Module
from codeVentureApp.learning_materials.Quiz import Quiz
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
    4) Table that stores the learner's completed modules
    5) Table that stores the learner's completed challenges
    6) Table that stores the modules
    7) Table that stores the challenges
    8) Table that stores the quizzes
    9) Table that stores the tutorials
    10) Table that stores the forum posts
    11) Table that stores the forum replies
    """
    def __init__(self):
        """
        Constructor
        """
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
                                role TEXT,
                                security_question TEXT,
                                answer TEXT
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
                                module_id INTEGER,
                                username TEXT,
                                completion_date TEXT,
                                score INTEGER
                                )
                                '''
        self.connection.execute(table_create_query)
        self.connection.commit()

        """
        Table 5
        """
        table_create_query = '''CREATE TABLE IF NOT EXISTS Challenge_Completion_Data
                                (
                                id INTEGER,
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
                                               solution TEXT,
                                               badge_award TEXT
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
                                                       explanation TEXT
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

        """
        Table 10
        """
        table_create_query = '''CREATE TABLE IF NOT EXISTS Forum_Post
                                        (
                                        forum_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        module_id INTEGER,
                                        username TEXT,
                                        user_role TEXT,
                                        content TEXT,
                                        date_posted TEXT
                                        )
                                        '''

        self.connection.execute(table_create_query)
        self.connection.commit()

        """
        Table 11
        """
        table_create_query = '''CREATE TABLE IF NOT EXISTS Forum_Replies
                                (
                                reply_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                forum_id INTEGER,
                                username TEXT,
                                user_role TEXT,
                                content TEXT,
                                date_replied TEXT
                                )
                                '''

        self.connection.execute(table_create_query)
        self.connection.commit()

    def insert_user_data(self, user, question, answer):
        """
        Query to insert user data into the User_Data and Learner_Progress table
        """
        self.cursor.execute('''
                    INSERT INTO User_Data (username, password, firstname, lastname, role, security_question, answer)
                    VALUES (?, ?, ?, ?, ?, ? ,?)
                ''', (
            user.get_username(), user.get_password(), user.get_firstname(), user.get_lastname(), user.get_role(),
            question, answer))
        self.connection.commit()

        # update learner's progress
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

    def insert_module_completion(self, learner, module_id, score):
        """
        Query to link child's username to parent account
        """
        self.cursor.execute('''
                            INSERT INTO Module_Completion_Data (module_id, username, completion_date, score)
                            VALUES (?, ?, ?, ?)
                            ''', (module_id, learner.get_username(), datetime.today(), score))
        self.connection.commit()

    def insert_completed_challenge(self, challenge):
        """
        Query to insert completed challenge and badge earned into Challenge_Completion_Data table
        """
        self.cursor.execute('''
                    INSERT INTO Challenge_Completion_Data (id, username, badge_earned, completion_date)
                    VALUES (?, ?, ?, ?)
                ''', (
            challenge.get_challenge_id(), challenge.get_user(), challenge.get_badge_award(),
            challenge.get_completion_date()))
        self.connection.commit()

    def insert_forum_post(self, module_id, username, user_role, content, date_posted):
        """
        Query to link child's username to parent account
        """
        self.cursor.execute('''
                            INSERT INTO Forum_Post (module_id, username, user_role, content, date_posted)
                            VALUES (?, ?, ?, ?, ?)
                            ''', (module_id, username, user_role, content, date_posted,))
        self.connection.commit()

    def insert_forum_reply(self, forum_id, username, user_role, content, date_replied):
        """
        Query to link child's username to parent account
        """
        self.cursor.execute('''
                            INSERT INTO Forum_Replies (forum_id, username, user_role, content, date_replied)
                            VALUES (?, ?, ?, ?, ?)
                            ''', (forum_id, username, user_role, content, date_replied,))
        self.connection.commit()

    def get_forum_posts(self, module_id):
        """
        Query to posts for a module
        """
        self.cursor.execute('SELECT * FROM Forum_Post WHERE module_id = ?',
                            (module_id,))
        user_data = self.cursor.fetchall()
        if user_data:
            return user_data
        return None

    def get_forum_id(self, module_id, username, content):
        """
        Query to posts for a module
        """
        self.cursor.execute('SELECT forum_id FROM Forum_Post WHERE module_id = ? AND username = ? AND content = ?',
                            (module_id, username, content))
        user_data = self.cursor.fetchone()[0]
        if user_data:
            return user_data
        return None

    def get_replies(self, forum_id):
        """
        Query to replies for a post
        """
        self.cursor.execute('SELECT * FROM Forum_Replies WHERE forum_id = ?',
                            (forum_id,))
        user_data = self.cursor.fetchall()
        if user_data:
            return user_data
        return None

    def get_user_completed_challenge(self, username, challenge_id):
        """
        Query to get user who completed challenge
        """
        self.cursor.execute('SELECT * FROM Challenge_Completion_Data WHERE id = ? AND username = ?',
                            (challenge_id, username))
        user_data = self.cursor.fetchone()
        if user_data:
            challenge_id, username, badge_name, completion_date = user_data
            return CompletedChallenge(challenge_id, username, badge_name, completion_date)
        return None

    def delete_completed_challenge(self, username, challenge_id):
        """
        Query to delete user who completed challenge
        """
        self.cursor.execute('DELETE FROM Challenge_Completion_Data WHERE id = ? AND username = ?',
                            (challenge_id, username))
        self.connection.commit()  # Commit changes to the database

        if self.cursor.rowcount > 0:
            return True  # Indicate that the deletion was successful
        else:
            return False  # Indicate that the deletion did not occur

    def update_module_score(self, module_id, username, score):
        """
        Query to update module score if user retakes the module
        """
        self.cursor.execute(
            'UPDATE Module_Completion_Data SET score = ? WHERE module_id = ? AND username = ?',
            (score, module_id, username))
        self.connection.commit()

    def update_module_date(self, module_id, username, date):
        """
        Query to update module completion date if user retakes the module
        """
        self.cursor.execute(
            'UPDATE Module_Completion_Data SET completion_date = ? WHERE module_id = ? AND username = ?',
            (date, module_id, username))
        self.connection.commit()

    def check_learner_module(self, module_id, username):
        """
        Query to check if learner have completed the module
        """
        self.cursor.execute('SELECT * FROM Module_Completion_Data WHERE module_id = ? AND username = ?',
                            (module_id, username))
        user_data = self.cursor.fetchone()
        if user_data:
            return True
        return False

    def get_user(self, username, password):
        """
        Query to get user
        """
        self.cursor.execute('SELECT * FROM User_Data WHERE username = ? AND password = ?', (username, password))
        user_data = self.cursor.fetchone()
        if user_data:
            username, password, firstname, lastname, role, ques, ans = user_data
            if role == "Learner":
                return Learner(username, password, firstname, lastname, ques, ans)
            elif role == "Parent":
                return Parent(username, password, firstname, lastname, ques, ans)
            elif role == "Educator":
                return Educator(username, password, firstname, lastname, ques, ans)
            elif role == "Admin":
                return Administrator(username, password, firstname, lastname, ques, ans)
        return None

    def get_user_by_username(self, username):
        """
        Query to get user only by username
        """
        self.cursor.execute('SELECT * FROM User_Data WHERE username = ?', (username,))
        user_data = self.cursor.fetchone()
        if user_data:
            username, password, firstname, lastname, role, ques, ans = user_data
            if role == "Learner":
                return Learner(username, password, firstname, lastname, ques, ans)
            elif role == "Parent":
                return Parent(username, password, firstname, lastname, ques, ans)
            elif role == "Educator":
                return Educator(username, password, firstname, lastname, ques, ans)
            elif role == "Admin":
                return Administrator(username, password, firstname, lastname, ques, ans)
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
            challenge_id, challenge_name, intro, difficulty, question, solution, badge_award = data
            challenge = Challenge(challenge_id, challenge_name, intro, difficulty, question, solution, badge_award)
            return challenge
        return None

    def get_quiz_data(self, id):
        """
        Query to get the module data
        """
        self.cursor.execute('SELECT * FROM All_Quizzes WHERE id = ?', (id,))
        data = self.cursor.fetchone()
        if data:
            quiz_id, question, solution, choice_one, choice_two, choice_three, explanation, img = data
            quiz = Quiz(quiz_id, question, solution, choice_one, choice_two, choice_three, explanation, img)
            return quiz
        return None

    def get_learner_badge(self, username):
        """
        Query to get the module data
        """
        self.cursor.execute('SELECT * FROM Challenge_Completion_Data WHERE username = ?', (username,))
        all_data = self.cursor.fetchall()
        if all_data:
            return all_data
        return None

    def get_learner_modules(self, username):
        """
        Query to get all the completed modules
        """
        self.cursor.execute("SELECT * FROM Module_Completion_Data WHERE username = ? ORDER BY module_id",
                            (username,))
        all_data = self.cursor.fetchall()
        if all_data:
            return all_data
        return None

    def get_all_students(self):
        """
        Query to get the number of students
        """
        self.cursor.execute("SELECT * FROM Learner_Progress")
        students = self.cursor.fetchall()
        if students:
            return students
        return None

    def get_teaching_module(self, edu_name):
        """
        Query to get the teaching module incharge
        """
        self.cursor.execute("SELECT * FROM All_modules WHERE educator_username = ?",
                            (edu_name,))
        all_data = self.cursor.fetchone()
        if all_data:
            return all_data
        return None

    def get_students_completed(self, module_id):
        """
        Query to get the info of students that completed the module
        """
        self.cursor.execute("SELECT * FROM Module_Completion_Data WHERE module_id = ?",
                            (module_id,))
        all_data = self.cursor.fetchall()
        if all_data:
            return all_data
        return None

    def get_all_modules(self):
        """
        Query to get all the modules
        """
        self.cursor.execute("SELECT * FROM All_Modules")
        all_modules = self.cursor.fetchall()
        if all_modules:
            return all_modules
        return None
