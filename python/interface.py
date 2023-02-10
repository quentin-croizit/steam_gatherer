from tkinter import *
from PIL import ImageTk, Image
import math

app = Tk()
app.title('Steam Gatherer Tool')
app.geometry('{}x{}'.format(700, 400))

# App Layout
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.minsize(375, 325)

# Frames
frame_left = Frame(app, bg='grey25')
frame_left.grid(column=0, row=0, rowspan=4, sticky="nsw")

frame_bottom = Frame(app, bg='grey50')
frame_bottom.grid(column=1, columnspan=2, row=1, rowspan=3, sticky="swe")
frame_bottom.columnconfigure(1, weight=1)

frame_arguments = Frame(app)
frame_presets = Frame(app)
frame_more = Frame(app)

# Functions
def activateCheck():
    if custom_command_inputable.get() == 1:
        entry_command.config(state=NORMAL)
    elif custom_command_inputable.get() == 0:
        entry_command.config(state=DISABLED)

def showArgumentFrame():
    hideMiddleFrames()
    frame_arguments.grid(column=1, row=0, sticky="nwes")
    button_arguments.configure(state="disabled")
 
def showPresetFrame():
    hideMiddleFrames()
    frame_presets.grid(column=1, row=0, sticky="nwes")
    button_preset.configure(state="disabled")
    
def showMoreFrame():
    hideMiddleFrames()
    frame_more.grid(column=1, row=0, sticky="nwes")
    button_more.configure(state="disabled")

def hideMiddleFrames():
    frame_arguments.grid_forget()
    frame_presets.grid_forget()
    frame_more.grid_forget()
    button_arguments.configure(state="normal")
    button_preset.configure(state="normal")
    button_more.configure(state="normal")

def write_in_entry_command(var, index, mode):
    command = "dotnet run -- "
    command += (" {}".format(arg_variable_id.get()))
    command += (" {}".format(arg_variable_filter.get()))
    command += (" {}".format(arg_variable_lang.get()))
    command += (" {}".format(arg_variable_range.get()))
    command += (" {}".format(arg_variable_type.get()))
    command += (" {}".format(arg_variable_purchase.get()))
    command += (" {}".format(arg_variable_number.get()))
    entry_command.configure(state="normal")
    entry_command.delete(0, END)
    entry_command.insert(0, command)
    entry_command.configure(state="disabled")

# Variables
custom_command_inputable = BooleanVar(frame_bottom, False)
image_info_icon = ImageTk.PhotoImage(Image.open("python/info_icon.png"))

arg_variable_id = StringVar(app)
arg_variable_id.set("0")
arg_variable_id.trace_add("write", write_in_entry_command)

list_filter = ["all","recent","updated"]
arg_variable_filter = StringVar(app)
arg_variable_filter.set(list_filter[0])
arg_variable_filter.trace_add("write", write_in_entry_command)

list_lang = ["all","arabic","bulgarian","schinese","tchinese","czech","danish","dutch","english","finnish","french","german","greek","hungarian","italian","japanese","koreana","norwegian","polish","portuguese","brazilian","romanian","russian","spanish","latam","swedish","thai","turkish","ukrainian","vietnamese"]
arg_variable_lang = StringVar(app)
arg_variable_lang.set(list_lang[0])
arg_variable_lang.trace_add("write", write_in_entry_command)

arg_variable_range = StringVar(app)
arg_variable_range.set("365")
arg_variable_range.trace_add("write", write_in_entry_command)

list_type = ["all","positive","negative"]
arg_variable_type = StringVar(app)
arg_variable_type.set(list_type[0])
arg_variable_type.trace_add("write", write_in_entry_command)

list_purchase = ["all","non_steam_purchase","steam"]
arg_variable_purchase = StringVar(app)
arg_variable_purchase.set(list_purchase[0])
arg_variable_purchase.trace_add("write", write_in_entry_command)

arg_variable_number = StringVar(app)
arg_variable_number.set("50")
arg_variable_number.trace_add("write", write_in_entry_command)

# Left Frame Widgets
button_arguments = Button(frame_left, text='Arguments',anchor="w", command=showArgumentFrame)
button_arguments.grid(row=0, sticky="ew", ipadx=5, ipady=5, padx=5, pady=(5,0))

button_preset = Button(frame_left, text='Presets',anchor="w", command=showPresetFrame)
button_preset.grid(row=1, sticky="ew", ipadx=5, ipady=5, padx=5, pady=(5,0))

button_more = Button(frame_left, text='More',anchor="w", command=showMoreFrame)
button_more.grid(row=2, sticky="ew", ipadx=5, ipady=5, padx=5, pady=(5,0))

# Bottom Frame Widgets
checkbox_custom_command= Checkbutton(frame_bottom, bg='grey50', activebackground="grey50", variable=custom_command_inputable, command=activateCheck)
checkbox_custom_command.grid(row=0, column=0, sticky="w", ipadx=5, ipady=5, padx=(5,0), pady=5)

entry_command= Entry(frame_bottom, disabledbackground="grey75")
entry_command.insert(-1, 'dotnet run --')
entry_command.grid(row=0, column=1, sticky="ew")
entry_command.configure(state="disabled")

button_gather = Button(frame_bottom, text='Gather',anchor="w")
button_gather.grid(row=0, column=2, sticky="e", pady=(1,0), padx=10)

# Arguments Frame Widgets
label_argument = Label(frame_arguments, text="Arguments", anchor="w", font=("Arial", 20))
label_argument.place(x=10, y=10)

label_arg_id = Label(frame_arguments, text="ID", anchor="w")
label_arg_id.place(x=10, y=60, width=60, height=20)
entry_arg_id = Entry(frame_arguments, textvariable=arg_variable_id)
entry_arg_id.place(x=80, y=60, width=150, height=20)

label_arg_filter = Label(frame_arguments, text="Filter", anchor="w")
label_arg_filter.place(x=10, y=90, width=60, height=20)
entry_arg_filter = OptionMenu(frame_arguments, arg_variable_filter, *list_filter)
entry_arg_filter.place(x=77, y=87, width=155, height=25)

label_arg_lang = Label(frame_arguments, text="Lang", anchor="w") 
label_arg_lang.place(x=10, y=120, width=60, height=20)
entry_arg_filter = OptionMenu(frame_arguments, arg_variable_lang, *list_lang)
entry_arg_filter.place(x=77, y=117, width=155, height=25)

label_arg_range = Label(frame_arguments, text="Range", anchor="w") 
label_arg_range.place(x=10, y=150, width=60, height=20)
entry_arg_range = Entry(frame_arguments, textvariable=arg_variable_range)
entry_arg_range.place(x=80, y=150, width=150, height=20)

label_arg_type = Label(frame_arguments, text="Type", anchor="w") 
label_arg_type.place(x=10, y=180, width=60, height=20)
entry_arg_type = OptionMenu(frame_arguments, arg_variable_type, *list_type)
entry_arg_type.place(x=77, y=177, width=155, height=25)

label_arg_purchase = Label(frame_arguments, text="Purchase", anchor="w") 
label_arg_purchase.place(x=10, y=210, width=60, height=20)
entry_arg_purchase = OptionMenu(frame_arguments, arg_variable_purchase, *list_purchase)
entry_arg_purchase.place(x=77, y=207, width=155, height=25)

label_arg_number = Label(frame_arguments, text="Number", anchor="w") 
label_arg_number.place(x=10, y=240, width=60, height=20)
entry_arg_number = Entry(frame_arguments, textvariable=arg_variable_number)
entry_arg_number.place(x=80, y=240, width=150, height=20)

# Presets Frame Widgets
label_presets = Label(frame_presets, text="Presets", anchor="w", font=("Arial", 20))
label_presets.place(x=10, y=10)

# More Frame Widgets
label_more = Label(frame_more, text="More", anchor="w", font=("Arial", 20))
label_more.place(x=10, y=10)

# Setup
showArgumentFrame()
write_in_entry_command(0, 0, 0)

app.mainloop()