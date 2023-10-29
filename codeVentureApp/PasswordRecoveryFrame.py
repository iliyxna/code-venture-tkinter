# tkinter import
import tkinter as tk
from tkinter import messagebox
import customtkinter

from codeVentureApp.SystemStorage import SystemStorage


class PasswordRecoveryFrame(customtkinter.CTkFrame):
    """
    Class to display for password recovery
    """

    def __init__(self, master, login_frame):
        """
        Constructor
        """
        super().__init__(master=master)
        self.master = master
        self.login_frame = login_frame
        self.user_storage = SystemStorage()
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

    def recover_password(self):
        """
        Method to handle password recovery
        """
        # might need to add some questions (What is your childhood nickname? so that not everyone can change password)
        username = self.username.get()
        new_password = self.new_password.get()
        new_password_2 = self.new_password_entry_two.get()

        if new_password != new_password_2:
            messagebox.showerror( "Password Error", "Passwords do not match. Please try again.")
        else:
            if self.user_storage.get_user_by_username(username) is not None:
                # self.system_storage.update_user_password(username, new_password)
                self.user_storage.update_user_password(username, new_password)
                messagebox.showinfo("Password Reset", "Password has been reset.")
                self.back_to_main()
            else:
                messagebox.showerror("User Not Found", "User not found. Please ensure your username is correct.")

    def back_to_main(self):
        """
        Method to return to the main frame
        """
        self.place_forget()
        self.master.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def clear_entries(self):
        """
        Method to clear the entries
        """
        for entry in self.entry_widget_list:
            entry.delete(0, tk.END)
