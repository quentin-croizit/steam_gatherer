from tkinter import *

app = Tk()
app.title('Steam Gatherer Tool')
app.geometry('{}x{}'.format(500, 350))

# App Layout
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.minsize(200, 200)

# Frames
frame_left = Frame(app, bg='grey25')
frame_left.grid(column=0, row=0, rowspan=4, sticky="nsw")

frame_bottom = Frame(app, bg='grey50')
frame_bottom.grid(column=1, columnspan=2, row=1, rowspan=3, sticky="swe")
frame_bottom.columnconfigure(1, weight=1)

frame_arguments = Frame(app)
frame_presets = Frame(app)
frame_more = Frame(app)

# Variables
boolvar = BooleanVar(frame_bottom, False)

# Functions
def activateCheck():
    if boolvar.get() == 1:
        entry_command.config(state=NORMAL)
    elif boolvar.get() == 0:
        entry_command.config(state=DISABLED)

def showArgumentFrame():
    hideMiddleFrames()
    frame_arguments.grid(column=1, row=0, sticky="nwes")
 
def showPresetFrame():
    hideMiddleFrames()
    frame_presets.grid(column=1, row=0, sticky="nwes")
    
def showMoreFrame():
    hideMiddleFrames()
    frame_more.grid(column=1, row=0, sticky="nwes")

def hideMiddleFrames():
    frame_arguments.grid_forget()
    frame_presets.grid_forget()
    frame_more.grid_forget()


# Left Frame Widgets
button_arguments = Button(frame_left, text='Arguments',anchor="w", command=showArgumentFrame)
button_arguments.grid(row=0, sticky="ew", ipadx=5, ipady=5, padx=5, pady=(5,0))

button_preset = Button(frame_left, text='Presets',anchor="w", command=showPresetFrame)
button_preset.grid(row=1, sticky="ew", ipadx=5, ipady=5, padx=5, pady=(5,0))

button_more = Button(frame_left, text='More',anchor="w", command=showMoreFrame)
button_more.grid(row=2, sticky="ew", ipadx=5, ipady=5, padx=5, pady=(5,0))

# Bottom Frame Widgets
checkbox_custom_command= Checkbutton(frame_bottom, bg='grey50', activebackground="grey50", variable=boolvar, command=activateCheck)
checkbox_custom_command.grid(row=0, column=0, sticky="w", ipadx=5, ipady=5, padx=(5,0), pady=5)

entry_command= Entry(frame_bottom, disabledbackground="grey75")
entry_command.insert(-1, 'dotnet run --')
entry_command.grid(row=0, column=1, sticky="ew")
entry_command.configure(state="disabled")

button_gather = Button(frame_bottom, text='Gather',anchor="w")
button_gather.grid(row=0, column=2, sticky="e", pady=(1,0), padx=10)

# Arguments Frame Widgets
label_arg_id = Label(frame_arguments, text="ID", anchor="w")
label_arg_id.grid(row=0, column=0, sticky="ew")
entry_arg_id = Entry(frame_arguments)
entry_arg_id.grid(row=0, column=1, sticky="ew")

label_arg_filter = Label(frame_arguments, text="Filter", anchor="w")
label_arg_filter.grid(row=1, column=0, sticky="ew")
entry_arg_filter = Entry(frame_arguments)
entry_arg_filter.grid(row=1, column=1, sticky="ew")

label_arg_lang = Label(frame_arguments, text="Lang", anchor="w") 
label_arg_lang.grid(row=2, column=0, sticky="ew")
entry_arg_lang = Entry(frame_arguments)
entry_arg_lang.grid(row=2, column=1, sticky="ew")

label_arg_range = Label(frame_arguments, text="Range", anchor="w") 
label_arg_range.grid(row=3, column=0, sticky="ew")
entry_arg_range = Entry(frame_arguments)
entry_arg_range.grid(row=3, column=1, sticky="ew")

label_arg_type = Label(frame_arguments, text="Type", anchor="w") 
label_arg_type.grid(row=4, column=0, sticky="ew")
entry_arg_type = Entry(frame_arguments)
entry_arg_type.grid(row=4, column=1, sticky="ew")

label_arg_purchase = Label(frame_arguments, text="Purchase", anchor="w") 
label_arg_purchase.grid(row=5, column=0, sticky="ew")
entry_arg_purchase = Entry(frame_arguments)
entry_arg_purchase.grid(row=5, column=1, sticky="ew")

label_arg_number = Label(frame_arguments, text="Number", anchor="w") 
label_arg_number.grid(row=6, column=0, sticky="ew")
entry_arg_number = Entry(frame_arguments)
entry_arg_number.grid(row=6, column=1, sticky="ew")

# Setup
showArgumentFrame()
app.mainloop()