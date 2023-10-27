from tkinter import messagebox

import customtkinter
import tkinter as tk

from codeVentureApp.SystemStorage import SystemStorage
from codeVentureApp.users.Administrator import Administrator
from codeVentureApp.users.Educator import Educator
from codeVentureApp.users.Learner import Learner
from codeVentureApp.users.Parent import Parent


class AdminFrame(customtkinter.CTkFrame):
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
        self.nav_bar = customtkinter.CTkFrame(self.master,
                                              fg_color="#6895B2",
                                              bg_color="#6895B2",
                                              corner_radius=0
                                              )
        self.nav_bar.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        logo_path = "images/cv.png"
        self.logo = tk.PhotoImage(file=logo_path)

        logo_label = tk.Label(self.nav_bar,
                              image=self.logo,
                              borderwidth=0,
                              anchor="center",
                              bg="#6895B2")

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

        # DASHBOARD BUTTON
        create_acc = customtkinter.CTkButton(self.nav_bar,
                                             text="Create Account",
                                             height=30,
                                             fg_color="transparent",
                                             hover_color="#878787",
                                             font=("Cascadia Mono Bold", 18),
                                             command=self.create_account
                                             )
        create_acc.place(relx=0, rely=0.35, relwidth=self.nav_bar.winfo_width())  # Centered vertically

        logout = customtkinter.CTkButton(self.nav_bar,
                                         text="Sign Out",
                                         height=30,
                                         fg_color="transparent",
                                         hover_color="#878787",
                                         font=("Cascadia Mono Bold", 18),
                                         command=self.confirm_logout
                                         )
        logout.place(relx=0, rely=0.45, relwidth=self.nav_bar.winfo_width())  # Centered vertically

        """""""""""""""""
        MAIN ADMIN FRAME
        """""""""""""""""
        # Main parent frame to be replaced when nav menu option is clicked
        self.admin_frame = customtkinter.CTkFrame(self.master)
        self.admin_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.admin_frame.configure(fg_color="#C2D3DF")

        """""""""""""""""""""""""""
        Welcome user frame section
        """""""""""""""""""""""""""
        self.welcome_frame = customtkinter.CTkFrame(self.admin_frame,
                                                    corner_radius=20,
                                                    height=200,
                                                    fg_color="#6895B2")

        self.welcome_frame.place(relx=0.05, y=100, relwidth=0.65)

        welcome_title = customtkinter.CTkLabel(master=self.welcome_frame,
                                               text=f'Welcome Back, {self.user.get_firstname()}!',
                                               font=("Fixedsys", 24),
                                               anchor="w",
                                               justify="left"
                                               )
        welcome_title.grid(row=0, column=0, padx=20, pady=20, sticky="sw")

        welcome_message = customtkinter.CTkLabel(master=self.welcome_frame,
                                                 text=f'You have the power to oversee the entire CodeVenture platform.\n'
                                                      f'Explore your admin dashboard '
                                                      'to access the tools and features to maintain the platform.',
                                                 anchor="w",
                                                 justify="left"
                                                 )
        welcome_message.grid(row=1, column=0, padx=20, pady=20, sticky="nw")

        self.current_frame = self.admin_frame

        """""""""""""""""""""""
        Profile frame section
        """""""""""""""""""""""
        self.profile_frame = customtkinter.CTkFrame(master=self.admin_frame,
                                                    fg_color="#6895B2",
                                                    corner_radius=0
                                                    )
        self.profile_frame.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)

        profile_label = customtkinter.CTkLabel(master=self.profile_frame,
                                               text="USER PROFILE",
                                               fg_color="#6895B2",
                                               font=("Cascadia Mono Bold", 16))
        profile_label.place(relx=0, y=100, relwidth=self.profile_frame.winfo_width())

        # Set current frame
        self.current_frame = self.welcome_frame

        avatar_path = "images/admin.png"
        self.avatar = tk.PhotoImage(file=avatar_path)

        avatar_label = tk.Label(self.profile_frame,
                                image=self.avatar,
                                borderwidth=0,
                                anchor="center",
                                bg="#6895B2")

        avatar_label.place(relx=0, rely=0.22, relwidth=self.profile_frame.winfo_width())

        # User's full name
        name_label = customtkinter.CTkLabel(self.profile_frame,
                                            text="N A M E",
                                            font=("Cascadia Code Bold", 14),
                                            fg_color="#4E6F86",
                                            anchor="center"
                                            )
        name_label.place(relx=0, y=370, relwidth=self.profile_frame.winfo_width())

        name = customtkinter.CTkLabel(self.profile_frame,
                                      text=f"{self.user.get_firstname()} {self.user.get_lastname()}",
                                      font=("Arial", 14),
                                      anchor="center")
        name.place(relx=0, y=405, relwidth=self.nav_bar.winfo_width())

        # Username
        username_label = customtkinter.CTkLabel(self.profile_frame,
                                                text="U S E R N A M E",
                                                font=("Cascadia Code Bold", 14),
                                                fg_color="#4E6F86",
                                                anchor="center"
                                                )
        username_label.place(relx=0, y=455, relwidth=self.nav_bar.winfo_width())

        username = customtkinter.CTkLabel(self.profile_frame,
                                          text=f"@{self.user.get_username()}",
                                          font=("Arial", 14),
                                          anchor="center")
        username.place(relx=0, y=490, relwidth=self.nav_bar.winfo_width())

        # User role
        role_label = customtkinter.CTkLabel(self.profile_frame,
                                            text='R O L E',
                                            font=("Cascadia Code Bold", 14),
                                            fg_color="#4E6F86",
                                            anchor="center"
                                            )
        role_label.place(relx=0, y=540, relwidth=self.nav_bar.winfo_width())

        role = customtkinter.CTkLabel(self.profile_frame,
                                      text="Learner",
                                      font=("Arial", 14),
                                      anchor="center")
        role.place(relx=0, y=575, relwidth=self.nav_bar.winfo_width())

    def show_dashboard_frame(self):
        """
        Method to show the dashboard page (homepage for learner)
        """
        self.current_frame.place_forget()
        self.current_frame = self.admin_frame
        self.welcome_frame.place(relx=0.05, y=100, relwidth=0.65)
        self.admin_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

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
        self.current_frame.place_forget()
        self.nav_bar.place_forget()
        self.profile_frame.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_account(self):
        self.current_frame.place_forget()
        entry_widget_list = []

        # Roles used for dropdown list
        roles = [
            "Learner",
            "Parent",
            "Educator",
            "Admin"
        ]

        # Create account frame
        create_account_frame = customtkinter.CTkFrame(self.master)
        create_account_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        create_account_frame.configure(fg_color="#C2D3DF")

        entries_frame = customtkinter.CTkFrame(create_account_frame)
        entries_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        entries_frame.configure(fg_color="transparent")

        # set current frame to create acc frame
        self.current_frame = create_account_frame

        register_title = customtkinter.CTkLabel(master=entries_frame,
                                                text="Create Account",
                                                font=("Fixedsys", 24),
                                                text_color="#6895B2")
        register_title.grid(row=0, columnspan=2, padx=10, pady=15)

        # Label to ask user for first name
        firstname_label = customtkinter.CTkLabel(master=entries_frame, text="First Name: ",
                                                 text_color="#6895B2",
                                                 font=("Cascadia Mono Bold", 14)
                                                 )
        firstname_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        # Variable and input widget for username
        firstname = tk.StringVar()
        firstname_entry = customtkinter.CTkEntry(master=entries_frame,
                                                 textvariable=firstname,
                                                 fg_color="#EFF9FF",
                                                 text_color="#6895B2",
                                                 border_color="#6895B2",
                                                 )  # Entry field text (text box)
        firstname_entry.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)
        entry_widget_list.append(firstname_entry)

        # Label to ask user for last_name
        lastname_label = customtkinter.CTkLabel(master=entries_frame, text="Last Name: ",
                                                text_color="#6895B2",
                                                font=("Cascadia Mono Bold", 14)
                                                )
        lastname_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
        # Variable and input widget for username
        lastname = tk.StringVar()
        lastname_entry = customtkinter.CTkEntry(master=entries_frame,
                                                textvariable=lastname,
                                                fg_color="#EFF9FF",
                                                text_color="#6895B2",
                                                border_color="#6895B2",
                                                )  # Entry field text (text box)
        lastname_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)
        entry_widget_list.append(lastname_entry)

        # Label to ask user for Username
        username_label = customtkinter.CTkLabel(master=entries_frame, text="Username: ",
                                                text_color="#6895B2",
                                                font=("Cascadia Mono Bold", 14)
                                                )
        username_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)
        # Variable and input widget for username
        username = tk.StringVar()
        username_entry = customtkinter.CTkEntry(master=entries_frame,
                                                textvariable=username,
                                                fg_color="#EFF9FF",
                                                text_color="#6895B2",
                                                border_color="#6895B2",
                                                )  # Entry field text (text box)
        username_entry.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)
        entry_widget_list.append(username_entry)

        password_label = customtkinter.CTkLabel(master=entries_frame, text="Password: ",
                                                text_color="#6895B2",
                                                font=("Cascadia Mono Bold", 14)
                                                )
        password_label.grid(row=5, column=0, sticky=tk.W, padx=10, pady=10)
        # Variable and input widget for password
        password = tk.StringVar()
        password_entry = customtkinter.CTkEntry(master=entries_frame,
                                                textvariable=password, show='●',
                                                fg_color="#EFF9FF",
                                                text_color="#6895B2",
                                                border_color="#6895B2",
                                                )  # Show = '●'
        password_entry.grid(row=5, column=1, sticky=tk.W, padx=10, pady=10)
        entry_widget_list.append(password_entry)

        # Re-enter password
        password_label2 = customtkinter.CTkLabel(master=entries_frame, text="Re-enter Password: ",
                                                 text_color="#6895B2",
                                                 font=("Cascadia Mono Bold", 14)
                                                 )
        password_label2.grid(row=6, column=0, sticky=tk.W, padx=10, pady=10)
        # Variable and input widget for password
        password2 = tk.StringVar()
        password_entry2 = customtkinter.CTkEntry(master=entries_frame,
                                                 textvariable=password2, show='●',
                                                 fg_color="#EFF9FF",
                                                 text_color="#6895B2",
                                                 border_color="#6895B2",
                                                 )  # Show = '●'
        password_entry2.grid(row=6, column=1, sticky=tk.W, padx=10, pady=10)
        entry_widget_list.append(password_entry2)

        # Role
        role_label = customtkinter.CTkLabel(master=entries_frame, text="Select Role: ",
                                            text_color="#6895B2",
                                            font=("Cascadia Mono Bold", 14)
                                            )
        role_label.grid(row=7, column=0, sticky=tk.W, padx=10, pady=10)

        role_dropdown = customtkinter.CTkComboBox(master=entries_frame,
                                                  values=roles,
                                                  fg_color="#EFF9FF",
                                                  text_color="#6895B2",
                                                  border_color="#6895B2",
                                                  button_color="#6895B2",
                                                  dropdown_fg_color="white",
                                                  dropdown_text_color="#577184",
                                                  dropdown_hover_color="#8BC9F0")
        role_dropdown.grid(row=7, column=1, sticky=tk.W, padx=10, pady=10)

        def register_user():
            """
            Method to register as a user.
            Note that only learners and parents can register. Educators and admins cannot register as they
            are added manually into the database.
            """
            first_name = firstname.get()
            last_name = lastname.get()
            user_name = username.get()
            pwd = password.get()
            pwd_confirmation = password2.get()
            role = role_dropdown.get()

            # Ensure all entries filled.
            if (len(first_name) == 0 or len(last_name) == 0 or len(user_name) == 0 or len(pwd) == 0 or
                    len(pwd_confirmation) == 0):
                messagebox.showerror("Empty Field Error", "Please fill in all the entries. All entries must be filled.")
                return

            # Check if passwords match
            elif pwd != pwd_confirmation:
                messagebox.showerror("Password Error", "Passwords do not match. Please try again.")
                return

            # Check if the username is unique
            elif self.system_storage.get_user_by_username(user_name) is not None:
                messagebox.showerror("Username Error", "Username already exists. Please choose a different username.")
                return

            else:
                if role == "Learner":
                    user = Learner(user_name, pwd, first_name, last_name)
                    self.system_storage.insert_user_data(user)
                elif role == "Parent":
                    user = Parent(user_name, pwd, first_name, last_name)
                    self.system_storage.insert_user_data(user)
                elif role == "Educator":
                    user = Educator(user_name, pwd, first_name, last_name)
                    self.system_storage.insert_user_data(user)
                elif role == "Admin":
                    user = Administrator(user_name, pwd, first_name, last_name)
                    self.system_storage.insert_user_data(user)
                else:
                    messagebox.showerror("Role Error", "Invalid role selection.")
                    return

            # Show a success message
            messagebox.showinfo("Account Creation Successful", "You have successfully created an account.")

            for entry in entry_widget_list:
                entry.delete(0, tk.END)

            if role_dropdown is not None:
                role_dropdown.set("Select Role")

        # Register button
        register_button = customtkinter.CTkButton(master=entries_frame,
                                                  text="Create Account", width=100,
                                                  fg_color="#6895B2",
                                                  command=register_user)
        register_button.grid(row=8, columnspan=2, padx=5, pady=13, sticky="s")

