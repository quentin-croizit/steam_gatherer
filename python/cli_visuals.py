# ---------------------------------------------------------------------------- #
# Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) #
# ---------------------------------------------------------------------------- #

import os

cli_textlines = open("python/visuals", "r", encoding='utf-8')
cli_textlines_list = cli_textlines.readlines()

for i in range(len(cli_textlines_list)):
    cli_textlines_list[i] = cli_textlines_list[i].strip('\n')

app_title = []
app_title_lines_number = 15
for i in range(app_title_lines_number):
    app_title.append(cli_textlines_list[i])

arguments = [cli_textlines_list[16], cli_textlines_list[17]]

app_commands = []
app_commands_lines_number = 9
for i in range(app_commands_lines_number):
    app_commands.append(cli_textlines_list[19+i])

app_help = []
app_help_lines_number = 9
for i in range(app_help_lines_number):
    app_help.append(cli_textlines_list[29+i])

app_endline = cli_textlines_list[39]

argument_detail_width = len(app_title[0]) - 4
arguments_types = ["id", "filter", "lang", "range", "type", "purchase", "number"]

current_page = "arguments"


def calculateSpace(type, arg):
    argument_detail_width
    space_width = argument_detail_width - len(type + " = " + arg)
    space_str = ""
    for i in range(space_width):
        space_str += " "
    return space_str


def printAppTitle():
    for app_title_line in app_title:
        print(app_title_line)


def printArguments(arguments_entered):
    print(arguments[0])
    print(arguments[1])
    for i in range(len(arguments_types)):
        arg_type = arguments_types[i]
        arg_value = arguments_entered[i]
        arg_space = calculateSpace(arguments_types[i], arguments_entered[i])
        arg_format = arg_type + " = " + arg_value + arg_space
        print("║ {} ║".format(arg_format))


def printHelp():
    for i in range(len(app_help)):
        print(app_help[i])


def printCommands():
    for i in range(len(app_commands)):
        print(app_commands[i])


def printAppBox(arguments_entered):
    clearConsole()
    printAppTitle()
    if current_page == "arguments":
        printArguments(arguments_entered)
    elif current_page == "help":
        printHelp()
    elif current_page == "commands":
        printCommands()
    print(app_endline)
    print("")


def clearConsole():
    os.system('clear')
    os.system('cls')
