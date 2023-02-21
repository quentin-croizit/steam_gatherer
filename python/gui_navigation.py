from tkinter import *
import gui_variables as vars
from functools import partial

navigation_button_list = ["arguments","presets","more"]
navigation_visibility_list = [1,0,0]

class navigation_frame:
    def __init__(self, gui, app):
        self.gui = gui
        self.app_root = app
        self.navigation_frame = Frame(self.gui, bg=vars.navigation_frame_color)
        self.navigation_frame.place(x=0, y=0, width=vars.navigation_frame_width, height=vars.window_height)

        for i in range(len(navigation_button_list)):
            Button(self.navigation_frame, text=navigation_button_list[i].capitalize(), anchor="w", command=partial(self.show_frame,i), relief=vars.button_style).place(x=vars.navigation_button_padding, y=calculate_button_y_position(i), width=vars.navigation_button_width, height=vars.navigation_button_height)

    def button_pressed(self,text):
        print("pressed {}".format(text))

    def show_frame(self,index):
        navigation_visibility_list.remove(1)
        navigation_visibility_list.append(0)
        navigation_visibility_list[index] = 1
        self.app_root.display_frames(navigation_visibility_list)


def calculate_button_y_position(index):
    return (int(vars.navigation_button_padding) * (index + 1)) + (int(vars.navigation_button_height) * index)