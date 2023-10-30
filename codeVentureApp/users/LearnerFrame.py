import customtkinter
import tkinter as tk
from tkinter import messagebox

from codeVentureApp.ModulesFrame import ModuleFrame
from codeVentureApp.ChallengeFrame import ChallengeFrame
from codeVentureApp.ProgressTrackerFrame import ProgressTrackerFrame
from codeVentureApp.SystemStorage import SystemStorage
from codeVentureApp.utilities.Rank import Rank


class LearnerFrame(customtkinter.CTkFrame):
    def __init__(self, master, login_frame, user):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        self.master = master
        self.login_frame = login_frame
        self.modules_frame = None
        self.challenge_frame = None
        self.system_storage = SystemStorage()
        self.user = self.system_storage.get_user_by_username(user.get_username())

        # import images
        self.robot_image = tk.PhotoImage(file='images/bmo_blue.png')
        self.snake_image = tk.PhotoImage(file='images/snake_bmo.png')
        self.controller_image = tk.PhotoImage(file='images/bmo-grass.png')
        self.dance_image = tk.PhotoImage(file='images/bmo_dance.png')

        # retrieve from db
        (self.username, self.points,
         self.rank, self.percentage_completion) = self.system_storage.get_learner_progress(self.user.get_username())

        # attributes for support frame images
        self.recommendation_image = None
        self.badge_doc_image = None
        self.challenge_image = None
        self.quiz_image = None
        self.tutorial_image = None
        self.module_image = None
        self.dashboard_image = None
        self.support_frame = None

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

        # SUPPORT DESK BUTTON
        help_option = customtkinter.CTkButton(self.nav_bar,
                                              text="Support Desk",
                                              height=30,
                                              fg_color="transparent",
                                              hover_color="#878787",
                                              font=("Cascadia Mono Bold", 18),
                                              command=self.show_support_frame
                                              )
        help_option.place(relx=0, rely=0.55, relwidth=self.nav_bar.winfo_width())  # Centered vertically

        # LOGOUT BUTTON
        logout = customtkinter.CTkButton(self.nav_bar,
                                         text="Sign Out",
                                         height=30,
                                         fg_color="transparent",
                                         hover_color="#878787",
                                         font=("Cascadia Mono Bold", 18),
                                         command=self.confirm_logout
                                         )
        logout.place(relx=0, rely=0.65, relwidth=self.nav_bar.winfo_width())  # Centered vertically

        """""""""""""""""
        MAIN LEARNER FRAME
        """""""""""""""""
        # Main learner frame to be replaced when other nav menu option is clicked
        self.learner_frame = customtkinter.CTkScrollableFrame(self.master)
        self.learner_frame.place(relx=0.2, rely=0, relwidth=0.6, relheight=1)
        self.learner_frame.configure(fg_color="#C2D3DF", corner_radius=0)

        """""""""""""""""""""""""""
        Welcome user frame section
        """""""""""""""""""""""""""
        self.welcome_frame = customtkinter.CTkFrame(self.learner_frame,
                                             corner_radius=20,
                                             height=200,
                                             fg_color="#6895B2",
                                             )
        self.welcome_frame.grid(row=0, column=0, padx=30, pady=50, sticky="ew")

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
        welcome_title.grid(row=0, column=1, padx=20, pady=20, sticky="sew")

        self.completion_percentage = 0.0
        if self.system_storage.get_learner_modules(self.user.get_username()) is not None:
            completed_count = len(self.system_storage.get_learner_modules(self.user.get_username()))
            self.completion_percentage =(completed_count/10)*100

        welcome_message = customtkinter.CTkLabel(master=self.welcome_frame,
                                                 text=f'You have completed '
                                                      f'{self.completion_percentage}% of your exciting learning adventures!\n\n'
                                                      f'But guess what? There\'s a whole world of knowledge out there waiting for you!'
                                                      f' Get \nready to embark on new modules and thrilling challenges to boost your skills and \nsuperpowers. '
                                                      f'Unleash your inner genius and become a learning superstar!\n\n'
                                                      f'Are you ready to dive into the magic of learning? Let\'s do this! ✨👾\n',
                                                 anchor="w",
                                                 justify="left",
                                                 )
        welcome_message.grid(row=1, column=1, padx=20, sticky="new")

        """""""""""""""
        Progress Frame
        """""""""""""""

        # self.progress_frame = customtkinter.CTkFrame(self.learner_frame, corner_radius=20)
        self.progress_frame = ProgressTrackerFrame(self.learner_frame, self.user)
        self.progress_frame.grid(row=1, column=0, padx=30, pady=20, sticky="ew")
        # self.progress_frame.place(relx=0.05, y=320, relwidth=0.65)

        """""""""""""""
        Recommendation Frame
        """""""""""""""
        # Retrieve all modules and completed modules from the database
        self.all_modules = self.system_storage.get_all_modules()
        self.completed_modules = self.system_storage.get_learner_modules(self.user.get_username())

        self.next_module = None

        # Find the first uncompleted module
        for module in self.all_modules:
            # Check if the module ID is not in the completed modules
            if module[0] not in [completed[0] for completed in self.completed_modules]:
                # If the module is not in completed modules, mark it as the next module
                self.next_module = module
                break

        if self.next_module is not None:
            self.recommend_frame = customtkinter.CTkFrame(master=self.learner_frame,
                                                          fg_color="#FAFAFA",
                                                          corner_radius=20)

            self.recommend_frame.grid(row=2, column=0, padx=30, pady=20, sticky="ew")

            recommendation_label = customtkinter.CTkLabel(self.recommend_frame,
                                                          text='Recommended Module',
                                                          font=("Fixedsys", 24),
                                                          text_color="#6895B2",
                                                          anchor="w",
                                                          )
            recommendation_label.grid(row=0, column=0, padx=30, pady=20, sticky="w")

            next_module_frame = ModuleFrame(self.recommend_frame, self.next_module[0], self.user, True)
            next_module_frame.grid(row=1, column=0, padx=30, pady=10, sticky="new")

        """""""""""""""""""""""
        Profile frame section
        """""""""""""""""""""""
        self.profile_frame = customtkinter.CTkFrame(master=self.master,
                                                    fg_color="#6895B2",
                                                    corner_radius=0)
        self.profile_frame.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

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
        name_label.place(relx=0, y=370, relwidth=self.profile_frame.winfo_width())

        name = customtkinter.CTkLabel(self.profile_frame,
                                      text=f"{self.user.get_firstname()} {self.user.get_lastname()}\n",
                                      font=("Arial", 14),
                                      anchor="center")
        name.place(relx=0, y=405, relwidth=self.profile_frame.winfo_width())

        # Username
        username_label = customtkinter.CTkLabel(self.profile_frame,
                                                text="U S E R N A M E",
                                                font=("Cascadia Code Bold", 14),
                                                fg_color="#4E6F86",
                                                anchor="center"
                                                )
        username_label.place(relx=0, y=455, relwidth=self.profile_frame.winfo_width())

        username = customtkinter.CTkLabel(self.profile_frame,
                                          text=f"@{self.username}\n",
                                          font=("Arial", 14),
                                          anchor="center")
        username.place(relx=0, y=490, relwidth=self.profile_frame.winfo_width())

        # User role
        role_label = customtkinter.CTkLabel(self.profile_frame,
                                            text='R O L E',
                                            font=("Cascadia Code Bold", 14),
                                            fg_color="#4E6F86",
                                            anchor="center"
                                            )
        role_label.place(relx=0, y=540, relwidth=self.profile_frame.winfo_width())

        role = customtkinter.CTkLabel(self.profile_frame,
                                      text="Learner\n",
                                      font=("Arial", 14),
                                      anchor="center")
        role.place(relx=0, y=575, relwidth=self.profile_frame.winfo_width())

        # User rank
        rank_label = customtkinter.CTkLabel(self.profile_frame,
                                            text="R A N K",
                                            font=("Cascadia Code Bold", 14),
                                            anchor="center",
                                            fg_color="#4E6F86",
                                            )
        rank_label.place(relx=0, y=625, relwidth=self.profile_frame.winfo_width())

        # update rank
        if self.completion_percentage >= 80:
            self.system_storage.update_learner_rank(self.user.get_username(), Rank.EXPERT.name)
            self.rank = Rank.NOVICE.name
        elif self.completion_percentage >= 40:
            self.system_storage.update_learner_rank(self.user.get_username(), Rank.INTERMEDIATE.name)
            self.rank = Rank.INTERMEDIATE.name
        else:
            self.system_storage.update_learner_rank(self.user.get_username(), Rank.NOVICE.name)
            self.rank = Rank.INTERMEDIATE.name

        rank = customtkinter.CTkLabel(self.profile_frame,
                                      text=f"{self.rank}",
                                      font=("Arial", 14),
                                      anchor="center")
        rank.place(relx=0, y=660, relwidth=self.profile_frame.winfo_width())

    def back_to_login(self):
        """
        Method to navigate back to login page
        """
        self.place_forget()
        self.learner_frame.place_forget()
        self.profile_frame.place_forget()
        self.nav_bar.place_forget()

        if self.modules_frame is not None:
            self.modules_frame.place_forget()

        if self.challenge_frame is not None:
            self.challenge_frame.place_forget()

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

        if self.modules_frame is not None:
            self.modules_frame.place_forget()

        if self.challenge_frame is not None:
            self.challenge_frame.place_forget()

        if self.support_frame is not None:
            self.support_frame.place_forget()

        if self.recommend_frame is not None:
            self.recommend_frame.place_forget()

        self.current_frame = self.learner_frame
        self.learner_frame.place(relx=0.2, rely=0, relwidth=0.6, relheight=1)
        self.progress_frame = ProgressTrackerFrame(self.learner_frame, self.user)
        self.progress_frame.grid(row=1, column=0, padx=30, pady=20, sticky="ew")
        self.welcome_frame.grid(row=0, column=0, padx=30, pady=50, sticky="ew")

        # Retrieve all modules and completed modules from the database
        self.all_modules = self.system_storage.get_all_modules()
        self.completed_modules = self.system_storage.get_learner_modules(self.user.get_username())

        self.next_module = None

        # Find the first uncompleted module
        for module in self.all_modules:
            # Check if the module ID is not in the completed modules
            if module[0] not in [completed[0] for completed in self.completed_modules]:
                # If the module is not in completed modules, mark it as the next module
                self.next_module = module
                break

        if self.next_module is not None:
            self.recommend_frame = customtkinter.CTkFrame(master=self.learner_frame,
                                                          fg_color="#FAFAFA",
                                                          corner_radius=20)

            self.recommend_frame.grid(row=2, column=0, padx=30, pady=20, sticky="ew")

            recommendation_label = customtkinter.CTkLabel(self.recommend_frame,
                                                          text='Recommended Module',
                                                          font=("Fixedsys", 24),
                                                          text_color="#6895B2",
                                                          anchor="w",
                                                          )
            recommendation_label.grid(row=0, column=0, padx=30, pady=20, sticky="w")

            next_module_frame = ModuleFrame(self.recommend_frame, self.next_module[0], self.user, True)
            next_module_frame.grid(row=1, column=0, padx=30, pady=10, sticky="new")

    def show_modules_frame(self):
        """
        Method to show the modules frame
        """
        self.learner_frame.place_forget()

        # Create account frame
        # modules_frame = customtkinter.CTkFrame(self.master)
        self.modules_frame = customtkinter.CTkScrollableFrame(self.master,
                                                              fg_color="#C2D3DF",
                                                              bg_color="#C2D3DF"
                                                              )
        self.modules_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

        self.current_frame = self.modules_frame

        # top frame
        intro_frame = customtkinter.CTkFrame(self.modules_frame,
                                             corner_radius=20,
                                             height=200,
                                             fg_color="#6895B2",
                                             )
        # intro_frame.place(relx=0.05, y=100, relwidth=0.9)
        intro_frame.grid(row=0, column=0, padx=30, pady=50, sticky="ew")

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
        selection_frame.grid(row=1, column=0, padx=30, pady=20, sticky="ew")

        select_label = customtkinter.CTkLabel(selection_frame,
                                              text='Select Your Module',
                                              font=("Fixedsys", 24),
                                              text_color="#6895B2",
                                              anchor="sw",
                                              )

        select_label.grid(row=0, column=0, padx=30, pady=30, sticky="sw")

        for i in range(10):
            module_frame = ModuleFrame(selection_frame, i, self.user, False)
            module_frame.grid(row=i + 1, column=0, padx=30, pady=10, sticky="new")

    def show_challenges_frame(self):
        """
        Method to show the challenges frame
        """
        self.current_frame.place_forget()

        if self.modules_frame is not None:
            self.modules_frame.place_forget()

        if self.support_frame is not None:
            self.support_frame.place_forget()

        # Challenge Frame
        self.challenge_frame = customtkinter.CTkScrollableFrame(self.master)
        self.challenge_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.challenge_frame.configure(fg_color="#C2D3DF",
                                       bg_color="#C2D3DF")

        self.current_frame = self.challenge_frame

        # Introduction frame
        intro_frame = customtkinter.CTkFrame(self.challenge_frame,
                                             corner_radius=20,
                                             height=200,
                                             fg_color="#6895B2",
                                             )
        intro_frame.grid(row=0, column=0, padx=30, pady=50, sticky="ew")

        intro_title = customtkinter.CTkLabel(master=intro_frame,
                                             text=f'It\'s Challenge time : Unleash Your Potential ! 🚀\n',
                                             font=("Fixedsys", 24),
                                             anchor="sw",
                                             justify="left"
                                             )
        intro_title.grid(row=0, column=0, padx=30, pady=20, sticky="sw")

        intro_message = customtkinter.CTkLabel(master=intro_frame,
                                               text=f'Hey, young coders! Are you ready to explore fascinating coding '
                                                    f'quests?'
                                                    f'Plunge into the world of Python, choose\nyour challenges'
                                                    f' and let the'
                                                    f' coding adventures begin with fun tasks that will test your '
                                                    f'skills.\n\n'
                                                    f'Start collecting your badges by completing challenges'
                                                    f'\nGet set, code, and conquer! 🐍\n',
                                               anchor="nw",
                                               justify="left"
                                               )
        intro_message.grid(row=1, column=0, padx=30, pady=10, sticky="nw")
        controller_label = tk.Label(intro_frame,
                                    image=self.controller_image,
                                    borderwidth=0,
                                    anchor="w",
                                    bg="#6895B2")
        controller_label.grid(row=0, rowspan=2, column=1, padx=20, pady=20, sticky="w")

        # Challenge selection frame
        selection_frame = customtkinter.CTkFrame(self.challenge_frame,
                                                 corner_radius=20,
                                                 height=200,
                                                 fg_color="#FAFAFA",
                                                 )
        # selection_frame.place(relx=0.05, rely=0.48, relwidth=0.9)
        selection_frame.grid(row=1, column=0, padx=30, pady=20, sticky="ew")

        select_label = customtkinter.CTkLabel(selection_frame,
                                              text='Select Your Challenge : ',
                                              font=("Fixedsys", 24),
                                              text_color="#6895B2",
                                              anchor="sw",
                                              )

        select_label.grid(row=0, column=0, padx=30, pady=30, sticky="sw")

        for i in range(3):
            challenge_option_frame = ChallengeFrame(selection_frame, i, self.user.get_username())
            challenge_option_frame.grid(row=i + 1, column=0, padx=30, pady=10, sticky="new")

    def show_support_frame(self):
        """
        Method to show the help and documentation frame
        """
        self.current_frame.place_forget()

        if self.modules_frame is not None:
            self.modules_frame.place_forget()

        if self.challenge_frame is not None:
            self.challenge_frame.place_forget()

        # support frame
        self.support_frame = customtkinter.CTkScrollableFrame(self.master)
        self.support_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.support_frame.configure(fg_color="#C2D3DF",
                                     bg_color="#C2D3DF")

        self.current_frame = self.support_frame

        # Introduction frame
        intro_frame = customtkinter.CTkFrame(self.support_frame,
                                             corner_radius=20,
                                             height=200,
                                             fg_color="#6895B2",
                                             )
        intro_frame.grid(row=0, column=0, padx=30, pady=50, sticky="ew")

        intro_title = customtkinter.CTkLabel(master=intro_frame,
                                             text=f'CodeVenture Support & Learning Hub\n',
                                             font=("Fixedsys", 24),
                                             anchor="sw",
                                             justify="left"
                                             )
        intro_title.grid(row=0, column=0, padx=30, pady=20, sticky="sw")

        intro_message = customtkinter.CTkLabel(master=intro_frame,
                                               text=f'Welcome to the CodeVenture Support & Learning Hub! 🌟\n'
                                                    f'This page is your central destination for all the help, guidance, '
                                                    f'and learning resources'
                                                    f'you need to embark on \nan exciting journey '
                                                    f'through the world of coding. '
                                                    f'\nWhether you\'re a budding young coder,'
                                                    f'a supportive parent, or an enthusiastic educator, \n'
                                                    f'this hub is tailored to assist you every step of the way.',
                                               anchor="nw",
                                               justify="left"
                                               )
        intro_message.grid(row=1, column=0, padx=30, pady=10, sticky="nw")
        controller_label = tk.Label(intro_frame,
                                    image=self.dance_image,
                                    borderwidth=0,
                                    anchor="w",
                                    bg="#6895B2")
        controller_label.grid(row=0, rowspan=2, column=1, padx=20, pady=20, sticky="w")

        # dashboard frame
        dashboard_frame = customtkinter.CTkFrame(self.support_frame,
                                                 corner_radius=20,
                                                 height=200,
                                                 fg_color="#FAFAFA",
                                                 )
        dashboard_frame.grid(row=1, column=0, padx=30, pady=20, sticky="ew")

        dashboard_label = customtkinter.CTkLabel(dashboard_frame,
                                                 text='(1) Dashboard',
                                                 font=("Fixedsys", 24),
                                                 text_color="#6895B2",
                                                 anchor="sw",
                                                 )
        dashboard_label.grid(row=0, column=0, padx=30, pady=30, sticky="sw")

        self.dashboard_image = tk.PhotoImage(file='images/dashboard.png')
        dashboard_label2 = tk.Label(dashboard_frame,
                                    image=self.dashboard_image,
                                    borderwidth=0,
                                    anchor="w")
        dashboard_label2.grid(row=1, rowspan=2, column=0, padx=20, pady=20, sticky="w")

        dashboard_description = customtkinter.CTkLabel(dashboard_frame,
                                                       text=f'Profile Section: \n\n'
                                                            f'* Personal Details: See your name and unique username '
                                                            f'prominently displayed.\n'
                                                            f'* Role Recognition: Identify yourself as a dedicated '
                                                            f'"Learner"\n'
                                                            f'* Achievement Level: Track your progress and '
                                                            f'accomplishments to know where you stand.\n\n'
                                                            f'Progress Tracking:\n\n'
                                                            f'* Visual Progress: Keep an eye on your advancement '
                                                            f'through an progress bar.\n'
                                                            f'* Completed Modules: View the number of modules you\'ve '
                                                            f'conquered, indicating your learning journey\'s '
                                                            f'milestones.\n'
                                                            f'* Quiz Scores: Observe your scores, gauging your '
                                                            f'performance.\n'
                                                            f'* Badge Showcase: Proudly exhibit badges earned from '
                                                            f'successfully completing challenges, with each badge\n   '
                                                            f'accompanied by its completion date.\n',
                                                       font=("Fixedsys", 16),
                                                       text_color="#6895B2",
                                                       anchor="sw",
                                                       justify="left"
                                                       )

        dashboard_description.grid(row=4, column=0, padx=30, pady=30, sticky="sw")
        self.recommendation_image = tk.PhotoImage(file='images/recommendations.png')
        dashboard_label3 = tk.Label(dashboard_frame,
                                    image=self.recommendation_image,
                                    borderwidth=0,
                                    anchor="w")
        dashboard_label3.grid(row=5, rowspan=2, column=0, padx=20, pady=20, sticky="w")

        dashboard_description2 = customtkinter.CTkLabel(dashboard_frame,
                                                        text=f'Recommended Module Section : \n\n'
                                                             f'* This section is to recommend you the most relevant '
                                                             f'and beneficial module based on your learning journey',
                                                        font=("Fixedsys", 16),
                                                        text_color="#6895B2",
                                                        anchor="sw",
                                                        justify="left"
                                                        )

        dashboard_description2.grid(row=9, column=0, padx=30, pady=30, sticky="sw")

        # Module frame
        module_frame = customtkinter.CTkFrame(self.support_frame,
                                              corner_radius=20,
                                              height=200,
                                              fg_color="#FAFAFA",
                                              )
        module_frame.grid(row=2, column=0, padx=30, pady=20, sticky="ew")

        module_label = customtkinter.CTkLabel(module_frame,
                                              text='(2) Modules',
                                              font=("Fixedsys", 24),
                                              text_color="#6895B2",
                                              anchor="sw",
                                              )
        module_label.grid(row=0, column=0, padx=30, pady=30, sticky="sw")

        self.module_image = tk.PhotoImage(file='images/module.png')
        module_label2 = tk.Label(module_frame,
                                 image=self.module_image,
                                 borderwidth=0,
                                 anchor="w")
        module_label2.grid(row=1, rowspan=2, column=0, padx=20, pady=20, sticky="w")

        module_description = customtkinter.CTkLabel(module_frame,
                                                    text=f'Module Selection: \n\n'
                                                         f'* You are able to choose from a diverse selection of '
                                                         f'modules, each varying in difficulty levels.\n'
                                                         f'* To start a module, just click on the "Start" button',
                                                    font=("Fixedsys", 16),
                                                    text_color="#6895B2",
                                                    anchor="sw",
                                                    justify="left"
                                                    )

        module_description.grid(row=4, column=0, padx=30, pady=30, sticky="sw")

        self.tutorial_image = tk.PhotoImage(file='images/tutorial.png')
        tutorial_label2 = tk.Label(module_frame,
                                   image=self.tutorial_image,
                                   borderwidth=0,
                                   anchor="w")
        tutorial_label2.grid(row=5, rowspan=2, column=0, padx=20, pady=20, sticky="w")

        tutorial_description = customtkinter.CTkLabel(module_frame,
                                                      text=f'Tutorial: \n\n'
                                                           f'* The tutorial will be displayed according to the module\n'
                                                           f'* Attempt the quiz to evaluate and '
                                                           f'reinforce your acquired knowledge by clicking on the '
                                                           f'"Start Quiz" button.\n',
                                                      font=("Fixedsys", 16),
                                                      text_color="#6895B2",
                                                      anchor="sw",
                                                      justify="left"
                                                      )

        tutorial_description.grid(row=8, column=0, padx=30, pady=30, sticky="sw")

        self.quiz_image = tk.PhotoImage(file='images/quiz.png')
        quiz_label2 = tk.Label(module_frame,
                               image=self.quiz_image,
                               borderwidth=0,
                               anchor="w")
        quiz_label2.grid(row=10, rowspan=2, column=0, padx=20, pady=20, sticky="w")

        quiz_description = customtkinter.CTkLabel(module_frame,
                                                  text=f'Quiz: \n\n'
                                                       f'* Every module has its own quiz to test the your '
                                                       f'comprehension\n'
                                                       f'* Instant feedback is provided based on the your '
                                                       f'answer '
                                                       f'once you have clicked on the "Submit" button\n'
                                                       f'* Note that you cannot change your answer upon'
                                                       f'clicking the submit button!',
                                                  font=("Fixedsys", 16),
                                                  text_color="#6895B2",
                                                  anchor="sw",
                                                  justify="left"
                                                  )

        quiz_description.grid(row=14, column=0, padx=30, pady=30, sticky="sw")

        # Challenge frame
        challenge_frame = customtkinter.CTkFrame(self.support_frame,
                                                 corner_radius=20,
                                                 height=200,
                                                 fg_color="#FAFAFA",
                                                 )
        challenge_frame.grid(row=3, column=0, padx=30, pady=20, sticky="ew")

        challenge_label = customtkinter.CTkLabel(challenge_frame,
                                                 text='(3) Challenges',
                                                 font=("Fixedsys", 24),
                                                 text_color="#6895B2",
                                                 anchor="sw",
                                                 )
        challenge_label.grid(row=0, column=0, padx=30, pady=30, sticky="sw")

        self.challenge_image = tk.PhotoImage(file='images/challenge.png')
        challenge_label2 = tk.Label(challenge_frame,
                                    image=self.challenge_image,
                                    borderwidth=0,
                                    anchor="w")
        challenge_label2.grid(row=1, rowspan=2, column=0, padx=20, pady=20, sticky="w")

        challenge_description = customtkinter.CTkLabel(challenge_frame,
                                                       text=f'Challenge Selection: \n\n'
                                                            f'* You are able to choose from a diverse selection of '
                                                            f'challenges, each varying in difficulty levels.\n'
                                                            f'* To start a challenge, just click on the "Start" button\n',
                                                       font=("Fixedsys", 16),
                                                       text_color="#6895B2",
                                                       anchor="sw",
                                                       justify="left"
                                                       )

        challenge_description.grid(row=4, column=0, padx=30, pady=30, sticky="sw")

        self.badge_doc_image = tk.PhotoImage(file='images/badge_doc.png')
        badge_label2 = tk.Label(challenge_frame,
                                image=self.badge_doc_image,
                                borderwidth=0,
                                anchor="w")
        badge_label2.grid(row=5, rowspan=2, column=0, padx=20, pady=20, sticky="w")

        badge_description = customtkinter.CTkLabel(challenge_frame,
                                                   text=f'Badge Collection: \n\n'
                                                        f'* Once you have completed the challenge, dont forget to '
                                                        f'claim your badge by clicking the "Claim Your Badge" button '
                                                        f'\n',
                                                   font=("Fixedsys", 16),
                                                   text_color="#6895B2",
                                                   anchor="sw",
                                                   justify="left"
                                                   )

        badge_description.grid(row=9, column=0, padx=30, pady=30, sticky="sw")