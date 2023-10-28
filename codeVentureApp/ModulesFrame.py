import customtkinter

from codeVentureApp.SystemStorage import SystemStorage
from codeVentureApp.learning_materials.Module import Module


class ModuleFrame(customtkinter.CTkFrame):
    """
    Each module will be a tiny frame
    """

    def __init__(self, master, module_id):
        super().__init__(master)
        self.master = master
        self.module_id = module_id
        self.configure(corner_radius=20,
                       fg_color="#638294",
                       width=830
                       )
        self.system_storage = SystemStorage()

        module = self.system_storage.get_module_data(module_id)
        module_name = module.get_module_name()
        module_intro = module.get_intro()
        module_level = module.get_level()

        # Different card colours
        if module_level == "Intermediate":
            self.configure(fg_color="#435560")
        if module_level == "Advanced":
            self.configure(fg_color="#223039")

        name_label = customtkinter.CTkLabel(self,
                                            text=f'\n({module_id + 1}) {module_name}',
                                            font=("Fixedsys", 20),
                                            text_color="white",
                                            anchor="sw",
                                            )
        name_label.grid(row=0, column=0, padx=20, pady=10, sticky="sw")

        intro = customtkinter.CTkLabel(self,
                                       text=f'\n{module_intro}',
                                       text_color="white",
                                       wraplength=830,
                                       justify="left"
                                       )
        intro.grid(row=1, columnspan=2, padx=20, sticky="w")

        level = customtkinter.CTkLabel(self,
                                       text=f'Difficulty: {module_level}',
                                       text_color="white",
                                       font=("Cascadia Code",14),
                                       fg_color="#6895B2",
                                       corner_radius=10
                                       )
        if module_level == "Intermediate":
            level.configure(fg_color="#6F818D")
        if module_level == "Advanced":
            level.configure(fg_color="#4A697D")
        level.grid(row=0, column=1, padx=20, pady=10, sticky="se")

        start_button = customtkinter.CTkButton(self,
                                               fg_color="white",
                                               text_color="#638294",
                                               text="Start")
        start_button.grid(row=2, column=0, padx=20, pady=20, sticky="nw")



