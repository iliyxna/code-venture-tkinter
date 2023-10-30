from datetime import datetime
from tkinter import messagebox

import customtkinter
import tkinter as tk

from codeVentureApp.SystemStorage import SystemStorage


class EducatorFrame(customtkinter.CTkFrame):
    def __init__(self, master, login_frame, user):
        """
        Constructor
        """
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        self.master = master
        self.login_frame = login_frame
        self.user = user
        self.system_storage = SystemStorage()

        self.module_in_charge = self.system_storage.get_teaching_module(self.user.get_username())
        self.module_id = self.module_in_charge[0]
        self.module_name = self.module_in_charge[2]

        self.forum_open = False
        self.forum_window = None

        self.current_row = 10 # random big num
        self.all_students = self.system_storage.get_all_students()

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
        # logo_label.grid(row=0, column=0, padx=5, pady=40)
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

        # FORUM BUTTON
        forum_button = customtkinter.CTkButton(self.nav_bar,
                                               text="Discussion Forum",
                                               height=30,
                                               fg_color="transparent",
                                               hover_color="#878787",
                                               font=("Cascadia Mono Bold", 18),
                                               command=self.show_forum_window
                                               )
        forum_button.place(relx=0, rely=0.35, relwidth=self.nav_bar.winfo_width())  # Centered vertically

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
        MAIN EDUCATOR FRAME
        """""""""""""""""
        # Main parent frame to be replaced when nav menu option is clicked
        self.educator_frame = customtkinter.CTkScrollableFrame(self.master)
        self.educator_frame.place(relx=0.2, rely=0, relwidth=0.6, relheight=1)
        self.educator_frame.configure(fg_color="#C2D3DF", corner_radius=0)

        """""""""""""""""""""""""""
        Welcome user frame section
        """""""""""""""""""""""""""
        self.welcome_frame = customtkinter.CTkFrame(self.educator_frame,
                                                    corner_radius=20,
                                                    height=200,
                                                    fg_color="#6895B2")
        self.welcome_frame.grid(row=0, column=0, padx=30, pady=50, sticky="sew")

        welcome_title = customtkinter.CTkLabel(master=self.welcome_frame,
                                               text=f'Welcome Back, {self.user.get_firstname()}!',
                                               font=("Fixedsys", 24),
                                               anchor="sw",
                                               justify="left"
                                               )
        welcome_title.grid(row=0, column=0, padx=20, pady=30, sticky="sw")

        welcome_message = customtkinter.CTkLabel(master=self.welcome_frame,
                                                 text=f'As an educator, you oversee one module topic. '
                                                      f'You can view class summaries, '
                                                      'learner results, and \nparticipate in module discussions. '
                                                      'Start by exploring your educator dashboard and '
                                                      'empowering young minds!\n',
                                                 anchor="nw",
                                                 justify="left"
                                                 )
        welcome_message.grid(row=1, column=0, padx=20, pady=10, sticky="nw")

        self.current_frame = self.educator_frame

        """""""""""""""
        Class overview
        """""""""""""""
        self.summary_frame = customtkinter.CTkFrame(self.educator_frame,
                                                    corner_radius=20,
                                                    fg_color="white")

        self.summary_frame.grid(row=1, column=0, padx=30, pady=20, sticky="ew")

        # class_summary_label = customtkinter.CTkLabel(master=self.summary_frame,
        #                                              text='Class Overview',
        #                                              font=("Fixedsys", 23),
        #                                              anchor="w",
        #                                              justify="left",
        #                                              text_color="#6895B2"
        #                                              )
        # class_summary_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        # all_students_frame = customtkinter.CTkFrame(master=self.summary_frame,
        #                                             corner_radius=20,
        #                                             fg_color="#FAFAFA")
        # all_students_frame.grid(row=0, column=0, padx=30, pady=50, sticky="ew")

        welcome_title = customtkinter.CTkLabel(master=self.summary_frame,
                                               text=f'Students Overview',
                                               font=("Fixedsys", 24),
                                               anchor="sw",
                                               justify="left",
                                               text_color="#6895B2"
                                               )
        welcome_title.grid(row=0, column=0, padx=30, pady=30, sticky="sw")

        module_label = customtkinter.CTkLabel(master=self.summary_frame,
                                              text=f'Module: {self.module_name}',
                                              font=("Cascadia Code", 18),
                                              anchor="sw",
                                              justify="left",
                                              text_color="#6895B2"
                                              )
        module_label.grid(row=1, column=0, padx=40, pady=10, sticky="sw")

        students_grid = customtkinter.CTkFrame(self.summary_frame,
                                               fg_color="#6895B2",
                                               corner_radius=10)
        students_grid.grid(row=2, column=0, padx=40, pady=10, sticky="new")

        # Column 0 - number
        num = customtkinter.CTkLabel(students_grid,
                                     text="No.   ",
                                     text_color="White",
                                     font=("Cascadia Code Bold", 16))
        num.grid(row=0, column=0, padx=20, pady=10, sticky="sw")

        # Column 1- student name
        name_label = customtkinter.CTkLabel(students_grid,
                                            text="Username              ",
                                            text_color="White",
                                            font=("Cascadia Code Bold", 16))
        name_label.grid(row=0, column=1, padx=20, pady=10, sticky="sw")

        # Display all the students
        for i in range(len(self.all_students)):
            student_data = self.all_students[i]

            student_username = student_data[0]

            number = customtkinter.CTkLabel(students_grid,
                                            text=f'{i + 1}.',
                                            font=("Calibri Bold", 14))
            number.grid(row=i + 1, column=0, padx=25, pady=5, sticky="sw")

            student = customtkinter.CTkLabel(students_grid,
                                             text=f'{student_username}',
                                             font=("Calibri Bold", 14))
            student.grid(row=i + 1, column=1, padx=25, pady=5, sticky="sw")

        # Column 2 - student score
        score_label = customtkinter.CTkLabel(students_grid,
                                             text="Score",
                                             text_color="White",
                                             font=("Cascadia Code Bold", 16))
        score_label.grid(row=0, column=2, padx=20, pady=5, sticky="ew")

        attempted_students = self.system_storage.get_students_completed(self.module_id)

        # loop through to check if the student has completed the module
        for i in range(len(self.all_students)):
            student_data = self.all_students[i]
            student_username = student_data[0]
            found = False

            # check against attempted_students list
            for student in attempted_students:
                if student_username == student[1]:
                    score = customtkinter.CTkLabel(students_grid,
                                                   text=f'{student[3]} / 3',
                                                   font=("Calibri Bold", 14)
                                                   )
                    score.grid(row=i + 1, column=2, padx=20, pady=5, sticky="sew")
                    found = True
                    break

            if not found:
                score = customtkinter.CTkLabel(students_grid,
                                               text=f'   No attempt   ',
                                               font=("Calibri Bold", 14))
                score.grid(row=i + 1, column=2, padx=20, pady=5, sticky="sew")

        """""""""""""""""""""""
        Profile frame section
        """""""""""""""""""""""
        self.profile_frame = customtkinter.CTkFrame(master=self.master,
                                                    fg_color="#6895B2",
                                                    corner_radius=0)
        self.profile_frame.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

        profile_label = customtkinter.CTkLabel(master=self.profile_frame,
                                               text="USER PROFILE",
                                               font=("Cascadia Mono Bold", 16))
        profile_label.place(relx=0, y=100, relwidth=self.profile_frame.winfo_width())

        # Set current frame
        self.current_frame = self.welcome_frame

        avatar_path = "images/educator1.png"
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
        name.place(relx=0, y=405, relwidth=self.profile_frame.winfo_width())

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
        username.place(relx=0, y=490, relwidth=self.profile_frame.winfo_width())

        # User role
        role_label = customtkinter.CTkLabel(self.profile_frame,
                                            text='R O L E',
                                            font=("Cascadia Code Bold", 14),
                                            fg_color="#4E6F86",
                                            anchor="center"
                                            )
        role_label.place(relx=0, y=540, relwidth=self.profile_frame.winfo_width())

        role = customtkinter.CTkLabel(self.profile_frame,
                                      text="Learner",
                                      font=("Arial", 14),
                                      anchor="center")
        role.place(relx=0, y=575, relwidth=self.profile_frame.winfo_width())

        # Module in charge
        module_label = customtkinter.CTkLabel(self.profile_frame,
                                              text="M O D U L E",
                                              font=("Cascadia Code Bold", 14),
                                              fg_color="#4E6F86",
                                              anchor="center"
                                              )
        module_label.place(relx=0, y=625, relwidth=self.profile_frame.winfo_width())

        module = customtkinter.CTkLabel(self.profile_frame,
                                        text=f"{self.module_name}",
                                        font=("Arial", 14),
                                        anchor="center")
        module.place(relx=0, y=660, relwidth=self.profile_frame.winfo_width())

    def show_dashboard_frame(self):
        """
        Method to show the dashboard page (homepage for learner)
        """
        self.current_frame.place_forget()
        self.welcome_frame.grid(row=0, column=0, padx=30, pady=50, sticky="ew")
        self.profile_frame.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)
        self.educator_frame.place(relx=0.2, rely=0, relwidth=0.6, relheight=1)

    def show_forum_window(self):
        """
        Method to show the dashboard page (homepage for learner)
        """
        if not self.forum_open:
            self.forum_open = True
            # Create a new Toplevel window
            self.forum_window = customtkinter.CTkToplevel(self.master,
                                                          fg_color="#C2D3DF")
            self.forum_window.geometry("980x670")

            self.forum_window.title(f"Module {self.module_id + 1}: {self.module_name}")

            window_frame = customtkinter.CTkScrollableFrame(self.forum_window,
                                                            fg_color="transparent")
            window_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

            # main frame
            main_frame = customtkinter.CTkFrame(window_frame,
                                                corner_radius=20,
                                                fg_color="#FAFAFA",
                                                )
            main_frame.grid(row=0, column=0, padx=40, pady=50, sticky="ew")

            module_title = customtkinter.CTkLabel(master=main_frame,
                                                  text=f'Module ({self.module_id + 1}) Discussion Forum',
                                                  font=("Fixedsys", 24),
                                                  anchor="sw",
                                                  text_color="#6895B2",
                                                  justify="left"
                                                  )
            module_title.grid(row=0, column=0, padx=30, pady=30, sticky="sw")

            text = customtkinter.CTkLabel(main_frame,
                                          text="Ask any questions you have about this module!",
                                          font=("Fixedsys", 20),
                                          text_color="#6895B2",
                                          justify="left")
            text.grid(row=1, column=0, padx=30, pady=5, sticky="sw")

            new_post_frame = customtkinter.CTkFrame(main_frame, corner_radius=10, fg_color="#6895B2")
            new_post_frame.grid(row=2, column=0, padx=30, pady=30, sticky="sw")

            discussions_title = customtkinter.CTkLabel(main_frame,
                                                       text="Discussions",
                                                       font=("Fixedsys", 20),
                                                       text_color="#6895B2"
                                                       )
            discussions_title.grid(row=3, column=0, padx=30, pady=10, sticky="sw")

            discussions = self.system_storage.get_forum_posts(self.module_id)

            discussion_frame = customtkinter.CTkFrame(main_frame,
                                                      fg_color="transparent")
            discussion_frame.grid(row=4, column=0, padx=0, pady=0, sticky="nw")

            add_new_post = customtkinter.CTkLabel(new_post_frame, text="Create New Post",
                                                  text_color="white",
                                                  font=("Fixedsys", 22))
            add_new_post.grid(row=0, column=0, padx=20, pady=20, sticky="sw")

            new_post_entry = customtkinter.CTkTextbox(new_post_frame, width=800, height=120,
                                                      fg_color="#FAFAFA",
                                                      text_color="#6895B2")
            new_post_entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

            def submit_post():
                response = messagebox.askyesno("Confirmation", "Are you sure you want to submit this post?")

                if response:
                    post_content = new_post_entry.get("1.0", "end")
                    date_of_post = datetime.now().strftime("%Y-%m-%d")
                    self.system_storage.insert_forum_post(self.module_id,
                                                          self.user.get_username(),
                                                          self.user.get_role(),
                                                          post_content,
                                                          date_of_post)

                    new_post_entry.delete("1.0", "end")

                    post_frame = customtkinter.CTkFrame(discussion_frame, corner_radius=10, fg_color="#6895B2")
                    post_frame.grid(row=self.current_row, column=0, padx=30, pady=10, sticky="new")

                    post_username = customtkinter.CTkLabel(post_frame,
                                                           text=f'@{self.user.get_username()}',
                                                           text_color="white",
                                                           font=("Calibri Bold", 16))
                    post_username.grid(row=0, column=0, padx=20, pady=5, sticky="sw")

                    post_date = customtkinter.CTkLabel(post_frame,
                                                       text=f'Date posted: {date_of_post}',
                                                       text_color="white",
                                                       font=("Calibri", 14))
                    post_date.grid(row=1, column=0, padx=20, pady=5, sticky="sw")

                    post_content_label = customtkinter.CTkLabel(post_frame,
                                                                text=post_content,
                                                                font=("Calibri", 16),
                                                                justify="left",
                                                                wraplength=800)
                    post_content_label.grid(row=2, column=0, padx=20, pady=5, sticky="nw")

                    reply_label = customtkinter.CTkLabel(post_frame,
                                                         text="\nReplies",
                                                         font=("Calibri Bold", 16),
                                                         text_color="white")
                    reply_label.grid(row=3, column=0, padx=20, pady=10, sticky="nw")

                    no_replies = customtkinter.CTkLabel(post_frame,
                                                        text="No replies yet...",
                                                        )
                    no_replies.grid(row=4, column=0, padx=20, pady=10, sticky="nw")

                    make_reply = customtkinter.CTkLabel(post_frame, text="Reply To This Post",
                                                        text_color="white",
                                                        font=("Calibri Bold", 16))
                    make_reply.grid(row=5, column=0, padx=20, pady=20, sticky="nw")

                    make_reply_entry = customtkinter.CTkTextbox(post_frame, width=800, height=50,
                                                                fg_color="#FAFAFA",
                                                                text_color="#6895B2")
                    make_reply_entry.grid(row=6, column=0, padx=20, pady=10, sticky="ew")

                    reply_btn1 = customtkinter.CTkButton(post_frame,
                                                         text="Reply",
                                                         text_color="white",
                                                         # command=lambda: submit_post())
                                                         )

                    reply_btn1.grid(row=7, column=0, padx=10, pady=10, sticky="ew")
                    self.current_row += 1

            post_button = customtkinter.CTkButton(new_post_frame,
                                                  text="Submit Post",
                                                  text_color="white",
                                                  command=lambda: submit_post())
            post_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

            # display all existing posts for this module
            if discussions is not None:
                for i in range(len(discussions)):
                    post_data = discussions[i]
                    forum_id = post_data[0]
                    p_username = post_data[2]
                    p_role = post_data[3]
                    p_content = post_data[4]
                    p_date_posted = post_data[5]

                    post = customtkinter.CTkFrame(discussion_frame, corner_radius=10, fg_color="#6895B2")
                    post.grid(row=self.current_row, column=0, padx=30, pady=10, sticky="new")

                    username = customtkinter.CTkLabel(post,
                                                      text=f'@{p_username} (Educator)',
                                                      text_color="white",
                                                      font=("Calibri Bold", 16))
                    username.grid(row=0, column=0, padx=20, pady=5, sticky="sw")

                    date = customtkinter.CTkLabel(post,
                                                  text=f'Date Posted: {p_date_posted}',
                                                  text_color="white",
                                                  font=("Calibri", 14))
                    date.grid(row=1, column=0, padx=20, pady=5, sticky="sw")

                    content = customtkinter.CTkLabel(post,
                                                     text=p_content,
                                                     font=("Calibri", 16),
                                                     justify="left",
                                                     wraplength=800)
                    content.grid(row=2, column=0, padx=20, pady=10, sticky="nw")

                    replies_label = customtkinter.CTkLabel(post,
                                                           text="\nReplies",
                                                           font=("Calibri Bold", 16),
                                                           text_color="white")
                    replies_label.grid(row=3, column=0, padx=20, pady=10, sticky="nw")

                    replies = self.system_storage.get_replies(forum_id)

                    if replies is None:
                        reply_text = customtkinter.CTkLabel(post,
                                                            text_color="white",
                                                            text="No replies yet...",
                                                            )
                        reply_text.grid(row=5, column=0, padx=20, pady=10, sticky="nw")

                    else:
                        replies_frame = customtkinter.CTkFrame(post,
                                                               fg_color="#FAFAFA",
                                                               corner_radius=20)
                        replies_frame.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

                        for j in range(len(replies)):
                            reply_data = replies[j]
                            replied_user = reply_data[2]
                            # replied_role = reply_data[3]
                            content = reply_data[4]
                            date_replied = reply_data[5]

                            reply = customtkinter.CTkFrame(replies_frame, corner_radius=10, fg_color="#FAFAFA")
                            reply.grid(row=j, column=0, padx=30, pady=10, sticky="new")

                            username = customtkinter.CTkLabel(reply,
                                                              text=f'@{replied_user} (Learner)',
                                                              text_color="#6895B2",
                                                              font=("Calibri Bold", 16))
                            username.grid(row=0, column=0, padx=20, pady=5, sticky="sw")

                            date = customtkinter.CTkLabel(reply,
                                                          text=f'Reply Date: {date_replied}',
                                                          text_color="#6895B2",
                                                          font=("Calibri", 14))
                            date.grid(row=1, column=0, padx=20, pady=5, sticky="sw")

                            content = customtkinter.CTkLabel(reply,
                                                             text=content,
                                                             font=("Calibri", 16),
                                                             justify="left",
                                                             text_color="#6895B2",
                                                             wraplength=800)
                            content.grid(row=2, column=0, padx=20, pady=10, sticky="nw")

                    self.current_row += 1

                    reply1_label = customtkinter.CTkLabel(post, text="Reply To This Post",
                                                          text_color="white",
                                                          font=("Calibri Bold", 16))
                    reply1_label.grid(row=6, column=0, padx=20, pady=20, sticky="nw")

                    reply1_entry = customtkinter.CTkTextbox(post, width=800, height=50,
                                                            fg_color="#FAFAFA",
                                                            text_color="#6895B2")
                    reply1_entry.grid(row=7, column=0, padx=20, pady=10, sticky="ew")

                    reply_btn2 = customtkinter.CTkButton(post,
                                                         text="Reply",
                                                         text_color="white",
                                                         # command=lambda: submit_post())
                                                         )

                    reply_btn2.grid(row=8, column=0, padx=10, pady=10, sticky="ew")

            def on_close():
                """
                Method to close the window
                """
                self.forum_open = False
                self.forum_window.destroy()

            self.forum_window.protocol("WM_DELETE_WINDOW", on_close)

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
        self.educator_frame.place_forget()
        self.nav_bar.place_forget()
        self.profile_frame.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

