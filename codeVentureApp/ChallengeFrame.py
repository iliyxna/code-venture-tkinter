import customtkinter

from codeVentureApp.SystemStorage import SystemStorage


class ChallengeFrame(customtkinter.CTkFrame):
    """
    Each challenge will be a tiny frame
    """

    def __init__(self, master, challenge_id):
        super().__init__(master)
        self.master = master
        self.challenge_id = challenge_id
        self.configure(corner_radius=20,
                       fg_color="#228B22",
                       width=880
                       )
        self.system_storage = SystemStorage()

        challenge = self.system_storage.get_challenge_data(challenge_id)
        challenge_name = challenge.get_challenge_name()
        challenge_intro = challenge.get_intro()
        challenge_level = challenge.get_difficulty()

        # Different card colours
        if challenge_level == "Intermediate":
            self.configure(fg_color="#F28C28")
        if challenge_level == "Advanced":
            self.configure(fg_color="#D22B2B")

        name_label = customtkinter.CTkLabel(self,
                                            text=f'\n({challenge_id + 1}) {challenge_name}',
                                            font=("Fixedsys", 20),
                                            wraplength=880,
                                            justify="left",
                                            text_color="white",
                                            anchor="sw",
                                            )
        name_label.grid(row=0, column=0, padx=20, pady=10, sticky="sw")

        intro = customtkinter.CTkLabel(self,
                                       text=f'\n{challenge_intro}',
                                       text_color="white",
                                       wraplength=830,
                                       justify="left"
                                       )
        intro.grid(row=2, columnspan=2, padx=20, sticky="w")

        level = customtkinter.CTkLabel(self,
                                       text=f'Difficulty: {challenge_level}',
                                       text_color="white",
                                       font=("Cascadia Code",14),
                                       fg_color="#355E3B",
                                       corner_radius=10
                                       )
        if challenge_level == "Intermediate":
            level.configure(fg_color="#B87333")
        if challenge_level == "Advanced":
            level.configure(fg_color="#880808")
        level.grid(row=1, column=0, padx=20, pady=10, sticky="nw")

        start_button = customtkinter.CTkButton(self,
                                               fg_color="white",
                                               text_color="#638294",
                                               text="Start",
                                               command=self.start_challenge)
        start_button.grid(row=3, column=0, padx=20, pady=20, sticky="nw")

    def start_challenge(self):
        pass


