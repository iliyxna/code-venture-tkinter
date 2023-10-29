import customtkinter
import tkinter as tk

from codeVentureApp.SystemStorage import SystemStorage


class ProgressTrackerFrame(customtkinter.CTkFrame):
    """
    Class to display the learner's progress
    """
    def __init__(self, master, user):
        """
        Constructor
        """
        super().__init__(master=master)
        self.master = master
        self.user = user
        self.configure(corner_radius=20,
                       fg_color="#FAFAFA")

        self.system_storage = SystemStorage()

        self.badge_display_one = tk.PhotoImage(file='images/badge1.png')
        self.badge_display_two = tk.PhotoImage(file='images/badge2.png')
        self.badge_display_three = tk.PhotoImage(file='images/badge3.png')
        self.badge_earned_list = self.system_storage.get_learner_badge(self.user.get_username())

        self.completed_modules = self.system_storage.get_learner_modules(self.user.get_username())

        percentage = (len(self.completed_modules) / 10) * 100
        self.user = self.system_storage.update_learner_percentage(self.user.get_username(), percentage)

        progress_label = customtkinter.CTkLabel(master=self,
                                                text='Progress Tracking',
                                                font=("Fixedsys", 24),
                                                text_color="#6895B2",
                                                anchor="w",
                                                )
        progress_label.grid(row=0, column=0, padx=30, pady=20, sticky="w")

        # progress bar
        pt_frame = customtkinter.CTkFrame(self)
        pt_frame.configure(fg_color="transparent")
        pt_frame.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        pt_label = customtkinter.CTkLabel(pt_frame, text="Progress Bar",
                                          text_color="#6895B2",
                                          font=("Cascadia Mono Bold", 16))
        pt_label.grid(row=0, column=0, padx=10, sticky="w")

        progress_bar = customtkinter.CTkProgressBar(pt_frame,
                                                    orientation="horizontal",
                                                    mode="determinate",
                                                    corner_radius=10,
                                                    fg_color="#CFDBE4",
                                                    progress_color="#3276CF"
                                                    )
        progress_bar.set(percentage / 100)
        progress_bar.grid(row=1, column=0, padx=10, pady=20)

        percentage_label = customtkinter.CTkLabel(pt_frame, text=f'{percentage}%',
                                                  text_color="#6895B2")
        percentage_label.grid(row=1, column=1, sticky='w')

        # modules completed
        modules_frame = customtkinter.CTkFrame(self)
        modules_frame.configure(fg_color="transparent")
        modules_frame.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        modules_label = customtkinter.CTkLabel(modules_frame, text="Modules Completed",
                                               text_color="#6895B2",
                                               font=("Cascadia Mono Bold", 16))
        modules_label.grid(row=0, column=0, padx=10, sticky="w")

        module_frame = customtkinter.CTkFrame(modules_frame,
                                              fg_color="#A6D1E8",
                                              corner_radius=10)
        module_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        for i in range(len(self.completed_modules)):
            module = self.system_storage.get_module_data(self.completed_modules[i][0])
            score = self.completed_modules[i][3]

            module_completed = customtkinter.CTkLabel(module_frame,
                                                      text=f'Module ({module.get_module_id()}) '
                                                           f'{module.get_module_name()}',
                                                      font=("Calibri Bold", 14),
                                                      text_color="white")
            module_completed.grid(row=i, column=0, padx=20, pady=5, sticky="w")

            score = customtkinter.CTkLabel(module_frame,
                                           text=f'Score: {score} / 3',
                                           text_color="#6895B2",
                                           font=("Cascadia Code Bold", 14),)
            score.grid(row=i, column=1, padx=20, pady=5, sticky="e")

        # badges frame
        badges_frame = customtkinter.CTkFrame(self)
        badges_frame.configure(fg_color="transparent")
        badges_frame.grid(row=13, column=0, padx=20, pady=10, sticky="w")

        badge_title = customtkinter.CTkLabel(badges_frame,
                                             text="Badges Earned",
                                             text_color="#6895B2",
                                             font=("Cascadia Mono Bold", 16))
        badge_title.grid(row=0, column=0, padx=10, sticky="w")

        # badges display
        for i in range(len(self.badge_earned_list)):
            badge = self.badge_earned_list[i]

            if badge[2] == "Code Cadet":
                badge_label = tk.Label(badges_frame,
                                       image=self.badge_display_one,
                                       borderwidth=0,
                                       background="#FAFAFA"

                                       )
                badge_label.grid(row=1, column=i, padx=20, pady=10)

                earned_date = customtkinter.CTkLabel(badges_frame,
                                                     text=f'Challenge 1 Completion\n'
                                                          f'Date: {badge[3]}',
                                                     text_color="#6895B2")
                earned_date.grid(row=2, column=i, padx=20, pady=5)

            elif badge[2] == "Junior Coder":
                badge_label = tk.Label(badges_frame,
                                       image=self.badge_display_two,
                                       borderwidth=0,
                                       background="#FAFAFA"
                                       )
                badge_label.grid(row=1, column=i, padx=20, pady=10)

                earned_date = customtkinter.CTkLabel(badges_frame,
                                                     text=f'Challenge 2 Completion\n'
                                                          f'Date: {badge[3]}',
                                                     text_color="#6895B2")
                earned_date.grid(row=2, column=i, padx=20, pady=5)

            elif badge[2] == "Logic Master":
                badge_label = tk.Label(badges_frame,
                                       image=self.badge_display_three,
                                       borderwidth=0,
                                       background="#FAFAFA"
                                       )
                badge_label.grid(row=1, column=i, padx=20, pady=10)

                earned_date = customtkinter.CTkLabel(badges_frame,
                                                     text=f'Challenge 3 Completion\n'
                                                          f'Date: {badge[3]}',
                                                     text_color="#6895B2")
                earned_date.grid(row=2, column=i, padx=20, pady=5)

