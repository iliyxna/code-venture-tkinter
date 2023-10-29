import customtkinter
import tkinter as tk

from codeVentureApp.QuizFrame import QuizFrame
from codeVentureApp.SystemStorage import SystemStorage


class ModuleFrame(customtkinter.CTkFrame):
    """
    Each module will be a tiny frame
    """

    def __init__(self, master, module_id, user):
        super().__init__(master)
        self.i1 = None
        self.i2 = None
        self.master = master
        self.module_id = module_id
        self.configure(corner_radius=20,
                       fg_color="#638294",
                       # width=830
                       )
        self.user = user
        # Flag to check if the window is open
        self.window_open = False
        self.new_window = None

        self.system_storage = SystemStorage()

        self.module = self.system_storage.get_module_data(module_id)
        self.module_name = self.module.get_module_name()
        self.module_intro = self.module.get_intro()
        self.module_level = self.module.get_level()

        # Different card colours
        if self.module_level == "Intermediate":
            self.configure(fg_color="#435560")
        if self.module_level == "Advanced":
            self.configure(fg_color="#223039")

        name_label = customtkinter.CTkLabel(self,
                                            text=f'\n({module_id + 1}) {self.module_name}',
                                            font=("Fixedsys", 20),
                                            text_color="white",
                                            anchor="sw",
                                            )
        name_label.grid(row=0, column=0, padx=20, pady=10, sticky="sw")

        intro = customtkinter.CTkLabel(self,
                                       text=f'\n{self.module_intro}',
                                       text_color="white",
                                       wraplength=830,
                                       justify="left"
                                       )
        intro.grid(row=2, columnspan=2, padx=20, sticky="w")

        level = customtkinter.CTkLabel(self,
                                       text=f'Difficulty: {self.module_level}',
                                       text_color="white",
                                       font=("Cascadia Code", 14),
                                       fg_color="#6895B2",
                                       corner_radius=10
                                       )
        if self.module_level == "Intermediate":
            level.configure(fg_color="#6F818D")
        if self.module_level == "Advanced":
            level.configure(fg_color="#4A697D")
        level.grid(row=1, column=0, padx=20, pady=10, sticky="nw")

        start_button = customtkinter.CTkButton(self,
                                               fg_color="white",
                                               text_color="#638294",
                                               text="Start",
                                               command=self.start_module)
        start_button.grid(row=3, column=0, padx=20, pady=20, sticky="nw")

    def start_module(self):
        """
        Method that spawns a new window for the tutorial and quizzes
        """
        if not self.window_open:
            self.window_open = True
            correct_count = 0
            is_correct = False
            # Create a new Toplevel window
            self.new_window = customtkinter.CTkToplevel(self.master,
                                                   fg_color="#C2D3DF")
            self.new_window.geometry("980x670")
            self.new_window.title(f"Module {self.module_id + 1}: {self.module_name}")

            # Add your content to the new window here
            window_frame = customtkinter.CTkScrollableFrame(self.new_window,
                                                            fg_color="transparent")
            window_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

            # top frame
            tutorial_frame = customtkinter.CTkFrame(window_frame,
                                                    corner_radius=20,
                                                    fg_color="#FAFAFA",
                                                    )
            tutorial_frame.grid(row=0, column=0, padx=40, pady=50, sticky="ew")

            module_title = customtkinter.CTkLabel(master=tutorial_frame,
                                                  text=f'Module {self.module_id + 1}: {self.module_name}',
                                                  font=("Fixedsys", 24),
                                                  anchor="sw",
                                                  text_color="#6895B2",
                                                  justify="left"
                                                  )
            module_title.grid(row=0, column=0, padx=30, pady=30, sticky="sw")

            tutorial_title = customtkinter.CTkLabel(master=tutorial_frame,
                                                    text=f'Tutorial',
                                                    font=("Fixedsys", 22),
                                                    text_color="#6895B2",
                                                    anchor="sw",
                                                    justify="left"
                                                    )
            tutorial_title.grid(row=1, column=0, padx=30, pady=10, sticky="sw")

            tutorial = self.system_storage.get_tutorial_data(self.module.get_tutorial_id())

            c1 = customtkinter.CTkLabel(master=tutorial_frame,
                                        text=f'{tutorial.get_c1()}',
                                        text_color="#6895B2",
                                        # anchor="sw",
                                        wraplength=830,
                                        justify="left"
                                        )
            c1.grid(row=2, column=0, padx=30, pady=5, sticky="sw")

            if tutorial.get_i1() != "":
                self.i1 = tk.PhotoImage(file=f'images/{tutorial.get_i1()}.png')
                i1 = tk.Label(master=tutorial_frame,
                              image=self.i1,
                              borderwidth=0,
                              justify="left",
                              )
                i1.grid(row=3, column=0, padx=30, pady=5, sticky="nw")

            if tutorial.get_c2() != "":
                c2 = customtkinter.CTkLabel(master=tutorial_frame,
                                            text=f'{tutorial.get_c2()}',
                                            text_color="#6895B2",
                                            anchor="sw",
                                            wraplength=830,
                                            justify="left"
                                            )
                c2.grid(row=4, column=0, padx=30, pady=5, sticky="sw")

            if tutorial.get_i2() != "":
                self.i2 = tk.PhotoImage(file=f'images/{tutorial.get_i2()}.png')
                i2 = tk.Label(master=tutorial_frame,
                              image=self.i2,
                              borderwidth=0,
                              anchor="w",
                              justify="left"
                              )
                i2.grid(row=5, column=0, padx=30, pady=5, sticky="w")

            if tutorial.get_c3() != "":
                c2 = customtkinter.CTkLabel(master=tutorial_frame,
                                            text=f'{tutorial.get_c3()}',
                                            text_color="#6895B2",
                                            anchor="w",
                                            wraplength=830,
                                            justify="left"
                                            )
                c2.grid(row=6, column=0, padx=30, pady=5, sticky="w")

            def start_quiz():
                quiz_frame = customtkinter.CTkFrame(window_frame,
                                                    corner_radius=20,
                                                    fg_color="#FAFAFA",
                                                    )
                quiz_frame.grid(row=1, column=0, padx=40, sticky="ew")

                quiz_title = customtkinter.CTkLabel(master=quiz_frame,
                                                    text=f'It\'s Quiz Time!',
                                                    font=("Fixedsys", 24),
                                                    text_color="#6895B2",
                                                    anchor="sw",
                                                    justify="left"
                                                    )
                quiz_title.grid(row=0, column=0, padx=30, pady=20, sticky="sw")

                ques_frame = customtkinter.CTkFrame(quiz_frame,
                                                    corner_radius=20,
                                                    fg_color="#FAFAFA",
                                                    )
                ques_frame.grid(row=1, column=0, padx=30, pady=10, sticky="new")

                curr_row = 1
                self.user.current_module_score = 0
                self.user.answered_count = 0
                for i in range(self.module.get_tutorial_id() * 3, self.module.get_tutorial_id() * 3 + 3):
                    quiz_card = QuizFrame(self.new_window, ques_frame, i, self.user, self.module_id, self)
                    quiz_card.grid(row=curr_row, column=0, padx=30, pady=20, sticky="sw")
                    curr_row += 1

            quiz_button = customtkinter.CTkButton(master=tutorial_frame,
                                                  text="Start Quiz",
                                                  text_color="white",
                                                  fg_color="#435560",
                                                  command=start_quiz
                                                  )
            quiz_button.grid(row=7, column=0, padx=30, pady=20, sticky="nw")

            # Function to run when the new window is closed
            def on_close():
                self.window_open = False
                self.new_window.destroy()

            self.new_window.protocol("WM_DELETE_WINDOW", on_close)
