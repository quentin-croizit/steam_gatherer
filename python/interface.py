# ---------------------------------------------------------------------------- #
# Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) #
# ---------------------------------------------------------------------------- #

from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image
import os
import re
from functools import partial
import presets
import gui_variables as vars
import gui_frames as frames

vars.gather_gui_variables()

app = Tk()
app.title('Steam Gatherer Tool')
app.iconphoto(False, PhotoImage(file='python\logo.png'))
app.geometry('{}x{}'.format(vars.default_window_width, vars.default_window_height))
app.resizable(width=False, height=False)

# Frames
frames.create_app_frames(app)
print(frames.main_frame_width)

# Functions
# def activateCheck():
#     if custom_command_inputable.get() == 1:
#         entry_command.config(state=NORMAL)
#     elif custom_command_inputable.get() == 0:
#         entry_command.config(state=DISABLED)

# def showArgumentFrame():
#     hideMiddleFrames()
#     frames.arguments_frame.grid(column=1, row=0, sticky="nwes")
#     button_arguments.configure(state="disabled")
 
# def showPresetFrame():
#     hideMiddleFrames()
#     frames.presets_frame.grid(column=1, row=0, sticky="nwes")
#     button_preset.configure(state="disabled")
    
# def showMoreFrame():
#     hideMiddleFrames()
#     frames.more_frame.grid(column=1, row=0, sticky="nwes")
#     button_more.configure(state="disabled")

# def hideMiddleFrames():
#     frames.arguments_frame.grid_forget()
#     frames.presets_frame.grid_forget()
#     frames.more_frame.grid_forget()
#     button_arguments.configure(state="normal")
#     button_preset.configure(state="normal")
#     button_more.configure(state="normal")

# def write_in_entry_command(var, index, mode):
#     arg_variable_id.set(re.sub("[^0-9]", "", arg_variable_id.get()))
#     arg_variable_range.set(re.sub("[^0-9]", "", arg_variable_range.get()))
#     arg_variable_number.set(re.sub("[^0-9]", "", arg_variable_number.get()))
#     if(arg_variable_id.get() == ""):
#         arg_variable_id.set("0")
#     if(arg_variable_range.get() == ""):
#         arg_variable_range.set("1")
#     if(int(arg_variable_range.get()) < 1):
#         arg_variable_range.set("1")
#     if(int(arg_variable_range.get()) > 365):
#         arg_variable_range.set("365")
#     if(arg_variable_number.get() == ""):
#         arg_variable_number.set("1")
#     if(int(arg_variable_number.get()) < 1):
#         arg_variable_number.set("1")
#     command = "dotnet run -- "
#     command += (" {}".format(arg_variable_id.get()))
#     command += (" {}".format(arg_variable_filter.get()))
#     command += (" {}".format(arg_variable_lang.get()))
#     command += (" {}".format(arg_variable_range.get()))
#     command += (" {}".format(arg_variable_type.get()))
#     command += (" {}".format(arg_variable_purchase.get()))
#     command += (" {}".format(arg_variable_number.get()))
#     entry_command.configure(state="normal")
#     entry_command.delete(0, END)
#     entry_command.insert(0, command)
#     entry_command.configure(state="disabled")

# def start_gather_command():
#     print(entry_command.get())
#     os.system(entry_command.get())

# def apply_preset(preset_values):
#     arg_variable_id.set(preset_values[0])
#     arg_variable_filter.set(preset_values[1])
#     arg_variable_lang.set(preset_values[2])
#     arg_variable_range.set(preset_values[3])
#     arg_variable_type.set(preset_values[4])
#     arg_variable_purchase.set(preset_values[5])
#     arg_variable_number.set(preset_values[6])
#     showArgumentFrame()

# # Fonts
# font_frame_title = tkFont.Font(size=20)
# font_preset_arg = tkFont.Font(size=7)
# font_preset_test = tkFont.Font(size=20)

# # Variables
# presets.gatherPreset()
# list_presets = presets.presets

# # custom_command_inputable = BooleanVar(frames.command_frame, False)

# arg_variable_id = StringVar(app)
# arg_variable_id.set("0")
# arg_variable_id.trace_add("write", write_in_entry_command)

# list_filter = ["all","recent","updated"]
# arg_variable_filter = StringVar(app)
# arg_variable_filter.set(list_filter[0])
# arg_variable_filter.trace_add("write", write_in_entry_command)

# list_lang = ["all","arabic","bulgarian","schinese","tchinese","czech","danish","dutch","english","finnish","french","german","greek","hungarian","italian","japanese","koreana","norwegian","polish","portuguese","brazilian","romanian","russian","spanish","latam","swedish","thai","turkish","ukrainian","vietnamese"]
# arg_variable_lang = StringVar(app)
# arg_variable_lang.set(list_lang[0])
# arg_variable_lang.trace_add("write", write_in_entry_command)

# arg_variable_range = StringVar(app)
# arg_variable_range.set("365")
# arg_variable_range.trace_add("write", write_in_entry_command)

# list_type = ["all","positive","negative"]
# arg_variable_type = StringVar(app)
# arg_variable_type.set(list_type[0])
# arg_variable_type.trace_add("write", write_in_entry_command)

# list_purchase = ["all","non_steam_purchase","steam"]
# arg_variable_purchase = StringVar(app)
# arg_variable_purchase.set(list_purchase[0])
# arg_variable_purchase.trace_add("write", write_in_entry_command)

# arg_variable_number = StringVar(app)
# arg_variable_number.set("50")
# arg_variable_number.trace_add("write", write_in_entry_command)

# Left Frame Widgets
# button_arguments = Button(frames.navigation_frame, text='Arguments',anchor="w", command=showArgumentFrame)
# button_arguments.grid(row=0, sticky="ew", ipadx=5, ipady=5, padx=5, pady=(5,0))

# button_preset = Button(frames.navigation_frame, text='Presets',anchor="w", command=showPresetFrame)
# button_preset.grid(row=1, sticky="ew", ipadx=5, ipady=5, padx=5, pady=(5,0))

# button_more = Button(frames.navigation_frame, text='More',anchor="w", command=showMoreFrame)
# button_more.grid(row=2, sticky="ew", ipadx=5, ipady=5, padx=5, pady=(5,0))

# # Bottom Frame Widgets
# checkbox_custom_command= Checkbutton(frames.command_frame, bg='grey50', activebackground="grey50", variable=custom_command_inputable, command=activateCheck)
# checkbox_custom_command.grid(row=0, column=0, sticky="w", ipadx=5, ipady=5, padx=(5,0), pady=5)

# entry_command= Entry(frames.command_frame, disabledbackground="grey75")
# entry_command.insert(-1, 'dotnet run --')
# entry_command.grid(row=0, column=1, sticky="ew")
# entry_command.configure(state="disabled")

# button_gather = Button(frames.command_frame, text='Gather',anchor="w", command=start_gather_command)
# button_gather.grid(row=0, column=2, sticky="e", pady=(1,0), padx=10)

# Arguments Frame Widgets
# label_argument = Label(frames.arguments_frame, text="Arguments", anchor="w", font=font_frame_title)
# label_argument.place(x=10, y=10)

# label_arg_id = Label(frames.arguments_frame, text="ID", anchor="w")
# label_arg_id.place(x=10, y=60, width=60, height=20)
# entry_arg_id = Entry(frames.arguments_frame, textvariable=arg_variable_id)
# entry_arg_id.place(x=80, y=60, width=150, height=20)

# label_arg_filter = Label(frames.arguments_frame, text="Filter", anchor="w")
# label_arg_filter.place(x=10, y=90, width=60, height=20)
# entry_arg_filter = OptionMenu(frames.arguments_frame, arg_variable_filter, *list_filter)
# entry_arg_filter.place(x=77, y=87, width=155, height=25)

# label_arg_lang = Label(frames.arguments_frame, text="Lang", anchor="w") 
# label_arg_lang.place(x=10, y=120, width=60, height=20)
# entry_arg_filter = OptionMenu(frames.arguments_frame, arg_variable_lang, *list_lang)
# entry_arg_filter.place(x=77, y=117, width=155, height=25)

# label_arg_range = Label(frames.arguments_frame, text="Range", anchor="w") 
# label_arg_range.place(x=10, y=150, width=60, height=20)
# entry_arg_range = Entry(frames.arguments_frame, textvariable=arg_variable_range)
# entry_arg_range.place(x=80, y=150, width=150, height=20)

# label_arg_type = Label(frames.arguments_frame, text="Type", anchor="w") 
# label_arg_type.place(x=10, y=180, width=60, height=20)
# entry_arg_type = OptionMenu(frames.arguments_frame, arg_variable_type, *list_type)
# entry_arg_type.place(x=77, y=177, width=155, height=25)

# label_arg_purchase = Label(frames.arguments_frame, text="Purchase", anchor="w") 
# label_arg_purchase.place(x=10, y=210, width=60, height=20)
# entry_arg_purchase = OptionMenu(frames.arguments_frame, arg_variable_purchase, *list_purchase)
# entry_arg_purchase.place(x=77, y=207, width=155, height=25)

# label_arg_number = Label(frames.arguments_frame, text="Number", anchor="w") 
# label_arg_number.place(x=10, y=240, width=60, height=20)
# entry_arg_number = Entry(frames.arguments_frame, textvariable=arg_variable_number)
# entry_arg_number.place(x=80, y=240, width=150, height=20)

# # Presets Frame Widgets
# label_presets = Label(frames.presets_frame, text="Presets", anchor="w", font=font_frame_title)
# label_presets.place(x=10, y=10)

# for i in range(len(list_presets)):
#     Button(frames.presets_frame, text=list_presets[i][0], command=partial(apply_preset,list_presets[i][1])).place(x=10, y=60+(60*i), width=80, height=40)
#     Label(frames.presets_frame, text=presets.preset_argument_format(list_presets[i][1]), anchor="w", font=font_preset_arg).place(x=100, y=82+(60*i), width=500, height=20)
#     Label(frames.presets_frame, text=list_presets[i][1][7], anchor="w").place(x=100, y=61+(60*i), width=500, height=20)

# # More Frame Widgets
# label_more = Label(frames.more_frame, text="More", anchor="w", font=font_frame_title)
# label_more.place(x=10, y=10)

# Setup
# showArgumentFrame()
# write_in_entry_command(0, 0, 0)

app.mainloop()