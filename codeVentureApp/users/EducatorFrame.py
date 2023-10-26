from tkinter import messagebox

import customtkinter
import tkinter as tk

from codeVentureApp.SystemStorage import SystemStorage


class EducatorFrame(customtkinter.CTkFrame):
    def __init__(self, master, login_frame, user):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        self.master = master
        self.login_frame = login_frame
        self.user = user
        self.system_storage = SystemStorage()

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

        # CLASS OVERVIEW BUTTON
        class_overview = customtkinter.CTkButton(self.nav_bar,
                                                 text="Class Overview",
                                                 height=30,
                                                 fg_color="transparent",
                                                 hover_color="#878787",
                                                 font=("Cascadia Mono Bold", 18),
                                                 # command=
                                                 )
        class_overview.place(relx=0, rely=0.35, relwidth=self.nav_bar.winfo_width())  # Centered vertically

        # FORUM BUTTON
        forum_button = customtkinter.CTkButton(self.nav_bar,
                                               text="Discussion Forum",
                                               height=30,
                                               fg_color="transparent",
                                               hover_color="#878787",
                                               font=("Cascadia Mono Bold", 18),
                                               # command=
                                               )
        forum_button.place(relx=0, rely=0.45, relwidth=self.nav_bar.winfo_width())  # Centered vertically

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
        MAIN EDUCATOR FRAME
        """""""""""""""""
        # Main parent frame to be replaced when nav menu option is clicked
        self.educator_frame = customtkinter.CTkFrame(self.master)
        self.educator_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.educator_frame.configure(fg_color="transparent")

        """""""""""""""""""""""""""
        Welcome user frame section
        """""""""""""""""""""""""""
        self.welcome_frame = customtkinter.CTkFrame(self.educator_frame,
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
                                                 text=f'As an educator, you oversee one module topic. '
                                                      f'You can view class summaries, '
                                                      '\nlearner results, and participate in module discussions. '
                                                      'Start by exploring your \neducator dashboard and '
                                                      'empowering young minds!\n',
                                                 anchor="w",
                                                 justify="left"
                                                 )
        welcome_message.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.current_frame = self.educator_frame

        """""""""""""""
        Class overview
        """""""""""""""
        self.summary_frame = customtkinter.CTkFrame(self.educator_frame,
                                                    corner_radius=20)

        self.summary_frame.place(relx=0.05, y=280, relwidth=0.65)

        class_summary_label = customtkinter.CTkLabel(master=self.summary_frame,
                                                     text='Summary of Class Overview',
                                                     font=("Fixedsys", 23),
                                                     anchor="w",
                                                     justify="left"
                                                     )
        class_summary_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        """""""""""""""""""""""
        Profile frame section
        """""""""""""""""""""""
        self.profile_frame = customtkinter.CTkFrame(master=self.educator_frame)
        self.profile_frame.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)

        profile_label = customtkinter.CTkLabel(master=self.profile_frame,
                                               text="USER PROFILE",
                                               font=("Cascadia Mono Bold", 16))
        profile_label.place(relx=0, y=100, relwidth=self.profile_frame.winfo_width())

        # Set current frame
        self.current_frame = self.welcome_frame

        avatar_path = "images/educator1.png"
        self.avatar = tk.PhotoImage(file=avatar_path)

        avatar_label = tk.Label(self.profile_frame,
                                image=self.avatar,
                                borderwidth=0,
                                anchor="center",
                                bg="#2b2b2b")

        avatar_label.place(relx=0, rely=0.2, relwidth=self.nav_bar.winfo_width())

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

        # Module in charge
        module_label = customtkinter.CTkLabel(self.profile_frame,
                                            text="M O D U L E",
                                            font=("Cascadia Code Bold", 14),
                                            anchor="center"
                                            )
        module_label.place(relx=0, y=610, relwidth=self.nav_bar.winfo_width())

        module = customtkinter.CTkLabel(self.profile_frame,
                                      text=f"Sample Module",
                                      font=("Arial", 14),
                                      anchor="center")
        module.place(relx=0, y=640, relwidth=self.nav_bar.winfo_width())

    def show_dashboard_frame(self):
        """
        Method to show the dashboard page (homepage for learner)
        """
        self.current_frame.place_forget()
        self.educator_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

    def confirm_logout(self):
        """
        Method to show pop up for logout confirmation
        """
        result = messagebox.askyesno("Logout Confirmation", "Are you sure you want to sign out?")
        if result:
            self.back_to_login()

    def back_to_login(self):
        """
        Method to navigate back to login page
        """
        self.place_forget()
        self.educator_frame.place_forget()
        self.nav_bar.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_class_overview(self):
        """
        Method to navigate to class overview frame
        """
        self.educator_frame.place_forget()
