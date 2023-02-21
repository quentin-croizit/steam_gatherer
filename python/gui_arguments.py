from tkinter import *
import gui_variables as vars
import re
from functools import partial

arguments_list_types = [("id","entry","0","9999999"),("filter","dropdown"),("lang","dropdown"), ("range","entry","1","365"), ("type","dropdown"), ("purchase","dropdown"), ("number","entry","1","9999999")]
list_filter = ["all","recent","updated"]
list_lang = ["all","arabic","bulgarian","schinese","tchinese","czech","danish","dutch","english","finnish","french","german","greek","hungarian","italian","japanese","koreana","norwegian","polish","portuguese","brazilian","romanian","russian","spanish","latam","swedish","thai","turkish","ukrainian","vietnamese"]
list_type = ["all","positive","negative"]
list_purchase = ["all","non_steam_purchase","steam"]

class arguments_frame:
    def __init__(self, gui, app):
        self.gui = gui
        self.app_root = app
        self.arguments_frame = Frame(self.gui, bg=vars.main_frame_color)
        self.place_frame()

        self.label_argument = Label(self.arguments_frame, text="Arguments", anchor="w", font=self.app_root.font_frame_title)
        self.label_argument.place(x=vars.main_frame_padding, y=vars.main_frame_padding - vars.frame_title_height_nudger)

        self.argument_pass_list = []

        for i in range(len(arguments_list_types)):
            self.var_name = "arg_variable_" + arguments_list_types[i][0]
            self.var_list = "list_" + arguments_list_types[i][0]

            globals()[self.var_name] = StringVar(self.arguments_frame, name=self.var_name)
            self.argument_y_position = vars.argument_line_base_y + i * (vars.argument_height + vars.argument_spacing)

            Label(self.arguments_frame, text=arguments_list_types[i][0].capitalize(), anchor="w").place(x=vars.main_frame_padding, y=self.argument_y_position, width=vars.argument_label_width, height=vars.argument_height)
            if arguments_list_types[i][1] == "entry":
                globals()[self.var_name].set(arguments_list_types[i][2])
                globals()[self.var_name].trace_add("write", partial(self.check_entry_value,self.var_name,i))
                Entry(self.arguments_frame, textvariable=globals()[self.var_name]).place(x=vars.argument_value_x, y=self.argument_y_position, width=vars.argument_value_width, height=vars.argument_height)
            if arguments_list_types[i][1] == "dropdown":   
                globals()[self.var_name].set(globals()[self.var_list][0])
                globals()[self.var_name].trace_add("write", partial(self.send_arguments_to_command))
                OptionMenu(self.arguments_frame, globals()[self.var_name], *globals()[self.var_list]).place(x=vars.argument_value_x-3, y=self.argument_y_position - 3, width=vars.argument_value_width + 5, height=vars.argument_height + 5)
            
        self.send_arguments_to_command("","","")

    def place_frame(self):
        self.arguments_frame.place(x=vars.navigation_frame_width, y=0, width=vars.main_frame_width, height=vars.main_frame_height)

    def hide_Frame(self):
        self.arguments_frame.place_forget()

    def check_entry_value(self, var_type, arg_index, var, index, mode):
        self.min_value = int(arguments_list_types[arg_index][2])
        self.max_value = int(arguments_list_types[arg_index][3])

        globals()[var_type].set(re.sub("[^0-9]", "", globals()[var_type].get()))
        if(globals()[var_type].get() == ""):
            globals()[var_type].set(self.min_value)
        if(int(globals()[var_type].get()) < self.min_value):
            globals()[var_type].set(self.min_value)
        if(int(globals()[var_type].get()) > self.max_value):
            globals()[var_type].set(self.max_value)

        self.send_arguments_to_command("","","")
        
    def send_arguments_to_command(self, var, index, mode):
        self.argument_pass_list.clear()
        for i in range(len(arguments_list_types)):
            self.argument_pass_list.append(globals()["arg_variable_" + arguments_list_types[i][0]].get())
        self.app_root.pass_argument_to_command(self.argument_pass_list)