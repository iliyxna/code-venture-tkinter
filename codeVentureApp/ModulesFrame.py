from datetime import datetime
from tkinter import messagebox

import customtkinter
import tkinter as tk

from codeVentureApp.QuizFrame import QuizFrame
from codeVentureApp.SystemStorage import SystemStorage


class ModuleFrame(customtkinter.CTkFrame):
    """
    Each module will be a tiny frame
    """

    def __init__(self, master, module_id, user, learner_dashboard):
        """
        Constructor
        """
        super().__init__(master)
        self.i1 = None
        self.i2 = None
        self.master = master
        self.module_id = module_id
        self.learner_dashboard = learner_dashboard
        self.configure(corner_radius=20,
                       fg_color="#638294",
                       # width=830
                       )
        self.user = user
        # Flag to check if the window is open
        self.window_open = False
        self.new_window = None

        self.current_row = 4

        self.forum_open = False
        self.forum_window = None

        self.system_storage = SystemStorage()

        self.module = self.system_storage.get_module_data(module_id)
        self.module_name = self.module.get_module_name()
        self.module_intro = self.module.get_intro()
        self.module_level = self.module.get_level()

        # Different card colours
        if self.module_level == "Intermediate":
            self.configure(fg_color="#435560")
        if self.module_level == "Advanced":
            self.configure(fg_color="#223039")

        name_label = customtkinter.CTkLabel(self,
                                            text=f'\n({module_id + 1}) {self.module_name}',
                                            font=("Fixedsys", 20),
                                            text_color="white",
                                            anchor="sw",
                                            )
        name_label.grid(row=0, column=0, padx=20, pady=10, sticky="sw")

        if self.system_storage.check_learner_module(self.module_id, self.user.get_username()):
            mark_completed = customtkinter.CTkFrame(self, fg_color="white", corner_radius=5)
            mark_completed.grid(row=0, column=1, padx=20, pady=5, sticky="se")
            complete_label = customtkinter.CTkLabel(mark_completed, text="Completed", text_color="#223039")
            complete_label.grid(row=0, column=0, padx=10, pady=5)

        if self.learner_dashboard:
            wrap_value = 650
        else:
            wrap_value = 830
        intro = customtkinter.CTkLabel(self,
                                       text=f'\n{self.module_intro}',
                                       text_color="white",
                                       wraplength=wrap_value,
                                       justify="left"
                                       )
        intro.grid(row=2, columnspan=2, padx=20, sticky="w")

        level = customtkinter.CTkLabel(self,
                                       text=f'Difficulty: {self.module_level}',
                                       text_color="white",
                                       font=("Cascadia Code", 14),
                                       fg_color="#6895B2",
                                       corner_radius=10
                                       )
        if self.module_level == "Intermediate":
            level.configure(fg_color="#6F818D")
        if self.module_level == "Advanced":
            level.configure(fg_color="#4A697D")
        level.grid(row=1, column=0, padx=20, pady=10, sticky="nw")

        start_button = customtkinter.CTkButton(self,
                                               fg_color="white",
                                               text_color="#638294",
                                               text="Start",
                                               command=self.start_module)
        start_button.grid(row=3, column=0, padx=20, pady=20, sticky="nw")

        forum_button = customtkinter.CTkButton(self,
                                               fg_color="white",
                                               text_color="#638294",
                                               text="Discussion Forum",
                                               command=self.open_forum)
        forum_button.grid(row=3, column=1, padx=20, pady=20, sticky="ne")

    def start_module(self):
        """
        Method that spawns a new window for the tutorial and quizzes
        """
        if not self.window_open:
            self.window_open = True
            # Create a new Toplevel window
            self.new_window = customtkinter.CTkToplevel(self.master,
                                                        fg_color="#C2D3DF")
            self.new_window.geometry("980x670")
            self.new_window.title(f"Module {self.module_id + 1}: {self.module_name}")

            # Add your content to the new window here
            window_frame = customtkinter.CTkScrollableFrame(self.new_window,
                                                            fg_color="transparent")
            window_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

            # top frame
            tutorial_frame = customtkinter.CTkFrame(window_frame,
                                                    corner_radius=20,
                                                    fg_color="#FAFAFA",
                                                    )
            tutorial_frame.grid(row=0, column=0, padx=40, pady=50, sticky="ew")

            module_title = customtkinter.CTkLabel(master=tutorial_frame,
                                                  text=f'Module {self.module_id + 1}: {self.module_name}',
                                                  font=("Fixedsys", 24),
                                                  anchor="sw",
                                                  text_color="#6895B2",
                                                  justify="left"
                                                  )
            module_title.grid(row=0, column=0, padx=30, pady=30, sticky="sw")

            tutorial_title = customtkinter.CTkLabel(master=tutorial_frame,
                                                    text=f'Tutorial',
                                                    font=("Fixedsys", 22),
                                                    text_color="#6895B2",
                                                    anchor="sw",
                                                    justify="left"
                                                    )
            tutorial_title.grid(row=1, column=0, padx=30, pady=10, sticky="sw")

            tutorial = self.system_storage.get_tutorial_data(self.module.get_tutorial_id())

            c1 = customtkinter.CTkLabel(master=tutorial_frame,
                                        text=f'{tutorial.get_c1()}',
                                        text_color="#6895B2",
                                        # anchor="sw",
                                        wraplength=830,
                                        justify="left"
                                        )
            c1.grid(row=2, column=0, padx=30, pady=5, sticky="sw")

            if tutorial.get_i1() != "":
                self.i1 = tk.PhotoImage(file=f'images/{tutorial.get_i1()}.png')
                i1 = tk.Label(master=tutorial_frame,
                              image=self.i1,
                              borderwidth=0,
                              justify="left",
                              )
                i1.grid(row=3, column=0, padx=30, pady=5, sticky="nw")

            if tutorial.get_c2() != "":
                c2 = customtkinter.CTkLabel(master=tutorial_frame,
                                            text=f'{tutorial.get_c2()}',
                                            text_color="#6895B2",
                                            anchor="sw",
                                            wraplength=830,
                                            justify="left"
                                            )
                c2.grid(row=4, column=0, padx=30, pady=5, sticky="sw")

            if tutorial.get_i2() != "":
                self.i2 = tk.PhotoImage(file=f'images/{tutorial.get_i2()}.png')
                i2 = tk.Label(master=tutorial_frame,
                              image=self.i2,
                              borderwidth=0,
                              anchor="w",
                              justify="left"
                              )
                i2.grid(row=5, column=0, padx=30, pady=5, sticky="w")

            if tutorial.get_c3() != "":
                c2 = customtkinter.CTkLabel(master=tutorial_frame,
                                            text=f'{tutorial.get_c3()}',
                                            text_color="#6895B2",
                                            anchor="w",
                                            wraplength=830,
                                            justify="left"
                                            )
                c2.grid(row=6, column=0, padx=30, pady=5, sticky="w")

            def start_quiz():
                """
                Method to start the quiz
                """
                quiz_frame = customtkinter.CTkFrame(window_frame,
                                                    corner_radius=20,
                                                    fg_color="#FAFAFA",
                                                    )
                quiz_frame.grid(row=1, column=0, padx=40, sticky="ew")

                quiz_title = customtkinter.CTkLabel(master=quiz_frame,
                                                    text=f'It\'s Quiz Time! 🧠💡',
                                                    font=("Fixedsys", 23),
                                                    text_color="#6895B2",
                                                    anchor="sw",
                                                    justify="left"
                                                    )
                quiz_title.grid(row=0, column=0, padx=30, pady=30, sticky="sw")

                ques_frame = customtkinter.CTkFrame(quiz_frame,
                                                    corner_radius=20,
                                                    fg_color="#FAFAFA",
                                                    )
                ques_frame.grid(row=1, column=0, padx=30, sticky="new")

                curr_row = 1
                self.user.current_module_score = 0
                self.user.answered_count = 0

                for i in range(self.module.get_tutorial_id() * 3, self.module.get_tutorial_id() * 3 + 3):
                    quiz_card = QuizFrame(self.new_window, ques_frame, i, self.user, self.module_id, self)
                    quiz_card.grid(row=curr_row, column=0, padx=30, pady=20, sticky="sw")
                    curr_row += 1

            quiz_button = customtkinter.CTkButton(master=tutorial_frame,
                                                  text="Start Quiz",
                                                  text_color="white",
                                                  fg_color="#435560",
                                                  command=start_quiz
                                                  )
            quiz_button.grid(row=7, column=0, padx=30, pady=20, sticky="nw")

            # Function to run when the new window is closed
            def on_close():
                """
                Method to close the window
                """
                self.window_open = False
                self.new_window.destroy()

            self.new_window.protocol("WM_DELETE_WINDOW", on_close)

    def open_forum(self):
        """
        Method that spawns a new window for the tutorial and quizzes
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

                                                         )

                    reply_btn1.grid(row=7, column=0, padx=10, pady=10, sticky="ew")
                    self.current_row += 1

            post_button = customtkinter.CTkButton(new_post_frame,
                                                  text="Submit Post",
                                                  text_color="white",
                                                  command=lambda: submit_post())
            post_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

            current_forum_id = 0

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
                                                      text=f'@{p_username} ({p_role})',
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

                    # Get the replies for that post
                    replies = self.system_storage.get_replies(forum_id)

                    # frame for all the replies
                    replies_frame = customtkinter.CTkFrame(post,
                                                           fg_color="white",
                                                           corner_radius=20)
                    replies_frame.grid(row=4, column=0, padx=20, pady=10, sticky="new")

                    num_replies = 0

                    if replies is None:
                        reply_text = customtkinter.CTkLabel(replies_frame,
                                                            text_color="#6895B2",
                                                            text="No replies yet...",
                                                            )
                        reply_text.grid(row=0, column=0, padx=20, pady=10, sticky="nw")

                    else:
                        for j in range(len(replies)):
                            reply_data = replies[j]
                            replied_user = reply_data[2]
                            replied_role = reply_data[3]
                            content = reply_data[4]
                            date_replied = reply_data[5]

                            # keep each reply in a frame in replies_frame
                            reply = customtkinter.CTkFrame(replies_frame, corner_radius=10, fg_color="#3C596B")
                            reply.grid(row=j, column=0, padx=20, pady=20, sticky="new")

                            username = customtkinter.CTkLabel(reply,
                                                              text=f'@{replied_user} ({replied_role})',
                                                              text_color="white",
                                                              font=("Calibri Bold", 16))
                            username.grid(row=0, column=0, padx=10, pady=5, sticky="sw")

                            date = customtkinter.CTkLabel(reply,
                                                          text=f'Reply Date: {date_replied}',
                                                          text_color="white",
                                                          font=("Calibri", 14))
                            date.grid(row=1, column=0, padx=10, pady=5, sticky="sw")

                            content = customtkinter.CTkLabel(reply,
                                                             text=content,
                                                             font=("Calibri", 16),
                                                             justify="left",
                                                             text_color="white",
                                                             wraplength=800)
                            content.grid(row=2, column=0, padx=10, pady=10, sticky="nw")

                            num_replies += 1

                    self.current_row += 1

                    # reply post
                    reply1_label = customtkinter.CTkLabel(post, text="Reply To This Post",
                                                          text_color="white",
                                                          font=("Calibri Bold", 16))
                    reply1_label.grid(row=6, column=0, padx=20, pady=20, sticky="nw")

                    def reply_to_post():
                        dialog = customtkinter.CTkInputDialog(text="Enter Reply: ", title="Reply to Post")
                        post_reply = dialog.get_input()
                        print(post_reply)
                        print(forum_id)

                    add_reply_button = customtkinter.CTkButton(post, text="Create a Reply",
                                                               fg_color="white",
                                                               text_color="#6895B2",
                                                               command=reply_to_post)
                    add_reply_button.grid(row=7, column=0, padx=20, pady=10, sticky="w")

            def on_close():
                """
                Method to close the window
                """
                self.forum_open = False
                self.forum_window.destroy()

            self.forum_window.protocol("WM_DELETE_WINDOW", on_close)