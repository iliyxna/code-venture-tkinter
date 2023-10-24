import time
from datetime import datetime

# from codeVentureApp.SystemStorage import SystemStorage
from codeVentureApp.learning_materials.Challenge import Challenge
from codeVentureApp.rewards.Badge import Badge
from codeVentureApp.utilities.Difficulty import Difficulty


class ChallengeManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ChallengeManager, cls).__new__(cls)
            cls._instance.__init__()  # Initialize the manager only once
        return cls._instance

    def __init__(self):
        # self.system_storage = SystemStorage()
        self.all_existing_challenges = []
        self.easy_challenges = []
        self.medium_challenges = []
        self.hard_challenges = []

    def get_all_challenges(self):
        challenge1_question = "Reverse a String: Write a Python function that takes a string as input and returns the reverse of that string."

        solution1 = "def reverse(input_string): return input_string[::-1]"

        badge1 = Badge("New Challenger Badge", "Completed Challenge 1. String Reversal")

        challenge2_question = "Find the Maximum Element: Write a Python function that takes a list of numbers as input and returns the maximum element from the list."

        def solution2(input_list):
            if not input_list:
                return None
            return max(input_list)

        badge2 = Badge("Max Element Finder Badge", "Completed Challenge 2. Find Max Element")

        challenge3_question = "Fibonacci Sequence: Write a Python function that generates the Fibonacci sequence up to a specified number of terms."

        def solution3(n):
            fib_sequence = [0, 1]
            while len(fib_sequence) < n:
                next_value = fib_sequence[-1] + fib_sequence[-2]
                fib_sequence.append(next_value)
            return fib_sequence

        badge3 = Badge("Fibonacci Badge", "Completed Challenge 3. Fibonacci Sequence")

        # Create challenge objects
        test_challenge = Challenge(0, Difficulty.EASY, "Printing: Print \"Hello World!\" to the console.",
                                   "print(\"Hello World!\")",
                                   Badge("Beginner Badge", "Print Hello World!"), 10)
        challenge1 = Challenge(1, Difficulty.EASY, challenge1_question, solution1, badge1, 10)
        challenge2 = Challenge(2, Difficulty.MEDIUM, challenge2_question, solution2, badge2, 10)
        challenge3 = Challenge(3, Difficulty.HARD, challenge3_question, solution3, badge3, 10)

        self.all_existing_challenges = [test_challenge, challenge1, challenge2, challenge3]

        # update system storage
        # self.system_storage.all_challenges = self.all_existing_challenges

        return self.all_existing_challenges

    def add_challenge(self, challenge):
        self.all_existing_challenges.append(challenge)

    def get_challenge(self, challenge_id):
        for challenge in self.all_existing_challenges:
            if challenge.challenge_id == challenge_id:
                return challenge
        return None

    def challenge_menu(self):
        """
        Prints the menu options for the learner user
        """
        print("Select the challenge you want to take:")
        for i in range(len(self.get_all_challenges())):
            challenge = self.get_all_challenges()[i]
            print(f'{i + 1}. {challenge.get_question()}, Level: {challenge.get_difficulty().name}')

            if i == len(self.get_all_challenges()) - 1:
                print(f'{i + 2}. Back to dashboard')

    def challenge_main(self, user):
        while True:
            self.challenge_menu()
            cont = ""
            user_input = input("Please enter a menu option: ")
            if user_input == "1":
                found = False

                for challenge in user.progress.get_challenges_completed():
                    if self.get_all_challenges()[0].get_question() == challenge.get_question():
                        found = True
                        prompt = input(
                            "You have already completed this challenge, do you want to re-do this challenge?\n"
                            "Note that you will not earn extra badges from completing this challenge.\n"
                            "Enter (Y/N): ")
                        cont = prompt

                        while prompt.upper() not in ["Y", "N"]:
                            print("You have not entered a valid input. Please enter either: Y for Yes, N for No")
                            prompt = input(
                                "You have already completed this challenge, do you want to re-do this challenge?\n"
                                "Note that you will not earn extra badges from completing this challenge.\n"
                                "Enter (Y/N): ")
                            cont = prompt

                        if prompt.upper() == "N":
                            break

                if cont.upper() != "N":
                    challenge = self.get_all_challenges()[0]
                    print("\nChallenge ONE")
                    print(challenge.get_question() + "\n")

                    user_input = input("Your solution: \n")

                    if user_input == challenge.get_solution():
                        print("Congratulations! You have successfully completed the challenge.\n")
                        time.sleep(1)

                        done = False
                        for challenge in user.progress.get_challenges_completed():
                            if self.get_all_challenges()[0].get_question() == challenge.get_question():
                                done = True
                                break

                        if not done:
                            challenge.get_badge_award().set_date_earned(datetime.today())
                            print(f"You have earned a new badge: {challenge.get_badge_award().get_badge_name()}! "
                                  f"Check your progress tracker to view your badges earned.")
                            user.get_progress_tracker().update_badges_earned(challenge.get_badge_award())
                            user.update_progress(module=None, challenge=self.get_all_challenges()[0])

                        time.sleep(1)
                        print("Going back to challenges...")
                        time.sleep(1)

                    else:
                        print("Incorrect solution. Try again next time.")
                        time.sleep(1)
                        print("Going back to challenges...")
                        time.sleep(1)
                else:
                    print("Going back to modules...\n")

            elif user_input == "2":
                print("Under Maintenance")

            elif user_input == "3":
                print("Under Maintenance")

            elif user_input == "4":
                print("Under Maintenance")

            elif user_input == "5":
                print("Going back to Learner's dashboard...")
                break
            else:
                print("You have not entered a valid menu option. Please try again.\n")
