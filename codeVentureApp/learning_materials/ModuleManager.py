import time

from SystemStorage import SystemStorage
from learning_materials.Module import Module
from learning_materials.Quiz import Quiz
from learning_materials.Solution import Solution
from learning_materials.Tutorial import Tutorial
from utilities.Level import Level


class ModuleManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModuleManager, cls).__new__(cls)
            cls._instance.__init__()  # Initialize the manager only once
        return cls._instance

    def __init__(self):
        self.system_storage = SystemStorage()
        self.all_existing_modules = self.get_all_modules()
        self.beginner_modules = []
        self.intermediate_modules = []
        self.advanced_modules = []

    def get_all_modules(self):
        self.all_existing_modules = [Module("Python Basics", 50, [], [], [], Level.BEGINNER),
                                     Module("Control Flow and Conditional Statements", 60, [], [], [], Level.BEGINNER),
                                     Module("Functions and Modules", 70, [], [], [], Level.INTERMEDIATE),
                                     Module("Data Structures", 80, [], [], [], Level.INTERMEDIATE),
                                     Module("File Handling", 60, [], [], [], Level.INTERMEDIATE),
                                     Module("Object-Oriented Programming (OOP)", 80, [], [], [], Level.INTERMEDIATE)
                                     ]

        # self.sort_modules()
        # update system storage
        self.system_storage.all_modules = self.all_existing_modules

        return self.all_existing_modules

    def add_module(self, module):
        self.all_existing_modules.append(module)

    def get_module(self, module_name):
        for module in self.all_existing_modules:
            if module.module_name == module_name:
                return module
        return None

    def show_all_modules(self):
        modules = ""
        # self.sort_modules()

        print("BEGINNER MODULES\n")
        for module in self.beginner_modules:
            modules += f'{module.get_module_name()}, Completion Status: {module.get_status().name}\n'

        print("INTERMEDIATE MODULES\n")
        for module in self.intermediate_modules:
            modules += f'{module.get_module_name()}, Completion Status: {module.get_status().name}\n'

        print("ADVANCED MODULES\n")
        for module in self.advanced_modules:
            modules += f'{module.get_module_name()}, Completion Status: {module.get_status().name}\n'

    # def sort_modules(self):
    #     for module in self.all_existing_modules:
    #         if module.get_level().value == Level.BEGINNER.value:
    #             if module not in self.beginner_modules:
    #                 self.beginner_modules.append(module)
    #         elif module.get_level().value == Level.INTERMEDIATE.value:
    #             if module not in self.intermediate_modules:
    #                 self.intermediate_modules.append(module)
    #         elif module.get_level().value == Level.ADVANCED.value:
    #             if module not in self.advanced_modules:
    #                 self.advanced_modules.append(module)

    def module_menu(self):
        """
        Prints the menu options for the learner user
        """
        print("Select the module you want to enrol in:")
        for i in range(len(self.get_all_modules())):
            module = self.get_all_modules()[i]
            print(f'{i + 1}. {module.get_module_name()}, Level: {module.get_level().name}')

            if i == len(self.get_all_modules()) - 1:
                print(f'{i + 2}. Back to dashboard')

    def module_main(self, user):
        while True:
            self.module_menu()
            cont = ""
            user_input = input("Please enter a menu option: ")
            if user_input == "1":
                # module = self.get_all_modules()[0].get_tutorials()
                found = False

                for module in user.progress.get_modules_completed():
                    if self.get_all_modules()[0].get_module_name() == module.get_module_name():
                        found = True
                        prompt = input(
                            "You have already completed this module, do you want to re-do this module?\n"
                            "Note that you will not earn extra points from completing this module.\n"
                            "Enter (Y/N): ")
                        cont = prompt

                        while prompt.upper() not in ["Y", "N"]:
                            print("You have not entered a valid input. Please enter either: Y for Yes, N for No")
                            prompt = input(
                                "You have already completed this module, do you want to re-do this module?\n"
                                "Note that you will not earn extra points from completing this module.\n"
                                "Enter (Y/N): ")
                            cont = prompt

                        if prompt.upper() == "N":
                            break

                if cont.upper() != "N":

                    content = (
                    "\nPYTHON BASICS TUTORIAL\nWelcome to the \"Python Basics\" module! In this tutorial, you'll "
                    "get started with the fundamentals of Python programming. Python is a versatile and beginner-friendly "
                    "programming language used in various domains, including web development, data analysis, and automation. Let's dive in! \n\n"
                    "What is Python?\nPython is a high-level, interpreted programming language known for its simplicity and readability.\n"
                    "It uses an easy-to-understand syntax, making it an excellent choice for beginners. Python is often used for tasks like\n"
                    "data analysis, web development, scientific computing, and more.\n\n""Python Basics\nVariables and Data Types\n"
                    "In Python, you can store data in variables.Variables are like containers that hold different types of information. "
                    "Common data types include:\n""int: Integer numbers (e.g., 5, -10, 42) \n"
                    "float: Floating-point numbers (e.g., 3.14, -0.5, 2.0)\n"
                    "str: Strings (e.g., \"Hello, World\", 'Python')\n"
                    "bool: Boolean values (True or False)\n"
                    "list: Ordered collection of items (e.g., [1, 2, 3])\n"
                    "tuple: Ordered, immutable collection (e.g., (1, 2, 3))\n"
                    "dict: Key-value pairs (e.g., {'name': 'Alice', 'age': 30})")

                    print(content)
                    time.sleep(2)

                    print("\nCongratulations, you have reached the end of this tutorial!\n")

                    temp_score = 0
                    total_score = 5

                    time.sleep(2)
                    # proceed to quiz
                    print("\nNow it's time for the End-of-topic Quiz\n")
                    time.sleep(1)
                    # Question 1
                    q1 = "What is the data type of 3920? Do not add additional spaces in your answer."
                    s1 = "int"

                    print(f"Question 1.\n{q1}")
                    user_answer = input("Your answer: ")
                    if user_answer == s1:
                        temp_score += 2.5
                        print(f"Correct Answer! Current score {temp_score}/{total_score}.0")
                    else:
                        print("Incorrect Answer. The answer should be: int")

                    time.sleep(1)

                    # Question 2
                    q2 = "What is the data type of \"hello\"? Do not add additional spaces in your answer."
                    s2 = "str"

                    print(q2)
                    user_answer = input("Your answer: ")
                    if user_answer == s2:
                        temp_score += 2.5
                        print(f"Correct Answer! Current score {temp_score}/{total_score}.0")
                    else:
                        print("Incorrect Answer. The answer should be: str")

                    print(f"Congratulations, you have completed this module! Score: {temp_score}/{total_score}.0")

                    done = False
                    for module in user.progress.get_modules_completed():
                        if self.get_all_modules()[0].get_module_name() == module.get_module_name():
                            done = True
                            break

                    if not done:
                        user.update_progress(module=self.get_all_modules()[0], challenge=None)
                        user.points.add_points(self.get_all_modules()[0].get_award_points().get_point_value())

                    time.sleep(1)
                    print("Going back to modules...\n")
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
                print("Under Maintenance")
            elif user_input == "6":
                print("Under Maintenance")
            elif user_input == "7":
                print("Going back to Learner's dashboard...")
                break
            else:
                print("You have not entered a valid menu option. Please try again.\n")

