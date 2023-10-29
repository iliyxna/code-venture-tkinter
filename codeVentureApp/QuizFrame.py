from datetime import datetime
from tkinter import messagebox

import customtkinter
import tkinter as tk
from codeVentureApp.SystemStorage import SystemStorage


class QuizFrame(customtkinter.CTkFrame):
    """
    Each quiz will be a tiny frame
    """

    def __init__(self, window, master, quiz_id, user, module_id, module_frame):
        """
        Constructor
        """
        super().__init__(master)
        self.i1 = None
        self.i2 = None
        self.window = window
        self.master = master
        self.quiz_id = quiz_id
        self.user = user
        self.module_frame = module_frame

        self.configure(corner_radius=20,
                       fg_color="transparent",
                       )
        self.system_storage = SystemStorage()
        self.module_id = module_id

        self.score = user.get_current_module_score()
        self.answered_count = user.get_answered_count()

        self.radio_buttons = []

        self.quiz = self.system_storage.get_quiz_data(quiz_id)
        question = self.quiz.get_question()
        solution = self.quiz.get_solution()
        opt1 = self.quiz.get_choice_one()
        opt2 = self.quiz.get_choice_two()
        opt3 = self.quiz.get_choice_three()
        self.choices = [opt1, opt2, opt3]
        self.img = self.quiz.get_image()

        if (self.quiz.get_quiz_id()+1) % 3 == 1:
            self.title = customtkinter.CTkLabel(master=self,
                                                text='Question 1',
                                                font=("Fixedsys", 20),
                                                text_color="#6895B2",
                                                anchor="sw",
                                                justify="left"
                                                )
        elif (self.quiz.get_quiz_id()+1) % 3 == 2:
            self.title = customtkinter.CTkLabel(master=self,
                                                text='Question 2',
                                                font=("Fixedsys", 20),
                                                text_color="#6895B2",
                                                anchor="sw",
                                                justify="left"
                                                )

        elif (self.quiz.get_quiz_id()+1) % 3 == 0:
            self.title = customtkinter.CTkLabel(master=self,
                                                text='Question 3',
                                                font=("Fixedsys", 20),
                                                text_color="#6895B2",
                                                anchor="sw",
                                                justify="left"
                                                )
        self.title.grid(row=1, column=0, padx=5, pady=5, sticky="sw")

        question_label = customtkinter.CTkLabel(master=self,
                                                text=f'{question}',
                                                text_color="#6895B2",
                                                wraplength=830,
                                                justify="left"
                                                )
        question_label.grid(row=2, column=0, padx=5, pady=5, sticky="nw")

        if self.img != "":
            self.i1 = tk.PhotoImage(file=f'images/{self.img}.png')
            i1 = tk.Label(master=self,
                          image=self.i1,
                          borderwidth=0,
                          justify="left",
                          )
            i1.grid(row=3, column=0, padx=10, pady=5, sticky="nw")

        selected_answer = tk.StringVar()

        self.submit_button = customtkinter.CTkButton(self, text="Submit",
                                                     text_color="white",
                                                     fg_color="#435560",
                                                     command=lambda: check_answer(selected_answer.get(), solution))
        self.submit_button.grid(row=7, column=0, padx=5, pady=10, sticky="w")

        def check_answer(selected, ans):
            """
            Method to check the user's answer
            """
            ans_frame = customtkinter.CTkFrame(self)
            if selected == ans:
                ans_frame.configure(bg_color="transparent",
                                    fg_color="#68B274")
                ans_frame.grid(row=8, column=0, padx=5, pady=10, sticky="w")

                result_label = customtkinter.CTkLabel(ans_frame, text="Correct!", text_color="white",
                                                      bg_color="transparent",
                                                      fg_color="transparent",
                                                      )
                self.score = user.get_current_module_score()
                self.user.increment_score()
                self.user.increment_answered()
                result_label.grid(row=8, column=0, padx=5, pady=10, sticky="nw")

            else:
                ans_frame.configure(bg_color="transparent",
                                    fg_color="#CB4C4C")
                ans_frame.grid(row=8, column=0, padx=5, pady=10, sticky="w")

                self.user.increment_answered()
                result_label = customtkinter.CTkLabel(ans_frame,
                                                      text=f'Your answer is incorrect. The correct answer is: \n'
                                                           f'{solution}\n\n Explanation: {self.quiz.get_explanation()}',
                                                      text_color="white",
                                                      # fg_color="#CB4C4C",
                                                      # bg_color="transparent",
                                                      justify="left",
                                                      # corner_radius=5
                                                      )
                result_label.grid(row=8, column=0, padx=5, pady=10, sticky="nw")

            # disable the buttons so only can attempt once per module entry
            for btn in self.radio_buttons:
                btn.configure(state="disabled")
            self.submit_button.configure(state="disabled")

            if self.user.get_answered_count() == 3:
                # display outcome - correct / wrong
                result_frame = customtkinter.CTkFrame(self,
                                                      fg_color="#6895B2")
                result_frame.grid(row=9, column=0, padx=0, pady=30, sticky="sw")

                result_str = customtkinter.CTkLabel(result_frame,
                                                    text=f'Congratulations,'
                                                         f'You have completed this module!'
                                                         f'\n\nScore: {self.user.get_current_module_score()} out of 3',
                                                    font=("Cascadia Mono", 16),
                                                    text_color="white",
                                                    anchor="w",
                                                    justify="left"
                                                    )

                result_str.grid(row=0, column=0, padx=20, pady=20, sticky="w")
                result_button = customtkinter.CTkButton(result_frame, text="Back To Modules",
                                                        height=30,
                                                        # font=("Cascadia Mono", 14),
                                                        fg_color="#435560",
                                                        command=self.window.destroy)
                result_button.grid(row=0, column=1, padx=15, pady=15)
                result_frame.columnconfigure(0, weight=3, minsize=0)

                self.module_frame.window_open = False

                if not self.system_storage.check_learner_module(self.module_id, self.user.get_username()):
                    self.system_storage.insert_module_completion(user, self.module_id,
                                                                 self.user.get_current_module_score())

                elif self.system_storage.check_learner_module(self.module_id, self.user.get_username()):
                    self.system_storage.update_module_score(self.user.get_username(),
                                                            self.user.get_current_module_score())
                    self.system_storage.update_module_date(self.user.get_username(), datetime.today())

        for i in range(len(self.choices)):
            radio_button = customtkinter.CTkRadioButton(self,
                                                        text=self.choices[i],
                                                        text_color="#6895B2",
                                                        variable=selected_answer,
                                                        value=self.choices[i])
            radio_button.grid(row=4 + i, column=0, padx=30, pady=5, sticky="nw")
            self.radio_buttons.append(radio_button)
