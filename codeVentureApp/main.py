import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter

from LoginSystem import LoginFrame, RegisterFrame, PasswordRecoveryFrame
from users.Learner import LearnerFrame


# customtkinter.set_appearance_mode("Dark")
# customtkinter.set_default_color_theme("green")

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
        # self.main_frame = tk.Frame(self)
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
                                                    command=self.login_frame.show_login_frame)
        self.login_button.grid(row=2, columnspan=2, padx=10, pady=10)

        self.register_button = customtkinter.CTkButton(master=self.main_frame,
                                                       text="Register",
                                                       fg_color="white",
                                                       text_color="black",
                                                       width=110,
                                                       command=self.register_frame.show_register_frame)
        self.register_button.grid(row=3, columnspan=2, padx=10, pady=10)

        # self.exit_button = ttk.Button(master=self.main_frame,
        #                               text="Exit",
        #                               command=self.confirm_exit)
        self.exit_button = customtkinter.CTkButton(master=self.main_frame,
                                                   text="Exit",
                                                   width=80,
                                                   command=self.confirm_exit)
        self.exit_button.grid(row=4, columnspan=2, padx=10, pady=10)

        # Set main frame as current
        self.current_frame = self.main_frame

    def switch_frame(self, new_frame):
        self.current_frame.place_forget()
        self.current_frame = new_frame  # Set the new frame as the current frame
        self.current_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_main_page(self):
        # Hide the login frame
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
    # app = MainApplication(root)
    root.mainloop()

