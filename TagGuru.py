import customtkinter
import os
from PIL import Image

from tkinter import PhotoImage
import tkinter.messagebox
import customtkinter
import requests
import pyperclip
import tkinter as tk

import webbrowser
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("TagGuru by@Adres_Dev")
        self.geometry("700x450")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

       
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "main_logo.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_light.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_dark.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "youtube_light.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "youtube_dark.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "tiktok_light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "tiktok_dark.png")), size=(20, 20))

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="   TagGuru ", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Youtube",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        
        

        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="TikTok",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        def Discord():
            webbrowser.open("https://discord.gg/td8wzKhXSJ")
        def channel():
            webbrowser.open("https://www.youtube.com/@d-ev")

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image,command=Discord)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="My Channel", image=self.image_icon_image, compound="right",command=channel)
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)


        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.select_frame_by_name("home")
        
        #Youtube_Fream_UI
        def youtube_get_tag():
            def get_tags(event=None):

                tag = entry.get()
                link = f"https://rapidtags.io/api/generator?query={tag}&type=YouTube"
                send = requests.get(link)
                if send.status_code == 200:
                    response_dict = send.json()
                    tags = response_dict.get("tags")
                    if tags:
                        output.configure(state='normal')
                        output.delete(1.0, customtkinter.END)
                        for tag in tags:
                            output.insert(customtkinter.END, f"{tag}\n")
                        output.configure(state='disabled')
                    else:
                        output.configure(state='normal')
                        output.delete(1.0, customtkinter.END)
                        output.insert(customtkinter.END, "No tags found.")
                        output.configure(state='disabled')
                else:
                    output.configure(state='normal')
                    output.delete(1.0,customtkinter.END)
                    output.insert(customtkinter.END, f"Error {send.status_code} occurred.")
                    output.configure(state='disabled')
            def copy_tags():
                
                tags_str = output.get(1.0, customtkinter.END)
                pyperclip.copy(tags_str+"Adres_Dev")
                def show_message_box():
                    tkinter.messagebox.showinfo("النظام", "تم النسخ ")
                show_message_box()




            label = customtkinter.CTkLabel(self.second_frame, text="Enter a tag:")

            label.pack()


            entry = customtkinter.CTkEntry(self.second_frame)

            entry.pack()

            entry.bind('<Return>', get_tags)

            button = customtkinter.CTkButton(self.second_frame, text="Extract tags", command=get_tags)
            button.pack(pady=20)

            copy_button = customtkinter.CTkButton(self.second_frame, text="Copy Tags", command=copy_tags)
            copy_button.pack(pady=10)

            output = customtkinter.CTkTextbox(self.second_frame, height=300, width=400, state='disabled')
            output.pack(pady=60, padx=60)



            App.mainloop()
        
        self.SEO_TITLE = customtkinter.CTkButton(self.second_frame, text=" Extract tags Tool ",command=youtube_get_tag)
        self.SEO_TITLE.pack(pady=20,padx=0.9)
        #tiktok_Fream_UI
        def youtube_get_tag():
            def get_tags(event=None):

                tag = entry.get()
                link = f"https://rapidtags.io/api/generator?query={tag}&type=TikTok"
                send = requests.get(link)
                if send.status_code == 200:
                    response_dict = send.json()
                    tags = response_dict.get("tags")
                    if tags:
                        output.configure(state='normal')
                        output.delete(1.0, customtkinter.END)
                        for tag in tags:
                            output.insert(customtkinter.END, f"{tag}\n")
                        output.configure(state='disabled')
                    else:
                        output.configure(state='normal')
                        output.delete(1.0, customtkinter.END)
                        output.insert(customtkinter.END, "No tags found.")
                        output.configure(state='disabled')
                else:
                    output.configure(state='normal')
                    output.delete(1.0,customtkinter.END)
                    output.insert(customtkinter.END, f"Error {send.status_code} occurred.")
                    output.configure(state='disabled')
            def copy_tags():
                
                tags_str = output.get(1.0, customtkinter.END)
                pyperclip.copy(tags_str+"Adres_Dev")
                def show_message_box():
                    tkinter.messagebox.showinfo("النظام", "تم النسخ ")
                show_message_box()




            label = customtkinter.CTkLabel(self.third_frame, text="Enter a tag:")

            label.pack()


            entry = customtkinter.CTkEntry(self.third_frame)

            entry.pack()

            entry.bind('<Return>', get_tags)

            button = customtkinter.CTkButton(self.third_frame, text="Extract tags", command=get_tags)
            button.pack(pady=20)

            copy_button = customtkinter.CTkButton(self.third_frame, text="Copy Tags", command=copy_tags)
            copy_button.pack(pady=10)

            output = customtkinter.CTkTextbox(self.third_frame, height=300, width=400, state='disabled')
            output.pack(pady=60, padx=60)



            App.mainloop()
        
        self.SEO_TITLE = customtkinter.CTkButton(self.third_frame, text=" Extract tags Tool ",command=youtube_get_tag)
        self.SEO_TITLE.pack(pady=20,padx=0.9)

    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Youtube":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "TikTok":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("Youtube")

    def frame_3_button_event(self):
        self.select_frame_by_name("TikTok")

        



    
    


    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
