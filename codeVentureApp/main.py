import tkinter as tk
from tkinter import messagebox

import customtkinter

from codeVentureApp.RegisterFrame import RegisterFrame
from codeVentureApp.LoginFrame import LoginFrame


class MainApplication(customtkinter.CTk):
    """
    Main class to run the Code Venture
    """

    def __init__(self, title, width=1400, height=700):
        """
        Constructor
        """
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self._set_appearance_mode("light")
        self.configure(fg_color="#C2D3DF")
        # Accessible frames from main page
        self.login_frame = LoginFrame(self)
        self.register_frame = RegisterFrame(self)

        # Create a container frame to hold all widgets
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.configure(fg_color="transparent",
                                  bg_color="transparent",
                                  corner_radius=20)
        # self.main_frame.grid(row=0, column=0, padx=10, pady=10)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.current_frame = self.main_frame

        self.login_title = customtkinter.CTkLabel(master=self.main_frame,
                                                  text="👾 Welcome to Code Venture 👾",
                                                  font=("Fixedsys", 30),
                                                  text_color="#6895B2")
        self.login_title.grid(row=1, columnspan=2, padx=20, pady=20)

        self.login_button = customtkinter.CTkButton(master=self.main_frame,
                                                    text="Login",
                                                    fg_color="#6895B2",
                                                    # text_color="black",
                                                    width=110,
                                                    hover_color="#878787",
                                                    command=self.show_login_frame)
        self.login_button.grid(row=2, columnspan=2, padx=10, pady=20, sticky="s")

        self.register_button = customtkinter.CTkButton(master=self.main_frame,
                                                       text="Register",
                                                       fg_color="#6895B2",
                                                       width=110,
                                                       hover_color="#878787",
                                                       command=self.show_register_frame)
        self.register_button.grid(row=3, columnspan=2, padx=10, pady=20)

        self.exit_button = customtkinter.CTkButton(master=self.main_frame,
                                                   text="Exit",
                                                   fg_color="#7C9AAF",
                                                   width=80,
                                                   command=self.confirm_exit)
        self.exit_button.grid(row=4, columnspan=2, padx=10, pady=20, sticky="s")

        # Set main frame as current
        self.current_frame = self.main_frame

    def show_login_frame(self):
        """
        Method to show login frame
        """
        self.main_frame.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_register_frame(self):
        """
        Method to show register frame
        """
        self.main_frame.place_forget()
        self.register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_main_frame(self):
        """
        Method to show main frame
        """
        # Hide the current frame
        self.current_frame.place_forget()
        # Show the main window widgets
        self.current_frame = self.main_frame
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def confirm_exit(self):
        """
        Method to confirm to exit
        """
        result = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
        if result:
            self.destroy()


if __name__ == "__main__":
    root = MainApplication("Code Venture")
    root.mainloop()
