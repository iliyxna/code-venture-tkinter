import customtkinter
import tkinter as tk
from tkinter import messagebox


class LearnerFrame(customtkinter.CTkFrame):
    def __init__(self, master, login_frame, user):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        self.master = master
        self.login_frame = login_frame
        self.user = user

        """""""""""""""""""""""""""
        SIDE NAVIGATION BAR FRAME
        """""""""""""""""""""""""""
        self.nav_bar = customtkinter.CTkFrame(self.master)
        self.nav_bar.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        logo_path = "images/codeventure_logo.png"
        self.logo = tk.PhotoImage(file=logo_path)

        logo_label = tk.Label(self.nav_bar,
                              image=self.logo,
                              borderwidth=0,
                              anchor="center",
                              bg="#2b2b2b")
        # logo_label.grid(row=0, column=0, padx=5, pady=40)
        logo_label.place(relx=0, rely=0.10, relwidth=self.nav_bar.winfo_width())

        # DASHBOARD BUTTON
        dashboard_option = customtkinter.CTkButton(self.nav_bar,
                                                   text="Dashboard",
                                                   height=30,
                                                   fg_color="transparent",
                                                   hover_color="#878787",
                                                   font=("Cascadia Mono Bold", 18),
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
        self.learner_frame.configure(fg_color="transparent")

        """""""""""""""""""""""""""
        Welcome user frame section
        """""""""""""""""""""""""""
        self.welcome_frame = customtkinter.CTkFrame(self.learner_frame,
                                                    corner_radius=20,
                                                    height=200)

        self.welcome_frame.place(relx=0.05, y=100, relwidth=0.65)

        welcome_title = customtkinter.CTkLabel(master=self.welcome_frame,
                                               text=f'Welcome Back, {self.user.get_firstname()}!',
                                               font=("Fixedsys", 24),
                                               anchor="w",
                                               justify="left"
                                               )
        welcome_title.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        welcome_message = customtkinter.CTkLabel(master=self.welcome_frame,
                                                 text=f'You have completed '
                                                      f'{self.user.get_percentage_completion()}% '
                                                      f'of your modules.\n'
                                                      f'Take on some new modules and challenges to improve your '
                                                      f'results!\n',
                                                 anchor="w",
                                                 justify="left"
                                                 )
        welcome_message.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        """""""""""""""
        Progress Frame
        """""""""""""""
        self.progress_frame = customtkinter.CTkFrame(self.learner_frame, corner_radius=20)

        self.progress_frame.place(relx=0.05, y=280, relwidth=0.65)

        # self.welcome_frame.configure(fg_color="transparent")
        progress_label = customtkinter.CTkLabel(master=self.progress_frame,
                                               text='Track Your Progress',
                                               font=("Fixedsys", 23),
                                               anchor="w",
                                               justify="left"
                                               )
        progress_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        """""""""""""""""""""""
        Profile frame section
        """""""""""""""""""""""
        self.profile_frame = customtkinter.CTkFrame(master=self.learner_frame)
        self.profile_frame.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)

        profile_label = customtkinter.CTkLabel(master=self.profile_frame,
                                               text="USER PROFILE",
                                               font=("Cascadia Mono Bold", 16))
        # profile_label.place(relx=0, y=100, relwidth=self.profile_frame.winfo_width())
        profile_label.place(relx=0, y=100, relwidth=self.profile_frame.winfo_width())

        # Set current frame
        self.current_frame = self.welcome_frame

        avatar_path = "images/avatar1.png"
        self.avatar = tk.PhotoImage(file=avatar_path)

        avatar_label = tk.Label(self.profile_frame,
                                image=self.avatar,
                                borderwidth=0,
                                anchor="center",
                                bg="#2b2b2b")

        avatar_label.place(relx=0, y=160, relwidth=self.nav_bar.winfo_width())
        # avatar_label.place(relx=0, rely=0.18, relwidth=self.nav_bar.winfo_width())

        # User's full name
        name_label = customtkinter.CTkLabel(self.profile_frame,
                                            text="N A M E",
                                            font=("Cascadia Code Bold", 14),
                                            anchor="center"
                                            )
        name_label.place(relx=0, y=370, relwidth=self.nav_bar.winfo_width())

        name = customtkinter.CTkLabel(self.profile_frame,
                                      text=f"{self.user.get_firstname()} {self.user.get_lastname()}",
                                      font=("Arial", 14),
                                      anchor="center")
        name.place(relx=0, y=400, relwidth=self.nav_bar.winfo_width())

        # Username
        username_label = customtkinter.CTkLabel(self.profile_frame,
                                                text="U S E R N A M E",
                                                font=("Cascadia Code Bold", 14),
                                                anchor="center"
                                                )
        username_label.place(relx=0, y=450, relwidth=self.nav_bar.winfo_width())

        username = customtkinter.CTkLabel(self.profile_frame,
                                          text=f"@{self.user.get_username()}",
                                          font=("Arial", 14),
                                          anchor="center")
        username.place(relx=0, y=480, relwidth=self.nav_bar.winfo_width())

        # User role
        role_label = customtkinter.CTkLabel(self.profile_frame,
                                            text='R O L E',
                                            font=("Cascadia Code Bold", 14),
                                            anchor="center"
                                            )
        role_label.place(relx=0, y=530, relwidth=self.nav_bar.winfo_width())

        role = customtkinter.CTkLabel(self.profile_frame,
                                      text="Learner",
                                      font=("Arial", 14),
                                      anchor="center")
        role.place(relx=0, y=560, relwidth=self.nav_bar.winfo_width())

        # User rank
        rank_label = customtkinter.CTkLabel(self.profile_frame,
                                            text="R A N K",
                                            font=("Cascadia Code Bold", 14),
                                            anchor="center"
                                            )
        rank_label.place(relx=0, y=610, relwidth=self.nav_bar.winfo_width())

        rank = customtkinter.CTkLabel(self.profile_frame,
                                      text=f"{self.user.get_rank().name}",
                                      font=("Arial", 14),
                                      anchor="center")
        rank.place(relx=0, y=640, relwidth=self.nav_bar.winfo_width())

    def back_to_login(self):
        """
        Method to navigate back to login page
        """
        self.place_forget()
        self.learner_frame.place_forget()
        self.nav_bar.place_forget()
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
        self.learner_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.welcome_frame.place(relx=0.05, y=100, relwidth=0.65)
        # self.progress_frame.place(relx=0.05, y=280, relwidth=0.65)
        # self.profile_frame.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)

    def show_modules_frame(self):
        """
        Method to show the modules frame
        """
        # self.current_frame.place_forget()
        # self.profile_frame.place_forget()
        # self.progress_frame.place_forget()
        self.learner_frame.place_forget()
        # self.learner_frame.grid(row=0, column=1, padx=20, pady=10)

    def show_challenges_frame(self):
        """
        Method to show the challenges frame
        """
        # self.current_frame.place_forget()
        # self.profile_frame.place_forget()
        # self.progress_frame.place_forget()
        self.learner_frame.place_forget()
        # self.learner_frame.grid(row=0, column=1, padx=20, pady=10)
