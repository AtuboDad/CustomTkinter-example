import customtkinter
from tkinter import messagebox
from PIL import Image
import os

from index_frame import IndexFrame
from login_frame import LoginFrame

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 700
    height = 450

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configure window
        self.title("XXX软件")
        self.geometry(f"{700}x{450}")
        self.resizable(False, False)
        

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/test_images/bg_gradient.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = LoginFrame(master=self)


        # self.main_label = customtkinter.CTkLabel(self.main_frame, text="CustomTkinter\nMain Page",
        #                                          font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        # self.back_button = customtkinter.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
        # self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

    


if __name__ == "__main__":
    app = App()
    app.mainloop()
