import customtkinter

from custom.main_frame import MianFrame

customtkinter.set_appearance_mode("dark")


class LoginFrame(customtkinter.CTkFrame):
    width = 700
    height = 450

    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, corner_radius=0)

        # self.grid(row=0, column=0, sticky="nsw")
        self.pack(fill="both", expand=True)
        self.login_label = customtkinter.CTkLabel(self, text="CustomTkinter\nLogin Page",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.pack(pady=(100, 15))
        self.username_entry = customtkinter.CTkEntry(self, width=200, placeholder_text="username")
        self.username_entry.pack(pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self, width=200, show="*", placeholder_text="password")
        self.password_entry.pack(pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.login_event, width=200)
        self.login_button.pack(pady=(15, 15))

                
        # create main frame
        self.main_frame = MianFrame(master=master)

    def login_event(self):
        # if not self.username_entry.get():
        #     messagebox.showinfo('info', 'Enter username please')
        #     return
        # if not self.password_entry.get():
        #     messagebox.showinfo('info', 'Enter password please')
        #     return
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())

        self.pack_forget()  # remove login frame
        self.main_frame.show()

    def back_event(self):
        # remove main frame
        self.main_frame.pack_forget()
        self.pack(fill="both", expand=True)  # show login frame