import customtkinter

from navigation_frame import NavigationFrame

customtkinter.set_appearance_mode("dark")


class MianFrame(customtkinter.CTkFrame):

    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, corner_radius=0)
        
        # create main frame
        self.navigation_frame = NavigationFrame(master=self)

    def show(self):
        self.pack(fill="both", expand=True)
        
        self.navigation_frame.show()