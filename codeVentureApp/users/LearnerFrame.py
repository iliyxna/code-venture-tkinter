import customtkinter
import tkinter as tk
from tkinter import messagebox

from codeVentureApp.ModulesFrame import ModuleFrame
from codeVentureApp.ProgressTrackerFrame import ProgressTrackerFrame
from codeVentureApp.SystemStorage import SystemStorage


class LearnerFrame(customtkinter.CTkFrame):
    def __init__(self, master, login_frame, user):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        self.master = master
        self.login_frame = login_frame
        self.modules_frame = None
        self.system_storage = SystemStorage()
        self.user = self.system_storage.get_user_by_username(user.get_username())
        self.robot_image = tk.PhotoImage(file='images/bmo_blue.png')
        self.snake_image = tk.PhotoImage(file='images/snake_bmo.png')

        (self.username, self.points,
         self.rank, self.percentage_completion) = self.system_storage.get_learner_progress(self.user.get_username())

        """""""""""""""""""""""""""
        SIDE NAVIGATION BAR FRAME
        """""""""""""""""""""""""""
        self.nav_bar = customtkinter.CTkFrame(self.master,
                                              fg_color="#6895B2",
                                              bg_color="#6895B2",
                                              corner_radius=0)
        self.nav_bar.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        logo_path = "images/cv.png"
        self.logo = tk.PhotoImage(file=logo_path)

        logo_label = tk.Label(self.nav_bar,
                              image=self.logo,
                              borderwidth=0,
                              anchor="center",
                              bg="#6895B2")
        logo_label.place(relx=0, rely=0.10, relwidth=self.nav_bar.winfo_width())

        # DASHBOARD BUTTON
        dashboard_option = customtkinter.CTkButton(self.nav_bar,
                                                   text="Dashboard",
                                                   height=30,
                                                   fg_color="transparent",
                                                   hover_color="#878787",
                                                   font=("Cascadia Mono Bold", 18),
                                                   corner_radius=0,
                                                   command=self.show_dashboard_frame
                                                   )
        dashboard_option.place(relx=0, rely=0.25, relwidth=self.nav_bar.winfo_width())  # Centered vertically

        # MODULES BUTTON
        module_option = customtkinter.CTkButton(self.nav_bar,
                                                text="Modules",
                                                height=30,
                                                fg_color="transparent",
                                                hover_color="#878787",
                                                font=("Cascadia Mono Bold", 18),
                                                command=self.show_modules_frame
                                                )
        module_option.place(relx=0, rely=0.35, relwidth=self.nav_bar.winfo_width())  # Centered vertically

        # CHALLENGES BUTTON
        challenge_option = customtkinter.CTkButton(self.nav_bar,
                                                   text="Challenges",
                                                   height=30,
                                                   fg_color="transparent",
                                                   hover_color="#878787",
                                                   font=("Cascadia Mono Bold", 18),
                                                   command=self.show_challenges_frame
                                                   )
        challenge_option.place(relx=0, rely=0.45, relwidth=self.nav_bar.winfo_width())  # Centered vertically

        logout = customtkinter.CTkButton(self.nav_bar,
                                         text="Sign Out",
                                         height=30,
                                         fg_color="transparent",
                                         hover_color="#878787",
                                         font=("Cascadia Mono Bold", 18),
                                         command=self.confirm_logout
                                         )
        logout.place(relx=0, rely=0.55, relwidth=self.nav_bar.winfo_width())  # Centered vertically

        """""""""""""""""
        MAIN LEARNER FRAME
        """""""""""""""""
        # Main learner frame to be replaced when nav menu option is clicked
        self.learner_frame = customtkinter.CTkFrame(self.master)
        self.learner_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.learner_frame.configure(fg_color="#C2D3DF", corner_radius=0)

        """""""""""""""""""""""""""
        Welcome user frame section
        """""""""""""""""""""""""""
        self.welcome_frame = customtkinter.CTkFrame(self.learner_frame,
                                                    corner_radius=20,
                                                    height=200,
                                                    fg_color="#6895B2")
        self.welcome_frame.place(relx=0.05, y=100, relwidth=0.65)

        bmo_label = tk.Label(self.welcome_frame,
                             image=self.robot_image,
                             borderwidth=0,
                             anchor="w",
                             bg="#2b2b2b")
        bmo_label.grid(rowspan=2, column=0, padx=20, pady=20, sticky="w")

        welcome_title = customtkinter.CTkLabel(master=self.welcome_frame,
                                               text=f'Welcome Back, {self.user.get_firstname()}!',
                                               font=("Fixedsys", 24),
                                               anchor="w",
                                               justify="left",
                                               # text_color="#6895B2"
                                               )
        welcome_title.grid(row=0, column=1, padx=20, pady=20, sticky="sw")

        welcome_message = customtkinter.CTkLabel(master=self.welcome_frame,
                                                 text=f'You have completed '
                                                      f'{self.percentage_completion}% '
                                                      f'of your modules.\n'
                                                      f'Take on some new modules and challenges to improve \nyour '
                                                      f'results!\n',
                                                 anchor="w",
                                                 justify="left",
                                                 # text_color="#6895B2"
                                                 )
        welcome_message.grid(row=1, column=1, padx=20, sticky="nw")

        """""""""""""""
        Progress Frame
        """""""""""""""
        # self.progress_frame = customtkinter.CTkFrame(self.learner_frame, corner_radius=20)
        self.progress_frame = ProgressTrackerFrame(self.learner_frame, self.user)

        self.progress_frame.place(relx=0.05, y=320, relwidth=0.65)

        """""""""""""""""""""""
        Profile frame section
        """""""""""""""""""""""
        self.profile_frame = customtkinter.CTkFrame(master=self.learner_frame,
                                                    fg_color="#6895B2",
                                                    corner_radius=0)
        self.profile_frame.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)

        profile_label = customtkinter.CTkLabel(master=self.profile_frame,
                                               text="USER PROFILE",
                                               font=("Cascadia Code Bold", 22))
        profile_label.place(relx=0, y=100, relwidth=self.profile_frame.winfo_width())

        # Set current frame
        self.current_frame = self.welcome_frame

        avatar_path = "images/avatar3.png"
        self.avatar = tk.PhotoImage(file=avatar_path)

        avatar_label = tk.Label(self.profile_frame,
                                image=self.avatar,
                                borderwidth=0,
                                anchor="center",
                                bg="#6895B2")

        avatar_label.place(relx=0, rely=0.22, relwidth=self.profile_frame.winfo_width())

        # User's full name
        name_label = customtkinter.CTkLabel(self.profile_frame,
                                            text="N A M E",
                                            font=("Cascadia Code Bold", 14),
                                            fg_color="#4E6F86",
                                            anchor="center"
                                            )
        name_label.place(relx=0, y=370, relwidth=self.nav_bar.winfo_width())

        name = customtkinter.CTkLabel(self.profile_frame,
                                      text=f"{self.user.get_firstname()} {self.user.get_lastname()}\n",
                                      font=("Arial", 14),
                                      anchor="center")
        name.place(relx=0, y=405, relwidth=self.nav_bar.winfo_width())

        # Username
        username_label = customtkinter.CTkLabel(self.profile_frame,
                                                text="U S E R N A M E",
                                                font=("Cascadia Code Bold", 14),
                                                fg_color="#4E6F86",
                                                anchor="center"
                                                )
        username_label.place(relx=0, y=455, relwidth=self.nav_bar.winfo_width())

        username = customtkinter.CTkLabel(self.profile_frame,
                                          text=f"@{self.username}\n",
                                          font=("Arial", 14),
                                          anchor="center")
        username.place(relx=0, y=490, relwidth=self.nav_bar.winfo_width())

        # User role
        role_label = customtkinter.CTkLabel(self.profile_frame,
                                            text='R O L E',
                                            font=("Cascadia Code Bold", 14),
                                            fg_color="#4E6F86",
                                            anchor="center"
                                            )
        role_label.place(relx=0, y=540, relwidth=self.nav_bar.winfo_width())

        role = customtkinter.CTkLabel(self.profile_frame,
                                      text="Learner\n",
                                      font=("Arial", 14),
                                      anchor="center")
        role.place(relx=0, y=575, relwidth=self.nav_bar.winfo_width())

        # User rank
        rank_label = customtkinter.CTkLabel(self.profile_frame,
                                            text="R A N K",
                                            font=("Cascadia Code Bold", 14),
                                            anchor="center",
                                            fg_color="#4E6F86",
                                            )
        rank_label.place(relx=0, y=625, relwidth=self.nav_bar.winfo_width())

        rank = customtkinter.CTkLabel(self.profile_frame,
                                      text=f"{self.rank}",
                                      font=("Arial", 14),
                                      anchor="center")
        rank.place(relx=0, y=660, relwidth=self.nav_bar.winfo_width())

    def back_to_login(self):
        """
        Method to navigate back to login page
        """
        self.place_forget()
        self.learner_frame.place_forget()
        self.nav_bar.place_forget()
        self.modules_frame.place_forget()
        # self.profile_frame.place_forget()
        # self.progress_frame.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def confirm_logout(self):
        """
        Method to show pop up for logout confirmation
        """
        result = messagebox.askyesno("Logout Confirmation", "Are you sure you want to sign out?")
        if result:
            self.back_to_login()

    def show_dashboard_frame(self):
        """
        Method to show the dashboard page (homepage for learner)
        """
        self.current_frame.place_forget()
        self.modules_frame.place_forget()
        self.current_frame = self.learner_frame
        self.learner_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.welcome_frame.place(relx=0.05, y=100, relwidth=0.65)

    def show_modules_frame(self):
        """
        Method to show the modules frame
        """
        self.learner_frame.place_forget()

        # Create account frame
        # modules_frame = customtkinter.CTkFrame(self.master)
        self.modules_frame = customtkinter.CTkScrollableFrame(self.master)
        self.modules_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.modules_frame.configure(fg_color="#C2D3DF",
                                     bg_color="#C2D3DF")

        self.current_frame = self.modules_frame

        # top frame
        intro_frame = customtkinter.CTkFrame(self.modules_frame,
                                             corner_radius=20,
                                             height=200,
                                             fg_color="#6895B2",
                                             )
        # intro_frame.place(relx=0.05, y=100, relwidth=0.9)
        intro_frame.grid(row=0, column=0, padx=30, pady=50, sticky="w")

        intro_title = customtkinter.CTkLabel(master=intro_frame,
                                             text=f'Welcome to the Magical World of Python Programming ✨',
                                             font=("Fixedsys", 24),
                                             anchor="sw",
                                             justify="left"
                                             )
        intro_title.grid(row=0, column=0, padx=30, pady=20, sticky="sw")

        intro_message = customtkinter.CTkLabel(master=intro_frame,
                                               text=f'Get ready to embark on an exciting journey into the realm of '
                                                    f'Python programming. Python is not just a snake; it\'s \n'
                                                    f'a magical language that allows you to create games, apps, and '
                                                    f'more, all while having tons of fun!\n\n'
                                                    f'So, what are you waiting for? Dive into the world of Python, '
                                                    f'select your modules, and let the coding adventures begin. '
                                                    f'\nHappy coding for kids! 🐍\n',
                                               anchor="nw",
                                               justify="left"
                                               )
        intro_message.grid(row=1, column=0, padx=30, pady=10, sticky="nw")

        snake_label = tk.Label(intro_frame,
                               image=self.snake_image,
                               borderwidth=0,
                               anchor="w",
                               bg="#6895B2")
        snake_label.grid(row=0, rowspan=2, column=1, padx=20, pady=20, sticky="w")
        # snake_label.grid
        # module selection frame
        selection_frame = customtkinter.CTkFrame(self.modules_frame,
                                                 corner_radius=20,
                                                 height=200,
                                                 fg_color="#FAFAFA",
                                                 )
        # selection_frame.place(relx=0.05, rely=0.48, relwidth=0.9)
        selection_frame.grid(row=1, column=0, padx=30, pady=20, sticky="w")

        select_label = customtkinter.CTkLabel(selection_frame,
                                              text='Select Your Module',
                                              font=("Fixedsys", 24),
                                              text_color="#6895B2",
                                              anchor="sw",
                                              )

        select_label.grid(row=0, column=0, padx=30, pady=30, sticky="sw")

        for i in range(2):
            module_frame = ModuleFrame(selection_frame, i)
            module_frame.grid(row=i + 1, column=0, padx=30, pady=10, sticky="nw")

    def show_challenges_frame(self):
        """
        Method to show the challenges frame
        """
        self.current_frame.place_forget()
        self.modules_frame.place_forget()
