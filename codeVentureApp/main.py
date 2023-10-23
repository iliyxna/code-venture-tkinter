import tkinter as tk
from tkinter import messagebox

import customtkinter

from codeVentureApp.RegisterFrame import RegisterFrame
from codeVentureApp.LoginFrame import LoginFrame


class MainApplication(customtkinter.CTk):

    def __init__(self, title, width=960, height=540):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        customtkinter.set_default_color_theme("dark-blue")

        # Accessible frames from main page
        self.login_frame = LoginFrame(self)
        self.register_frame = RegisterFrame(self)

        # Create a container frame to hold all widgets
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.configure(fg_color="transparent")
        # self.main_frame.grid(row=0, column=0, padx=10, pady=10)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.current_frame = self.main_frame

        self.login_title = customtkinter.CTkLabel(master=self.main_frame,
                                                  text="👾 Welcome to Code Venture 👾",
                                                  font=("Fixedsys", 30),
                                                  text_color="white")
        self.login_title.grid(row=1, columnspan=2, padx=10, pady=15)

        self.login_button = customtkinter.CTkButton(master=self.main_frame,
                                                    text="Login",
                                                    fg_color="white",
                                                    text_color="black",
                                                    width=110,
                                                    command=self.show_login_frame)
        self.login_button.grid(row=2, columnspan=2, padx=10, pady=10)

        self.register_button = customtkinter.CTkButton(master=self.main_frame,
                                                       text="Register",
                                                       fg_color="white",
                                                       text_color="black",
                                                       width=110,
                                                       command=self.show_register_frame)
        self.register_button.grid(row=3, columnspan=2, padx=10, pady=10)

        self.exit_button = customtkinter.CTkButton(master=self.main_frame,
                                                   text="Exit",
                                                   width=80,
                                                   command=self.confirm_exit)
        self.exit_button.grid(row=4, columnspan=2, padx=10, pady=10)

        # Set main frame as current
        self.current_frame = self.main_frame

    def show_login_frame(self):
        self.main_frame.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_register_frame(self):
        self.main_frame.place_forget()
        self.register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_main_frame(self):
        # Hide the current frame
        self.current_frame.place_forget()
        # Show the main window widgets
        self.current_frame = self.main_frame
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def confirm_exit(self):
        result = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
        if result:
            self.destroy()


if __name__ == "__main__":
    root = MainApplication("Code Venture")
    root.mainloop()
