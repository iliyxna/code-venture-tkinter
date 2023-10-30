import sqlite3

import customtkinter
import tkinter as tk
from tkinter import messagebox

from codeVentureApp.ProgressTrackerFrame import ProgressTrackerFrame
from codeVentureApp.SystemStorage import SystemStorage


class ParentFrame(customtkinter.CTkFrame):
    def __init__(self, master, login_frame, user):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        self.master = master
        self.login_frame = login_frame
        self.user = user
        self.child_username = None
        self.system_storage = SystemStorage()

        """""""""""""""""""""""""""
        SIDE NAVIGATION BAR FRAME
        """""""""""""""""""""""""""
        self.nav_bar = customtkinter.CTkFrame(self.master,
                                              fg_color="#6895B2",
                                              corner_radius=0)
        self.nav_bar.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        logo_path = "images/cv.png"
        self.logo = tk.PhotoImage(file=logo_path)

        logo_label = tk.Label(self.nav_bar,
                              image=self.logo,
                              borderwidth=0,
                              anchor="center",
                              bg="#6895B2")
        # logo_label.grid(row=0, column=0, padx=5, pady=40)
        logo_label.place(relx=0, rely=0.10, relwidth=self.nav_bar.winfo_width())

        # DASHBOARD BUTTON
        dashboard_option = customtkinter.CTkButton(self.nav_bar,
                                                   text="Dashboard",
                                                   height=30,
                                                   fg_color="transparent",
                                                   hover_color="#878787",
                                                   font=("Cascadia Mono Bold", 18),
                                                   # command=self.show_dashboard_frame
                                                   )
        dashboard_option.place(relx=0, rely=0.25, relwidth=self.nav_bar.winfo_width())  # Centered vertically

        logout = customtkinter.CTkButton(self.nav_bar,
                                         text="Sign Out",
                                         height=30,
                                         fg_color="transparent",
                                         hover_color="#878787",
                                         font=("Cascadia Mono Bold", 18),
                                         command=self.confirm_logout
                                         )
        logout.place(relx=0, rely=0.35, relwidth=self.nav_bar.winfo_width())  # Centered vertically

        """""""""""""""""
        MAIN PARENT FRAME
        """""""""""""""""
        # Main parent frame to be replaced when nav menu option is clicked
        self.parent_frame = customtkinter.CTkScrollableFrame(self.master)
        self.parent_frame.place(relx=0.2, rely=0, relwidth=0.6, relheight=1)
        self.parent_frame.configure(fg_color="#C2D3DF", corner_radius=0)

        """""""""""""""""""""""""""
        Welcome user frame section
        """""""""""""""""""""""""""
        self.welcome_frame = customtkinter.CTkFrame(self.parent_frame,
                                                    corner_radius=20,
                                                    fg_color="#6895B2",
                                                    height=200)
        self.welcome_frame.grid(row=0, column=0, padx=30, pady=50, sticky="ew")

        welcome_title = customtkinter.CTkLabel(master=self.welcome_frame,
                                               text=f'Welcome Back, {self.user.get_firstname()}!',
                                               font=("Fixedsys", 24),
                                               anchor="w",
                                               justify="left"
                                               )
        welcome_title.grid(row=0, column=0, padx=30, pady=50, sticky="ew")

        # if self.user.get_child_username() is None:
        if not self.system_storage.check_parent_child(self.user.get_username()):
            welcome_message = customtkinter.CTkLabel(master=self.welcome_frame,
                                                     text=f"To get started, add your child's account and join the "
                                                          f"exciting journey of monitoring their progress! 🚀\n\n"
                                                          f"By connecting with your child's account, you'll be able "
                                                          f"to track their learning adventures, see their achievements,"
                                                          f" and celebrate \ntheir success together."
                                                          f"Watch as they conquer new modules, complete thrilling "
                                                          f"challenges, and earn cool badges. \n\nIt's a fantastic way "
                                                          f"to support their growth and share the joy of learning."
                                                          f"So, don't wait any longer! \nJoin hands with your little "
                                                          f"explorer and embark on this educational voyage together. "
                                                          f"It's time to create amazing \nmemories and witness their "
                                                          f"development every step of the way. Let's get started!\n",

                                                     anchor="w",
                                                     justify="left"
                                                     )
            welcome_message.grid(row=1, column=0, padx=30, pady=0, sticky="nw")

            add_child_button = customtkinter.CTkButton(master=self.welcome_frame,
                                                       text="Link Child\'s Account",
                                                       hover_color="#878787",
                                                       command=self.add_child
                                                       )
            add_child_button.grid(row=2, column=0, padx=20, pady=20, sticky="w")

        else:  # if already linked to child account
            parent_username, child_username = self.system_storage.get_parent_data(self.user.get_username())
            self.child_username = child_username

            (learner_username, learner_points, learner_rank,
             percentage_completion) = self.system_storage.get_learner_progress(child_username)

            welcome_message = customtkinter.CTkLabel(master=self.welcome_frame,
                                                     text=f"Great news! Your child, @{child_username}, has been on "
                                                          f"an incredible learning journey and has successfully "
                                                          f"completed {percentage_completion}% of their modules!\n"
                                                          f"Isn't that amazing? It's a testament to their dedication "
                                                          f"and curiosity for knowledge.\n\n"
                                                          f"As their dedicated learning partner, you can "
                                                          f"continue to support "
                                                          f"and nurture their growth. Encourage them to explore new "
                                                          f"modules,\n tackle exciting challenges, and earn impressive "
                                                          f"badges. By working together, you can create a rich and "
                                                          f"rewarding learning \nexperience, full of fun and discovery."
                                                          f" So, let's keep the momentum going and embark on more "
                                                          f"educational adventures together!\n\n"
                                                          f"Stay excited, stay curious, and keep the love for learning "
                                                          f"alive! The sky's the limit for your child's potential.\n",
                                                     anchor="w",
                                                     justify="left"
                                                     )
            welcome_message.grid(row=1, column=0, padx=30, pady=10, sticky="nw")

        """""""""""""""""""""""
        Profile frame section
        """""""""""""""""""""""
        self.profile_frame = customtkinter.CTkFrame(master=self.master,
                                                    fg_color="#6895B2",
                                                    corner_radius=0
                                                    )
        self.profile_frame.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

        profile_label = customtkinter.CTkLabel(master=self.profile_frame,
                                               text="USER PROFILE",
                                               font=("Cascadia Mono Bold", 16))
        profile_label.place(relx=0, y=100, relwidth=self.profile_frame.winfo_width())

        avatar_path = "images/parent2.png"
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
                                      text=f"{self.user.get_firstname()} {self.user.get_lastname()}\n",
                                      font=("Arial", 14),
                                      anchor="center")
        name.place(relx=0, y=405, relwidth=self.profile_frame.winfo_width())

        # Username
        username_label = customtkinter.CTkLabel(self.profile_frame,
                                                text="U S E R N A M E",
                                                font=("Cascadia Code Bold", 14),
                                                fg_color="#4E6F86",
                                                anchor="center"
                                                )
        username_label.place(relx=0, y=455, relwidth=self.profile_frame.winfo_width())

        username = customtkinter.CTkLabel(self.profile_frame,
                                          text=f"@{self.user.get_username()}",
                                          font=("Arial", 14),
                                          anchor="center")
        username.place(relx=0, y=490, relwidth=self.profile_frame.winfo_width())

        # Child username
        child_label = customtkinter.CTkLabel(self.profile_frame,
                                             text="C H I L D",
                                             fg_color="#4E6F86",
                                             font=("Cascadia Code Bold", 14),
                                             anchor="center"
                                             )
        child_label.place(relx=0, y=540, relwidth=self.profile_frame.winfo_width())

        if self.system_storage.check_parent_child(self.user.get_username()):
            child = customtkinter.CTkLabel(self.profile_frame,
                                           text=f"@{self.child_username}",
                                           font=("Arial", 14),
                                           anchor="center")
            child.place(relx=0, y=575, relwidth=self.profile_frame.winfo_width())

        else:
            child = customtkinter.CTkLabel(self.profile_frame,
                                           text=f"None",
                                           font=("Arial", 14),
                                           anchor="center")
            child.place(relx=0, y=575, relwidth=self.profile_frame.winfo_width())

        # User role
        role_label = customtkinter.CTkLabel(self.profile_frame,
                                            text='R O L E',
                                            font=("Cascadia Code Bold", 14),
                                            fg_color="#4E6F86",
                                            anchor="center"
                                            )
        role_label.place(relx=0, y=625, relwidth=self.profile_frame.winfo_width())

        role = customtkinter.CTkLabel(self.profile_frame,
                                      text="Parent",
                                      font=("Arial", 14),
                                      anchor="center")
        role.place(relx=0, y=660, relwidth=self.profile_frame.winfo_width())

        """""""""""""""
        Child Progress Frame
        """""""""""""""
        if self.system_storage.check_parent_child(self.user.get_username()):
            # self.progress_frame = customtkinter.CTkFrame(self.parent_frame, corner_radius=20)
            child_user = self.system_storage.get_user_by_username(self.child_username)
            self.progress_frame = ProgressTrackerFrame(self.parent_frame, child_user)
            self.progress_frame.grid(row=1, column=0, padx=30, pady=20, sticky="ew")

        self.current_frame = self.parent_frame

    def show_dashboard_frame(self):
        """
        Method to show the dashboard page (homepage for learner)
        """
        self.current_frame.place_forget()
        self.parent_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.progress_frame.grid(row=1, column=0, padx=30, pady=20, sticky="ew")

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
        self.parent_frame.place_forget()
        self.profile_frame.place_forget()
        self.nav_bar.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def add_child(self):
        """
        Method to add child username to parent account
        """
        # Create new window to add child username by checking system storage
        dialog = customtkinter.CTkInputDialog(text="Enter Child's Username: ", title="Link Child Account")
        username = dialog.get_input()

        try:
            if self.system_storage.get_user_by_username(username) is not None:
                child_user = self.system_storage.get_user_by_username(username)
                if child_user.get_role() == "Learner":
                    self.child_username = child_user.get_username()
                    self.system_storage.insert_child_username(self.user, child_user)
                    messagebox.showinfo(title="Successfully Linked", message="You have successfully linked your "
                                                                             "account to your child's account.")

                    # If successfully linked, update the message and remove the add child button
                    if self.system_storage.check_parent_child(self.user.get_username()):
                        self.welcome_frame.grid_forget()

                        # Recreate with child's progress once linked
                        self.welcome_frame = customtkinter.CTkFrame(self.parent_frame,
                                                                    corner_radius=20,
                                                                    fg_color="#6895B2",
                                                                    height=200)
                        self.welcome_frame.grid(row=0, column=0, padx=30, pady=50, sticky="ew")

                        welcome_title = customtkinter.CTkLabel(master=self.welcome_frame,
                                                               text=f'Welcome Back, {self.user.get_firstname()}!',
                                                               font=("Fixedsys", 24),
                                                               anchor="w",
                                                               justify="left"
                                                               )
                        welcome_title.grid(row=0, column=0, padx=30, pady=50, sticky="ew")

                        parent_username, child_username = self.system_storage.get_parent_data(self.user.get_username())
                        (learner_username, learner_points, learner_rank,
                         percentage_completion) = self.system_storage.get_learner_progress(child_username)

                        welcome_message = customtkinter.CTkLabel(master=self.welcome_frame,
                                                                 text=f"Great news! Your child, @{child_username}, has been on "
                                                                      f"an incredible learning journey and has successfully "
                                                                      f"completed {percentage_completion}% of their modules!\n"
                                                                      f"Isn't that amazing? It's a testament to their dedication "
                                                                      f"and curiosity for knowledge.\n\n"
                                                                      f"As their dedicated learning partner, you can "
                                                                      f"continue to support "
                                                                      f"and nurture their growth. Encourage them to explore new "
                                                                      f"modules,\n tackle exciting challenges, and earn impressive "
                                                                      f"badges. By working together, you can create a rich and "
                                                                      f"rewarding learning \nexperience, full of fun and discovery."
                                                                      f" So, let's keep the momentum going and embark on more "
                                                                      f"educational adventures together!\n\n"
                                                                      f"Stay excited, stay curious, and keep the love for learning "
                                                                      f"alive! The sky's the limit for your child's potential.\n",
                                                                 anchor="w",
                                                                 justify="left"
                                                                 )
                        welcome_message.grid(row=1, column=0, padx=30, pady=10, sticky="nw")

                        # Add Child Username to Profile frame
                        child = customtkinter.CTkLabel(self.profile_frame,
                                                       text=f"@{child_username}",
                                                       font=("Arial", 14),
                                                       anchor="center")
                        child.place(relx=0, y=560, relwidth=self.profile_frame.winfo_width())

                        # Update progress frame
                        self.progress_frame = ProgressTrackerFrame(self.parent_frame, child_user)
                        self.progress_frame.grid(row=1, column=0, padx=30, pady=20, sticky="ew")
                else:
                    messagebox.showerror("Linking Failed", "The specified user is not a child learner.")
            else:
                messagebox.showerror("Linking Failed", "Child username does not exist. Please try again.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Linking Failed", "The child username is already linked to another parent account.")
