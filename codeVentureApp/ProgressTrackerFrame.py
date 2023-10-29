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
        self.badge_display_one = tk.PhotoImage(file='images/badge1.png')
        self.badge_display_two = tk.PhotoImage(file='images/badge2.png')
        self.badge_display_three = tk.PhotoImage(file='images/badge3.png')
        self.badge_list = [self.badge_display_one, self.badge_display_two, self.badge_display_three]
        self.system_storage = SystemStorage()

        (self.username, self.points,
         self.rank, self.percentage_completion) = self.system_storage.get_learner_progress(self.user.get_username())

        # self.welcome_frame.configure(fg_color="transparent")
        progress_label = customtkinter.CTkLabel(master=self,
                                                text='Progress Tracking',
                                                font=("Fixedsys", 24),
                                                text_color="#6895B2",
                                                anchor="w",
                                                # justify="left"
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
        progress_bar.set(self.percentage_completion / 100)
        progress_bar.grid(row=1, column=0, padx=10, pady=20)

        percentage_label = customtkinter.CTkLabel(pt_frame, text=f'{self.percentage_completion}%',
                                                  text_color="#6895B2")
        percentage_label.grid(row=1, column=1, sticky='w')

        # modules completed
        modules_frame = customtkinter.CTkFrame(self)
        modules_frame.configure(fg_color="transparent")
        modules_frame.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        modules_label = customtkinter.CTkLabel(modules_frame, text="Modules Completed",
                                               text_color="#6895B2",
                                               font=("Cascadia Mono Bold", 16))
        modules_label.grid(row=0, column=0, padx=10)

        # badges frame
        badges_frame = customtkinter.CTkFrame(self)
        badges_frame.configure(fg_color="transparent")
        badges_frame.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        badge_title = customtkinter.CTkLabel(badges_frame,
                                             text="Badges Earned",
                                             text_color="#6895B2",
                                             font=("Cascadia Mono Bold", 16))
        badge_title.grid(row=0, column=0, padx=10, sticky="w")

        # # badges display
        # for i in range(len(self.badge_list)):
        #     badge_label = tk.Label(badges_frame,
        #                            image=self.badge_list[i],
        #                            borderwidth=0,
        #                            )
        #     badge_label.grid(row=1, column=i, padx=10, pady=10)
