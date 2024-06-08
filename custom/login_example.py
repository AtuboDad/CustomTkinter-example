import customtkinter

from custom.login_frame import LoginFrame

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 700
    height = 450

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configure window
        self.title("XXX soft")
        self.geometry(f"{700}x{450}")

        # create login frame
        self.login_frame = LoginFrame(master=self)
