import re
import tkinter.font as tkFont

gui_variable_regex = '[\s\S]+[\s]=[\s][\s\S]+,'

def gather_gui_variables():
    config = open("gui_config", "r")
    config_lines = config.readlines()
    for i in range(len(config_lines)):
        config_lines[i] = config_lines[i].strip()

    for line in config_lines:
        if re.fullmatch(gui_variable_regex, line) != None:
            add_to_variable_list(line)

    calculate_derived_values()

def add_to_variable_list(line):
    var_name = re.search("[\s\S]+(?=\s=)", line).group()
    var_value = re.search("(?<==\s)[\s\S]+(?=,)", line).group()
    try:
        globals()[var_name] = int(var_value)
    except:
        globals()[var_name] = var_value

def calculate_derived_values():
    globals()["frame_title_height_nudger"] = tkFont.Font(size=main_frame_title_size).metrics("descent")
    globals()["frame_title_height"] = tkFont.Font(size=main_frame_title_size).metrics("linespace")
    globals()["window_width"] = main_frame_width + navigation_frame_width
    globals()["window_height"] = main_frame_height + command_frame_height
    globals()["navigation_button_width"] = navigation_frame_width - 2 * navigation_button_padding
    globals()["gather_button_x"] = main_frame_width - gather_button_width - command_frame_padding
    globals()["gather_button_height"] = command_frame_height - 2 * command_frame_padding
    globals()["custom_command_checkbox_height"] = command_frame_height - 2 * command_frame_padding
    globals()["command_entry_x_position"] = custom_command_checkbox_width+ 2 * command_frame_padding
    globals()["command_entry_width"] = main_frame_width - (4 * command_frame_padding) - custom_command_checkbox_width - gather_button_width
    globals()["command_entry_height"] = command_frame_height - 2 * command_frame_padding
    globals()["argument_value_x"] = argument_label_width + 2 * main_frame_padding
    globals()["argument_line_base_y"] = frame_title_height + (2 * main_frame_padding)