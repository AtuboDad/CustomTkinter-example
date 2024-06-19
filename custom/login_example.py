import customtkinter

from custom.login_frame import LoginFrame

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 700
    height = 450

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 获取屏幕宽高
        window_width = self.winfo_screenwidth()
        window_height = self.winfo_screenheight()

        x = (window_width - self.winfo_width()) // 2
        y = (window_height - self.winfo_height()) // 2

        # configure window
        self.title("XXX soft")
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

        # create login frame
        self.login_frame = LoginFrame(master=self)
