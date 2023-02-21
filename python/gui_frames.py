from tkinter import *
import gui_variables as vars

def create_app_frames(app_window):
    main_frame_width = int(vars.default_window_width) - int(vars.navigation_frame_width)
    command_frame_y = int(vars.default_window_height) - int(vars.command_frame_height)

    navigation_frame = Frame(app_window, bg=vars.navigation_frame_color)
    navigation_frame.place(x=0, y=0, width=vars.navigation_frame_width, height=vars.default_window_height)

    command_frame = Frame(app_window, bg=vars.command_frame_color)
    command_frame.place(x=vars.navigation_frame_width, y=command_frame_y, width=main_frame_width, height=vars.command_frame_height)

    arguments_frame = Frame(app_window, bg=vars.main_frame_color)
    arguments_frame.place(x=vars.navigation_frame_width, y=0, width=main_frame_width, height=command_frame_y)

    presets_frame = Frame(app_window, bg=vars.main_frame_color)
    presets_frame.place(x=vars.navigation_frame_width, y=0, width=main_frame_width, height=command_frame_y)

    more_frame = Frame(app_window, bg=vars.main_frame_color)
    more_frame.place(x=vars.navigation_frame_width, y=0, width=main_frame_width, height=command_frame_y)