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

# Variables
boolvar = BooleanVar(frame_bottom, False)

# Functions
def activateCheck():
            if boolvar.get() == 1:          #whenever checked
                entry_command.config(state=NORMAL)
            elif boolvar.get() == 0:        #whenever unchecked
                entry_command.config(state=DISABLED)

# Left Frame Widgets
button_arguments = Button(frame_left, text='Arguments',anchor="w")
button_arguments.grid(row=0, sticky="ew", ipadx=5, ipady=5, padx=5, pady=(5,0))

button_preset = Button(frame_left, text='Presets',anchor="w")
button_preset.grid(row=1, sticky="ew", ipadx=5, ipady=5, padx=5, pady=(5,0))

button_more = Button(frame_left, text='More',anchor="w")
button_more.grid(row=2, sticky="ew", ipadx=5, ipady=5, padx=5, pady=(5,0))

# Bottom Frame Widgets
checkbox_custom_command= Checkbutton(frame_bottom, bg='grey50', activebackground="grey50", variable=boolvar, command=activateCheck)
checkbox_custom_command.grid(row=0, column=0, sticky="w", ipadx=5, ipady=5, padx=(5,0), pady=5)

entry_command= Entry(frame_bottom, state="disabled", textvariable="Text set by button", disabledbackground="grey75")
entry_command.grid(row=0, column=1, sticky="ew")

button_gather = Button(frame_bottom, text='Gather',anchor="w")
button_gather.grid(row=0, column=2, sticky="e", pady=(1,0), padx=10)

# Setup
app.mainloop()