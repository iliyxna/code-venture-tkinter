from codeVentureApp.PasswordRecoveryFrame import PasswordRecoveryFrame
from codeVentureApp.users.AdminFrame import AdminFrame
from codeVentureApp.users.EducatorFrame import EducatorFrame
from codeVentureApp.users.LearnerFrame import LearnerFrame
from codeVentureApp.SystemStorage import SystemStorage

import tkinter as tk
from tkinter import messagebox
import customtkinter

from codeVentureApp.users.ParentFrame import ParentFrame


class LoginFrame(customtkinter.CTkFrame):
    """
    Class that displays the login frame
    """
    def __init__(self, master):
        """
        Constructor
        """
        super().__init__(master=master)
        self.master = master
        self.user_storage = SystemStorage()

        # Store the logged-in user to be passed to child
        self.user = None  # set to None before login

        # To reset entries when change frame
        self.entry_widget_list = []
        self.current_frame = self

        # Frame configuration
        self.configure(fg_color="transparent")

        # Accessible frames from login frame
        self.learner_frame = None
        self.parent_frame = None
        self.educator_frame = None
        self.admin_frame = None
        self.password_recovery_frame = PasswordRecoveryFrame(self.master, self)

        # Label containing the welcome heading
        login_title = customtkinter.CTkLabel(master=self,
                                             text="Sign In",
                                             font=("Fixedsys", 24),
                                             text_color="#6895B2")
        login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        # Label to ask user for Username
        username_label = customtkinter.CTkLabel(master=self, text="Username: ",
                                                font=("Cascadia Mono Bold", 14),
                                                text_color="#6895B2"
                                                )
        username_label.grid(row=2, column=0, sticky=tk.EW, padx=10, pady=10)

        # Variable and input widget for username
        self.username = tk.StringVar()
        self.username_entry = customtkinter.CTkEntry(master=self,
                                                     textvariable=self.username,
                                                     fg_color="#EFF9FF",
                                                     text_color="#6895B2",
                                                     border_color="#6895B2",
                                                     )  # Entry field text (text box)
        self.username_entry.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)
        self.entry_widget_list.append(self.username_entry)

        password_label = customtkinter.CTkLabel(master=self, text="Password: ",
                                                font=("Cascadia Mono Bold",14),
                                                text_color="#6895B2")
        password_label.grid(row=3, column=0, sticky=tk.EW, padx=10, pady=10)

        # Variable and input widget for password
        self.password = tk.StringVar()
        self.password_entry = customtkinter.CTkEntry(master=self, textvariable=self.password, show='●',
                                                     fg_color="#EFF9FF",
                                                     text_color="#6895B2",
                                                     border_color="#6895B2",
                                                     )  # Show = '●'
        self.password_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)
        self.entry_widget_list.append(self.password_entry)

        login_button = customtkinter.CTkButton(master=self, text="Login",
                                               fg_color="#6895B2",
                                               command=self.authenticate_login)
        login_button.grid(row=4, column=0, padx=5, pady=10, sticky="W")

        forget_password_button = customtkinter.CTkButton(master=self, text="Forget Password",
                                                         fg_color="#6895B2",
                                                         command=self.show_pwd_recovery_frame)
        forget_password_button.grid(row=4, column=1, padx=5, pady=10, sticky="W")

        back_button = customtkinter.CTkButton(master=self, text="Back to Main Page",
                                              fg_color="#6895B2",
                                              command=self.back_to_main)
        back_button.grid(row=5, columnspan=2, padx=5, pady=10)

    def clear_entries(self):
        """
        Method to clear all the entries
        """
        for entry in self.entry_widget_list:
            entry.delete(0, tk.END)

    def clear_password(self):
        """
        Method to clear password entry
        """
        self.password_entry.delete(0, tk.END)

    def back_to_main(self):
        """
        Method to navigate back to main page
        """
        self.place_forget()
        self.master.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.clear_entries()

    def authenticate_login(self):
        """
        Method to authenticate user login
        """
        username = self.username.get()
        password = self.password.get()

        # user = self.system_storage.get_user(username, password)
        user = self.user_storage.get_user(username, password)
        # temporary, modify later

        if user is not None:
            self.user = user
            # print(user.get_role())
            # output a Label to show login successful in a pop-up
            messagebox.showinfo(title="Login Successful", message="Login Successful!")
            # print(user.get_role())
            if user.get_role() == "Learner":
                self.learner_frame = LearnerFrame(master=self.master, login_frame=self, user=user)
                self.place_forget()
                self.learner_frame.place(relx=0, rely=0)
            elif user.get_role() == "Parent":
                self.parent_frame = ParentFrame(master=self.master, login_frame=self, user=user)
                self.place_forget()
                self.parent_frame.place(relx=0, rely=0)
            if user.get_role() == "Educator":
                self.educator_frame = EducatorFrame(master=self.master, login_frame=self, user=user)
                self.place_forget()
                self.educator_frame.place(relx=0, rely=0)
            if user.get_role() == "Admin":
                self.admin_frame = AdminFrame(master=self.master, login_frame=self, user=user)
                self.place_forget()
                self.admin_frame.place(relx=0, rely=0)

            # Clear all the entries after login
            self.clear_entries()

        else:
            messagebox.showerror("Login Failed", "Login failed. Invalid username or password.")

    def show_pwd_recovery_frame(self):
        """
        Method to recover password
        """
        self.place_forget()
        self.clear_entries()
        self.password_recovery_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def get_user(self):
        """
        Method to get the user that is logged in
        """
        return self.username.get()
