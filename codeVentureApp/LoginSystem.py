# tkinter import
import tkinter as tk
from tkinter import messagebox
import customtkinter

from users.Educator import Educator
from users.Learner import LearnerFrame, Learner
from SystemStorage import SystemStorage
from users.Parent import Parent
from utilities.Role import Role


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
                                                         command=self.recover_password)
        forget_password_button.grid(row=4, column=1, padx=5, pady=10)

        back_button = customtkinter.CTkButton(master=self, text="Back to Main Page",
                                              command=self.back_to_main)
        back_button.grid(row=5, columnspan=2, padx=5, pady=10)

    def switch_frame(self, new_frame):
        self.current_frame.place_forget()
        self.current_frame = new_frame  # Set the new frame as the current frame
        self.current_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_login_frame(self):
        self.master.switch_frame(self)

    def clear_entries(self):
        for entry in self.entry_widget_list:
            entry.delete(0, tk.END)

    def clear_password(self):
        self.password_entry.delete(0, tk.END)

    def back_to_main(self):
        self.master.show_main_page()
        self.clear_entries()

    def authenticate_login(self):
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
                self.master.switch_frame(self.learner_frame)
            else:
                print("Under Construction")
            self.clear_entries()

        else:
            messagebox.showerror("Login Failed", "Login failed. Invalid username or password.")

    def recover_password(self):
        self.clear_entries()
        self.master.switch_frame(self.password_recovery_frame)

    def get_user(self):
        return self.username.get()

class RegisterFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.system_storage = SystemStorage()
        self.entry_widget_list = []
        self.current_frame = self
        self.roles = [
            "Learner",
            "Educator",
            "Parent"
        ]
        self.configure(fg_color="transparent")
        register_title = customtkinter.CTkLabel(master=self,
                                                text="Register",
                                                font=("Fixedsys", 20))
        register_title.grid(row=1, columnspan=2, padx=10, pady=15)

        # Label to ask user for Username
        firstname_label = customtkinter.CTkLabel(master=self, text="First Name: ")
        firstname_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)
        # Variable and input widget for username
        self.firstname = tk.StringVar()
        self.firstname_entry = customtkinter.CTkEntry(master=self,
                                                      textvariable=self.firstname)  # Entry field text (text box)
        self.firstname_entry.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)
        self.entry_widget_list.append(self.firstname_entry)

        # Label to ask user for Username
        lastname_label = customtkinter.CTkLabel(master=self, text="Last Name: ")
        lastname_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)
        # Variable and input widget for username
        self.lastname = tk.StringVar()
        self.lastname_entry = customtkinter.CTkEntry(master=self,
                                                     textvariable=self.lastname)  # Entry field text (text box)
        self.lastname_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)
        self.entry_widget_list.append(self.lastname_entry)

        # Label to ask user for Username
        username_label = customtkinter.CTkLabel(master=self, text="Username: ")
        username_label.grid(row=4, column=0, sticky=tk.E, padx=10, pady=10)
        # Variable and input widget for username
        self.username = tk.StringVar()
        self.username_entry = customtkinter.CTkEntry(master=self,
                                                     textvariable=self.username)  # Entry field text (text box)
        self.username_entry.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)
        self.entry_widget_list.append(self.username_entry)

        password_label = customtkinter.CTkLabel(master=self, text="Password: ")
        password_label.grid(row=5, column=0, sticky=tk.E, padx=10, pady=10)
        # Variable and input widget for password
        self.password = tk.StringVar()
        self.password_entry = customtkinter.CTkEntry(master=self,
                                                     textvariable=self.password, show='●')  # Show = '●'
        self.password_entry.grid(row=5, column=1, sticky=tk.W, padx=10, pady=10)
        self.entry_widget_list.append(self.password_entry)

        # Re-enter password
        password_label2 = customtkinter.CTkLabel(master=self, text="Re-enter Password: ")
        password_label2.grid(row=6, column=0, sticky=tk.E, padx=10, pady=10)
        # Variable and input widget for password
        self.password2 = tk.StringVar()
        self.password_entry2 = customtkinter.CTkEntry(master=self,
                                                      textvariable=self.password2, show='●')  # Show = '●'
        self.password_entry2.grid(row=6, column=1, sticky=tk.W, padx=10, pady=10)
        self.entry_widget_list.append(self.password_entry2)

        # Role
        role_label = customtkinter.CTkLabel(master=self, text="Select Role: ")
        role_label.grid(row=7, column=0, sticky=tk.E, padx=10, pady=10)
        # self.role = tk.StringVar()
        # self.role_dropdown = ttk.Combobox(master=self, values=self.roles)
        self.role_dropdown = customtkinter.CTkComboBox(master=self,
                                                       values=self.roles,
                                                       fg_color="white",
                                                       text_color="black",
                                                       dropdown_fg_color="white",
                                                       dropdown_text_color="black",
                                                       dropdown_hover_color="#8BC9F0")
        self.role_dropdown.grid(row=7, column=1, sticky=tk.W, padx=10, pady=10)

        register_button = customtkinter.CTkButton(master=self, text="Register", width=100, command=self.register_user)
        register_button.grid(row=8, columnspan=2, padx=5, pady=13)

        back_button = customtkinter.CTkButton(master=self, text="Back to Main Page", command=self.back_to_main)
        back_button.grid(row=9, columnspan=2, padx=5, pady=10)

    def show_register_frame(self):
        self.master.switch_frame(self)

    def back_to_main(self):
        self.master.show_main_page()
        self.clear_entries()

    def clear_entries(self):
        for entry in self.entry_widget_list:
            entry.delete(0, tk.END)

        if self.role_dropdown is not None:
            self.role_dropdown.set("")

    def register_user(self):
        first_name = self.firstname.get()
        last_name = self.lastname.get()
        username = self.username.get()
        password = self.password.get()
        password_confirmation = self.password2.get()
        role = self.role_dropdown.get()

        # Check if passwords match
        if password != password_confirmation:
            messagebox.showerror("Password Error", "Passwords do not match. Please try again.")
            return

        # Check if the username is unique
        if username in self.system_storage.existing_usernames:
            messagebox.showerror("Username Error", "Username already exists. Please choose a different username.")
            return

        if role == "Learner":
            user = Learner(username, password, first_name, last_name)
        elif role == "Educator":
            user = Educator(username, password, first_name, last_name)
        elif role == "Parent":
            messagebox.showerror("Cannot wei not done", "Belum lagi bos")
            return
        else:
            messagebox.showerror("Role Error", "Invalid role selection.")
            return

        # Add the user to the storage
        self.system_storage.add_user(user)
        self.system_storage.existing_usernames.append(username)

        with open("C:/Users/User/PycharmProjects/codeVentureApp/user_details", "a", encoding="utf8") as file:
            # add registration into UserAccount.txt
            file.write(f"{username},{password},{first_name},{last_name},{role}\n")

        # Show a success message
        messagebox.showinfo("Registration Successful", "User registration successful!")
        self.back_to_main()


class PasswordRecoveryFrame(customtkinter.CTkFrame):

    def __init__(self, master, parent):
        super().__init__(master=master)
        self.master = master
        self.parent = parent
        self.system_storage = SystemStorage()
        self.current_frame = self

        # To reset entries when change frame
        self.entry_widget_list = []

        # Border set to transparent
        self.configure(fg_color="transparent")

        recovery_title = customtkinter.CTkLabel(master=self, text="Password Recovery", font=("Fixedsys", 20))
        recovery_title.grid(row=1, columnspan=2, padx=10, pady=15)

        # Label to ask for username
        username_label = customtkinter.CTkLabel(master=self, text="Enter Username:")
        username_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)

        self.username = tk.StringVar()
        self.username_entry = customtkinter.CTkEntry(master=self, textvariable=self.username)
        self.username_entry.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)
        self.entry_widget_list.append(self.username_entry)

        new_password_label = customtkinter.CTkLabel(master=self, text="Enter new password: ")
        new_password_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)

        self.new_password = tk.StringVar()
        self.new_password_entry = customtkinter.CTkEntry(master=self, textvariable=self.new_password, show='●')
        self.new_password_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)
        self.entry_widget_list.append(self.new_password_entry)

        new_password_label_two = customtkinter.CTkLabel(master=self, text="Re-enter new password: ")
        new_password_label_two.grid(row=4, column=0, sticky=tk.E, padx=10, pady=10)

        self.new_password_two = tk.StringVar()
        self.new_password_entry_two = customtkinter.CTkEntry(master=self, textvariable=self.new_password_two, show='●')
        self.new_password_entry_two.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)
        self.entry_widget_list.append(self.new_password_entry_two)

        recover_button = customtkinter.CTkButton(master=self, text="Recover Password", command=self.recover_password)
        recover_button.grid(row=5, columnspan=2, padx=5, pady=10)

        back_button = customtkinter.CTkButton(master=self, text="Back to Main Page", command=self.back_to_main)
        back_button.grid(row=6, columnspan=2, padx=5, pady=10)

    def show_password_recovery_frame(self):
        self.master.switch_frame(self.parent.password_recovery_frame)

    # Method to handle password recovery
    def recover_password(self):  # might need to add some questions (What is your childhood nickname? so that not everyone can change password)
        username = self.username.get()
        new_password = self.new_password.get()

        if self.system_storage.check_existing_username(username):
            self.system_storage.update_user_password(username, new_password)
            messagebox.showinfo("Password Reset", "Password has been reset.")
            self.back_to_main()
        else:
            messagebox.showerror("User Not Found", "User not found. Please ensure your username is correct.")

    def back_to_main(self):
        self.master.show_main_page()
        self.clear_entries()
    def clear_entries(self):
        for entry in self.entry_widget_list:
            entry.delete(0, tk.END)