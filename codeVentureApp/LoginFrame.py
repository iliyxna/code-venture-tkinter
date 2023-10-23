from codeVentureApp.users.LearnerFrame import LearnerFrame
from codeVentureApp.LoginSystem import PasswordRecoveryFrame
from codeVentureApp.SystemStorage import SystemStorage
import tkinter as tk
from tkinter import messagebox
import customtkinter


class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.system_storage = SystemStorage()

        # Store the logged-in user to be passed to child
        self.user = None  # set to None before login

        # To reset entries when change frame
        self.entry_widget_list = []
        self.current_frame = self

        # Frame configuration
        self.configure(fg_color="transparent")

        # Accessible frames from login frame
        self.learner_frame = None
        self.password_recovery_frame = PasswordRecoveryFrame(self.master, self)

        # Label containing the welcome heading
        login_title = customtkinter.CTkLabel(master=self,
                                             text="Sign In",
                                             font=("Fixedsys", 20))
        login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        # Label to ask user for Username
        username_label = customtkinter.CTkLabel(master=self, text="Username: ")
        username_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and input widget for username
        self.username = tk.StringVar()
        self.username_entry = customtkinter.CTkEntry(master=self,
                                                     textvariable=self.username)  # Entry field text (text box)
        self.username_entry.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)
        self.entry_widget_list.append(self.username_entry)

        password_label = customtkinter.CTkLabel(master=self, text="Password: ")
        password_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and input widget for password
        self.password = tk.StringVar()
        self.password_entry = customtkinter.CTkEntry(master=self, textvariable=self.password, show='●')  # Show = '●'
        self.password_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)
        self.entry_widget_list.append(self.password_entry)

        login_button = customtkinter.CTkButton(master=self, text="Login", command=self.authenticate_login)
        login_button.grid(row=4, column=0, padx=5, pady=10)
        # login_button.pack()

        forget_password_button = customtkinter.CTkButton(master=self, text="Forget Password",
                                                         command=self.show_pwd_recovery_frame)
        forget_password_button.grid(row=4, column=1, padx=5, pady=10)

        back_button = customtkinter.CTkButton(master=self, text="Back to Main Page",
                                              command=self.back_to_main)
        back_button.grid(row=5, columnspan=2, padx=5, pady=10)

    # def switch_frame(self, new_frame):
    #     self.current_frame.place_forget()
    #     self.current_frame = new_frame  # Set the new frame as the current frame
    #     self.current_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def clear_entries(self):
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

        user = self.system_storage.get_user(username, password)
        # temporary, modify later
        if user is not None:
            self.user = user
            # output a Label to show login successful in a pop-up
            messagebox.showinfo(title="Login Successful", message="Login Successful!")
            # print(user.get_role())
            if user.get_role() == "Learner":
                self.learner_frame = LearnerFrame(self.master, self, self.user)
                self.place_forget()
                self.learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            else:
                print("Under Construction")
            self.clear_entries()

        else:
            messagebox.showerror("Login Failed", "Login failed. Invalid username or password.")

    def show_pwd_recovery_frame(self):
        self.place_forget()
        self.clear_entries()
        self.password_recovery_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def get_user(self):
        return self.username.get()