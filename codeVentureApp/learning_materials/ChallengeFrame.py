from datetime import datetime
from tkinter import messagebox

import customtkinter
import tkinter as tk

from codeVentureApp.SystemStorage import SystemStorage
from codeVentureApp.learning_materials.CompletedChallenge import CompletedChallenge


class ChallengeFrame(customtkinter.CTkFrame):
    """
    Each challenge will be a tiny frame
    """

    def __init__(self, master, challenge_id, username):
        """
        Constructor
        """
        super().__init__(master)
        self.master = master
        self.challenge_id = challenge_id
        self.username = username
        self.configure(corner_radius=20,
                       fg_color="#AFE1AF",
                       width=830
                       )
        self.system_storage = SystemStorage()

        # retrieve challenge information
        challenge = self.system_storage.get_challenge_data(challenge_id)
        challenge_name = challenge.get_challenge_name()
        challenge_intro = challenge.get_intro()
        challenge_level = challenge.get_difficulty()

        # assigning images based on badges
        self.badge_image = None
        if challenge_level == "Easy":
            self.badge_image = tk.PhotoImage(file='./images/badge1.png')
        elif challenge_level == "Intermediate":
            self.badge_image = tk.PhotoImage(file='./images/badge2.png')
        elif challenge_level == "Hard":
            self.badge_image = tk.PhotoImage(file='./images/badge3.png')

        # attributes for pop-up
        self.popup_success = None
        self.popup = None
        self.answer = None

        # Different card colours
        if challenge_level == "Intermediate":
            self.configure(fg_color="#FFD580")
        if challenge_level == "Hard":
            self.configure(fg_color="#CBC3E3")

        # challenge card details
        name_label = customtkinter.CTkLabel(self,
                                            text=f'\n({challenge_id + 1}) {challenge_name}',
                                            font=("Fixedsys", 20),
                                            text_color="#304263",
                                            anchor="sw",
                                            )
        name_label.grid(row=0, column=0, padx=20, pady=10, sticky="sw")

        intro = customtkinter.CTkLabel(self,
                                       text=f'\n{challenge_intro}',
                                       text_color="#304263",
                                       wraplength=830,
                                       justify="left"
                                       )
        intro.grid(row=2, columnspan=2, padx=20, sticky="w")

        level = customtkinter.CTkLabel(self,
                                       text=f'Difficulty: {challenge_level}',
                                       text_color="white",
                                       font=("Cascadia Code", 14),
                                       fg_color="#355E3B",
                                       corner_radius=10
                                       )
        if challenge_level == "Intermediate":
            level.configure(fg_color="#B87333")
        if challenge_level == "Hard":
            level.configure(fg_color="#702963")
        level.grid(row=1, column=0, padx=20, pady=0, sticky="w")

        start_button = customtkinter.CTkButton(self,
                                               fg_color="white",
                                               text_color="#638294",
                                               text="Start",
                                               command=self.start_challenge)
        start_button.grid(row=3, column=0, padx=20, pady=20, sticky="nw")

    def start_challenge(self):
        """
        Method to start each challenge via pop-up window
        """

        # Check if user would like to reattempt the challenge
        if self.system_storage.get_user_completed_challenge(self.username, self.challenge_id) is not None:
            confirmation_message = messagebox.askyesno("Confirmation", "Do you want to re-attempt the challenge?")
            if confirmation_message:
                self.system_storage.delete_completed_challenge(self.username, self.challenge_id)
            else:
                return

        # initialising the pop-up
        self.popup = tk.Toplevel()
        self.popup.title("Challenge")
        self.popup.geometry("900x600")
        self.popup.configure(background="#C2D3DF")

        # to get the challenge details
        self.system_storage = SystemStorage()

        challenge = self.system_storage.get_challenge_data(self.challenge_id)
        challenge_id = challenge.get_challenge_id()
        challenge_name = challenge.get_challenge_name()
        challenge_question = challenge.get_question()

        # pop-up details
        title = customtkinter.CTkLabel(master=self.popup,
                                       text=f'Let the Challenge Begin 🕹️\n\n'
                                            f'Challenge : {challenge_name} !\n',
                                       text_color="#304263",
                                       font=("Fixedsys", 24, "bold"),
                                       anchor="sw",
                                       justify="left"
                                       )
        title.place(relx=0.05, y=100, relwidth=0.8)
        question = customtkinter.CTkLabel(self.popup,
                                          text=f'{challenge_question}\n',
                                          text_color="#304263",
                                          font=("Fixedsys", 18),
                                          anchor="nw",
                                          justify="left"
                                          )
        question.place(relx=0.05, y=220, relwidth=0.8)

        question_frame = customtkinter.CTkFrame(self.popup,
                                                corner_radius=20,
                                                height=200,
                                                fg_color="white",
                                                )
        question_frame.place(relx=0.05, y=270, relwidth=0.5)

        submit_button = customtkinter.CTkButton(self.popup, text="Submit",
                                                height=30,
                                                font=("Cascadia Mono Bold", 14, "bold"),
                                                command=self.solution
                                                )
        submit_button.place(relx=0.05, y=400, relwidth=0.15)

        # custom for each challenge question
        if challenge_id == 0:
            self.answer = tk.StringVar()
            answer_entry = customtkinter.CTkEntry(question_frame, textvariable=self.answer,
                                                  fg_color="#C2D3DF", border_color="#6895B2",
                                                  text_color="#304263")
            answer_entry.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

            question_cont = customtkinter.CTkLabel(question_frame,
                                                   text=f'("Hello World")\n',
                                                   text_color="#304263",
                                                   font=("Cascadia Mono Bold", 16),
                                                   anchor="sw",
                                                   justify="left"
                                                   )
            question_cont.grid(row=0, column=1, sticky="sw", padx=10, pady=10)

        elif challenge_id == 1:
            self.answer = tk.StringVar()
            answer_entry = customtkinter.CTkEntry(question_frame, textvariable=self.answer,
                                                  fg_color="#C2D3DF", border_color="#6895B2",
                                                  text_color="#304263")
            answer_entry.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

            question_cont = customtkinter.CTkLabel(question_frame,
                                                   text=f'This is a single comment\n',
                                                   text_color="#304263",
                                                   font=("Cascadia Mono Bold", 16),
                                                   anchor="sw",
                                                   justify="left"
                                                   )
            question_cont.grid(row=0, column=1, sticky="sw", padx=10, pady=10)
        elif challenge_id == 2:
            self.answer = tk.StringVar()
            question_cont = customtkinter.CTkLabel(question_frame,
                                                   text=f'   x = 5\n'
                                                        f'   print(type(x))',
                                                   text_color="#304263",
                                                   font=("Cascadia Mono Bold", 16),
                                                   anchor="sw",
                                                   justify="left"
                                                   )
            question_cont.grid(row=0, column=0, sticky="sw", padx=10, pady=10)

            answer_entry = customtkinter.CTkEntry(question_frame, textvariable=self.answer,
                                                  fg_color="#C2D3DF", border_color="#6895B2",
                                                  text_color="#304263")
            answer_entry.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

    def solution(self):
        """
        Method to verify the solution
        """
        self.system_storage = SystemStorage()

        challenge = self.system_storage.get_challenge_data(self.challenge_id)
        challenge_solution = challenge.get_solution()

        # display outcome - correct / wrong
        result_frame = customtkinter.CTkFrame(self.popup, fg_color="transparent")
        result_frame.place(relx=0.05, y=450, relwidth=0.6)

        if challenge_solution == self.answer.get():

            result_frame.configure(fg_color="#50C878")

            result_str = customtkinter.CTkLabel(result_frame,
                                                text=f'Your Answer is Correct!',
                                                font=("Cascadia Mono Bold", 16),
                                                text_color="#304263",
                                                anchor="w",
                                                justify="left"
                                                )
            result_str.grid(row=0, column=0, padx=20, pady=20, sticky="w")
            result_button = customtkinter.CTkButton(result_frame, text="Next",
                                                    height=30,
                                                    font=("Cascadia Mono Bold", 14, "bold"),
                                                    command=self.complete_challenge)
            result_button.grid(row=0, column=1, padx=15, pady=15)
            result_frame.columnconfigure(0, weight=3, minsize=0)

        else:
            result_frame.configure(fg_color="#FAA0A0")

            result_str = customtkinter.CTkLabel(result_frame,
                                                text=f'Your answer is incorrect! Try Again',
                                                font=("Cascadia Mono Bold", 16),
                                                text_color="#304263",
                                                anchor="w",
                                                justify="left"
                                                )
            result_str.grid(row=0, column=0, padx=20, pady=20, sticky="w")

    def complete_challenge(self):
        """
        Method to collect badges once user has completed a challenge
        """
        # destroy previous pop up
        self.popup.destroy()

        # create pop up
        self.popup_success = tk.Toplevel()
        self.popup_success.title("Congratulations!")
        self.popup_success.geometry("520x560")
        self.popup_success.configure(background="#C2D3DF")

        # to get badge name
        self.system_storage = SystemStorage()

        challenge = self.system_storage.get_challenge_data(self.challenge_id)
        badge_name = challenge.get_badge_award()

        title = customtkinter.CTkLabel(self.popup_success,
                                       text=f'Congratulations\n You\'ve Earned a Badge!\n',
                                       text_color="#304263",
                                       font=("Cascadia Mono Bold", 20, "bold")
                                       )
        title.grid(row=0, column=0, padx=20, pady=20)

        badge_label = tk.Label(self.popup_success,
                               image=self.badge_image,
                               borderwidth=0,
                               anchor="w",
                               bg="#C2D3DF")
        badge_label.grid(row=1, column=0, padx=20, pady=20)

        message = customtkinter.CTkLabel(self.popup_success,
                                         text=f'You\'ve unlocked the {badge_name} badge by acing this challenge.\n '
                                              f'Your success is the key to this shiny achievement! 🏅',
                                         text_color="#304263",
                                         font=("Cascadia Mono Bold", 16)
                                         )
        message.grid(row=2, column=0, padx=20, pady=20)

        claim_button = customtkinter.CTkButton(self.popup_success,
                                               text="Claim Your Badge",
                                               height=40,
                                               font=("Cascadia Mono Bold", 14, "bold"),
                                               command=self.update_complete_challenge)
        claim_button.grid(row=3, column=0, padx=20, pady=20)

    def update_complete_challenge(self):
        """
        Method to update the learner's badges once they have completed a challenge
        """
        self.system_storage = SystemStorage()

        challenge = self.system_storage.get_challenge_data(self.challenge_id)
        badge_name = challenge.get_badge_award()
        challenge_id = challenge.get_challenge_id()

        completion_date = datetime.now().strftime("%Y-%m-%d")

        completed_challenge = CompletedChallenge(challenge_id, self.username, badge_name, completion_date)
        self.system_storage.insert_completed_challenge(completed_challenge)

        self.popup_success.destroy()
