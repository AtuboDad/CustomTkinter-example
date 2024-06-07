import customtkinter
from tkinter import messagebox
from PIL import Image
import os

from main_frame import MianFrame

customtkinter.set_appearance_mode("dark")


class LoginFrame(customtkinter.CTkFrame):
    width = 700
    height = 450

    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, corner_radius=0)

        self.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self, text="CustomTkinter\nLogin Page",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(self, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

                
        # create main frame
        self.main_frame = MianFrame(master=master)

    def login_event(self):
        # if not self.username_entry.get():
        #     messagebox.showinfo('提示', '请输入用户名')
        #     return
        # if not self.password_entry.get():
        #     messagebox.showinfo('提示', '请输入密码')
        #     return
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())

        self.grid_forget()  # remove login frame
        self.main_frame.show()

    def back_event(self):
        # remove main frame
        self.main_frame.grid_forget()
        self.grid(row=0, column=0, sticky="nsew")  # show login frame