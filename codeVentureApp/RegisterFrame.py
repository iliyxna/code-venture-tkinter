# tkinter import
import tkinter as tk
from tkinter import messagebox
import customtkinter

from codeVentureApp.users.Administrator import Administrator
# from codeVentureApp.SystemStorageDraft import SystemStorage
from codeVentureApp.users.Educator import Educator
from codeVentureApp.users.Learner import Learner
from codeVentureApp.users.Parent import Parent
from codeVentureApp.SystemStorage import SystemStorage


class RegisterFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        """
        Constructor
        """
        super().__init__(master=master)
        self.master = master
        self.user_storage = SystemStorage()
        self.entry_widget_list = []  # to clear the entries in one go
        self.current_frame = self

        # Roles used for dropdown list (Learner and Parent only)
        self.roles = [
            "Learner",
            "Parent",
        ]

        self.configure(fg_color="transparent")  # set the frame as transparent to match default bg colour
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

        back_button = customtkinter.CTkButton(master=self, text="Back to Main Page", command=self.show_main_page)
        back_button.grid(row=9, columnspan=2, padx=5, pady=10)

    def show_main_page(self):
        """
        Method to navigate back to the main page
        """
        self.place_forget()
        self.master.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.clear_entries()

    def clear_entries(self):
        """
        Method to clear all the register entries
        """
        for entry in self.entry_widget_list:
            entry.delete(0, tk.END)

        if self.role_dropdown is not None:
            self.role_dropdown.set("Select Role")

    def register_user(self):
        """
        Method to register as a user.
        Note that only learners and parents can register. Educators and admins cannot register as they
        are added manually into the database.
        """
        first_name = self.firstname.get()
        last_name = self.lastname.get()
        username = self.username.get()
        password = self.password.get()
        password_confirmation = self.password2.get()
        role = self.role_dropdown.get()

        if (len(first_name) == 0 or len(last_name) == 0 or len(username) == 0 or len(password) == 0 or
                len(password_confirmation) == 0):
            messagebox.showerror("Empty Field Error", "Please fill in all the entries.")
            return

        # Check if passwords match
        elif password != password_confirmation:
            messagebox.showerror("Password Error", "Passwords do not match. Please try again.")
            return

        # Check if the username is unique
        elif self.user_storage.get_user_by_username(username) is not None:
            messagebox.showerror("Username Error", "Username already exists. Please choose a different username.")
            return

        else:
            print(f'Selected role: {role}')
            if role == "Learner":
                user = Learner(username, password, first_name, last_name)
                self.user_storage.insert_user_data(user)
            elif role == "Parent":
                user = Parent(username, password, first_name, last_name)
                self.user_storage.insert_user_data(user)
            else:
                messagebox.showerror("Role Error", "Invalid role selection.")
                return

        # debugging purposes
        # Add the user to the storage
        if self.user_storage.get_user_by_username(user.get_username()) is not None:
            print(user)
        else:
            print("NOT ADDED TO LIST")

        # Show a success message
        messagebox.showinfo("Registration Successful", "User registration successful!")
        self.show_main_page()
