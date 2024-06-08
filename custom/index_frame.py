import customtkinter
import os
from PIL import Image

customtkinter.set_appearance_mode("dark")


class IndexFrame(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master, corner_radius=0)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self.home_frame, command=self.checkbox_frame_event,
                                                                 item_list=[f"item {i}" for i in range(20)])
        self.scrollable_checkbox_frame.pack(fill='both', expand=True)
        self.scrollable_checkbox_frame.add_item("new item")

    def show(self, name):
        if name == "home":
            self.pack(side='right', fill='both', expand=True)
            self.home_frame.pack(fill='both', expand=True)
        else:
            self.grid_forget()
    
    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")

    # def radiobutton_frame_event(self):
    #     print(f"radiobutton frame modified: {self.scrollable_radiobutton_frame.get_checked_item()}")

    def label_button_frame_event(self, item):
        print(f"label button frame clicked: {item}")


class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []
        self.button_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        checkbox = customtkinter.CTkCheckBox(self, text=item, width=200)
        button = customtkinter.CTkButton(self, text="删 除", width=60, height=24, fg_color='#F56C6C')
        
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list), column=0, pady=5)
        button.grid(row=len(self.button_list), column=1, pady=5, padx=5)
        self.checkbox_list.append(checkbox)
        self.button_list.append(button)

    def remove_item(self, item):
        for checkbox, button in zip(self.checkbox_list, self.button_list):
            if item == checkbox.cget("text"):
                checkbox.destroy()
                button.destroy()
                self.checkbox_list.remove(checkbox)
                self.button_list.remove(button)
                return

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]