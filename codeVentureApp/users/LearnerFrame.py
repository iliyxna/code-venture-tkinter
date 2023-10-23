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

        welcome_title = customtkinter.CTkLabel(master=self,
                                               text=f'Welcome Back, {self.user.get_firstname()}!',
                                               font=("Fixedsys", 20))
        welcome_title.grid(row=1, columnspan=2, padx=10, pady=10)

        learner_frame_title = customtkinter.CTkLabel(master=self,
                                                     text="Learner Dashboard",
                                                     font=("Fixedsys", 20))
        learner_frame_title.grid(row=2, columnspan=2, padx=10, pady=10)

        logout = customtkinter.CTkButton(master=self, text="Logout", command=self.confirm_logout)
        logout.grid(row=5, columnspan=2, padx=5, pady=10)
        print(f"User in LearnerFrame: {self.user}")

    def back_to_login(self):
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def confirm_logout(self):
        result = messagebox.askyesno("Logout Confirmation", "Are you sure you want to sign out?")
        if result:
            self.back_to_login()