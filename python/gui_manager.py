from tkinter import *
import gui_navigation
import gui_command
import gui_arguments
import gui_variables as vars
import tkinter.font as tkFont

class app:
    def __init__(self, root):
        self.gui = root
        self.gui.title('Steam Gatherer Tool')
        self.gui.iconphoto(False, PhotoImage(file='python\logo.png'))
        self.gui.geometry('{}x{}'.format(vars.window_width, vars.window_height))
        self.gui.resizable(width=False, height=False)

        self.font_frame_title = tkFont.Font(size=vars.main_frame_title_size)

    def start(self):
        self.navigation_frame = gui_navigation.navigation_frame(self.gui, self)
        self.command_frame = gui_command.command_frame(self.gui, self)
        self.arguments_frame = gui_arguments.arguments_frame(self.gui, self)

        self.gui.mainloop()

    def pass_argument_to_command(self, argument_list):
        self.command_frame.write_arguments_in_entry(argument_list)

    def display_frames(self,visibility_indexes):
        for i in range(len(visibility_indexes)):
            if visibility_indexes[i] == 1:
            #     globals()["self." + gui_navigation.navigation_button_list[i] + "_frame"].place_frame()
            # else:
            #     globals()["self." + gui_navigation.navigation_button_list[i] + "_frame"].hide_frame()
                print(globals())

if __name__ == '__main__':
    root = Tk()
    vars.gather_gui_variables()
    gatherer_gui = app(root)
    gatherer_gui.start()