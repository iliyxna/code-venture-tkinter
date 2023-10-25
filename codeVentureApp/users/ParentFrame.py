import customtkinter
import tkinter as tk
from tkinter import messagebox

from codeVentureApp.SystemStorage import SystemStorage


class ParentFrame(customtkinter.CTkFrame):
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

        logout = customtkinter.CTkButton(self.nav_bar,
                                         text="Sign Out",
                                         height=30,
                                         fg_color="transparent",
                                         hover_color="#878787",
                                         font=("Cascadia Mono Bold", 18),
                                         command=self.confirm_logout
                                         )
        logout.place(relx=0, rely=0.35, relwidth=self.nav_bar.winfo_width())  # Centered vertically

        """""""""""""""""
        MAIN PARENT FRAME
        """""""""""""""""
        # Main parent frame to be replaced when nav menu option is clicked
        self.parent_frame = customtkinter.CTkFrame(self.master)
        self.parent_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.parent_frame.configure(fg_color="transparent")

        """""""""""""""""""""""""""
         Welcome user frame section
        """""""""""""""""""""""""""
        self.welcome_frame = customtkinter.CTkFrame(self.parent_frame,
                                                    corner_radius=20,
                                                    height=200)

        self.welcome_frame.place(relx=0.05, y=100, relwidth=0.7)

        welcome_title = customtkinter.CTkLabel(master=self.welcome_frame,
                                               text=f'Welcome Back, {self.user.get_firstname()}!',
                                               font=("Fixedsys", 24),
                                               anchor="w",
                                               justify="left"
                                               )
        welcome_title.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        if self.user.get_child_username() is None:
            welcome_message = customtkinter.CTkLabel(master=self.welcome_frame,
                                                     text=f'To get started, add your child\'s account to monitor'
                                                          ' their progress now! ',
                                                     anchor="w",
                                                     justify="left"
                                                     )
            welcome_message.grid(row=1, column=0, padx=20, pady=0, sticky="w")

            add_child_button = customtkinter.CTkButton(master=self.welcome_frame,
                                                       text="Add Child\'s Username Here",
                                                       hover_color="#878787",
                                                       )  # add command
            add_child_button.grid(row=2, column=0, padx=20, pady=20, sticky="w")

        else:
            child_username = self.user.get_child_username()
            welcome_message = customtkinter.CTkLabel(master=self.welcome_frame,
                                                     text=f'Your child @{child_username} has completed '
                                                          f'{child_username.get_percentage_completion()}% '
                                                          f'of their modules.\n',
                                                     anchor="w",
                                                     justify="left"
                                                     )
            welcome_message.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        self.current_frame = self.parent_frame

    def show_dashboard_frame(self):
        """
        Method to show the dashboard page (homepage for learner)
        """
        self.current_frame.place_forget()
        self.parent_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

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
        self.parent_frame.place_forget()
        self.nav_bar.place_forget()
        # self.profile_frame.place_forget()
        # self.progress_frame.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
