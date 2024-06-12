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
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0)
        
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image, compound="left", padx=40, anchor="w", fg_color="transparent")
        self.home_frame_large_image_label.pack(fill='x')

        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self.home_frame, command=self.checkbox_frame_event, fg_color="transparent",
                                                                 item_list=[f"item {i}" for i in range(15)])
        self.scrollable_checkbox_frame.pack(fill='both', expand=True)
        self.scrollable_checkbox_frame.add_item("new item")

    def show(self, name):
        if name == "home":
            self.pack(side='right', fill='both', expand=True)
            self.home_frame.pack(fill='both', expand=True)
        else:
            self.pack_forget()
    
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
        self.label_1 = []
        self.label_2 = []
        self.label_3 = []
        self.label_4 = []
        self.button_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        checkbox = customtkinter.CTkCheckBox(self, text=item, width=200)
        label1 = customtkinter.CTkLabel(self, text='测试数据1', compound="left", padx=10, anchor="w")
        label2 = customtkinter.CTkLabel(self, text='测试数据2', compound="left", padx=10, anchor="w")
        label3 = customtkinter.CTkLabel(self, text='测试数据3', compound="left", padx=10, anchor="w")
        label4 = customtkinter.CTkLabel(self, text='测试数据4', compound="left", padx=10, anchor="w")
        button = customtkinter.CTkButton(self, text="删 除", width=60, height=24, fg_color='#F56C6C')
        
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list), column=0, padx=(40, 0), pady=5)
        label1.grid(row=len(self.label_1), column=1, padx=5, pady=5, sticky="w")
        label2.grid(row=len(self.label_2), column=2, padx=5, pady=5, sticky="w")
        label3.grid(row=len(self.label_3), column=3, padx=5, pady=5, sticky="w")
        label4.grid(row=len(self.label_4), column=4, padx=5, pady=5, sticky="w")
        button.grid(row=len(self.button_list), column=5, padx=5, pady=5)
        self.checkbox_list.append(checkbox)
        self.label_1.append(label1)
        self.label_2.append(label2)
        self.label_3.append(label3)
        self.label_4.append(label4)
        self.button_list.append(button)

    def remove_item(self, item):
        for checkbox, button, label in zip(self.checkbox_list, self.button_list, self.label_1):
            if item == checkbox.cget("text"):
                checkbox.destroy()
                button.destroy()
                label.destroy()
                self.checkbox_list.remove(checkbox)
                self.label_1.remove(label)
                self.button_list.remove(button)
                return
        

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]