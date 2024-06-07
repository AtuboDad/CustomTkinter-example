import customtkinter
from tkinter import messagebox
from PIL import Image
import os

from navigation_frame import NavigationFrame
from index_frame import IndexFrame

customtkinter.set_appearance_mode("dark")


class MianFrame(customtkinter.CTkFrame):
    width = 700
    height = 450

    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, corner_radius=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create main frame
        self.navigation_frame = NavigationFrame(master=self)

    def show(self):
        self.grid(row=0, column=0, sticky="nsew")
        
        self.navigation_frame.show()