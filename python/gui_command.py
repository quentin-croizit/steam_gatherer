from tkinter import *
import gui_variables as vars
import os

class command_frame:
    def __init__(self, gui, app):
        self.gui = gui
        self.app_root = app
        self.command_frame = Frame(self.gui, bg=vars.command_frame_color)
        self.command_frame.place(x=vars.navigation_frame_width, y=vars.main_frame_height, width=vars.main_frame_width, height=vars.command_frame_height)
        
        self.command_base_text = "dotnet run --"
        self.command_text = self.command_base_text
        self.custom_command_inputable = BooleanVar(self.command_frame, False)

        self.custom_command_checkbox= Checkbutton(self.command_frame, variable=self.custom_command_inputable, command=self.custom_command_switcher, relief=FLAT, background=vars.command_frame_color, activebackground=vars.command_frame_color)
        self.custom_command_checkbox.place(x=vars.command_frame_padding + 3, y=vars.command_frame_padding + 1, width=vars.custom_command_checkbox_width, height=vars.custom_command_checkbox_height)

        self.command_entry= Entry(self.command_frame, relief=vars.button_style)
        self.command_entry.insert(-1, self.command_text)
        self.command_entry.place(x=vars.command_entry_x_position, y=vars.command_frame_padding, width=vars.command_entry_width, height=vars.command_entry_height)
        self.command_entry.configure(state="disabled")

        self.gather_button = Button(self.command_frame, text='Gather',anchor="w", command=lambda : start_gather_command(self.command_entry.get()), relief=vars.button_style)
        self.gather_button.place(x=vars.gather_button_x, y=vars.command_frame_padding, width=vars.gather_button_width, height=vars.gather_button_height)


    def custom_command_switcher(self):
      if self.custom_command_inputable.get() == 1:
          self.command_entry.config(state=NORMAL)
      elif self.custom_command_inputable.get() == 0:
          self.command_entry.config(state=DISABLED)

    def write_arguments_in_entry(self, arg_list):

        self.command_text = self.command_base_text

        for i in range(len(arg_list)):
            self.command_text += (" {}".format(arg_list[i]))

        self.command_entry.configure(state="normal")
        self.command_entry.delete(0, END)
        self.command_entry.insert(0, self.command_text)
        self.command_entry.configure(state="disabled")

def start_gather_command(command):
    print(command)
    os.system(command)