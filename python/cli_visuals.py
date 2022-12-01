import os

bar_top = "╔════════════════════════════════════════════════════════════════════════╗"
bar_separator = "╠════════════════════════════════════════════════════════════════════════╣"
bar_bottom = "╚════════════════════════════════════════════════════════════════════════╝"
bar_empty = "║                                                                        ║"

app_title_01 = "║    _____ _                          _____            _                 ║"
app_title_02 = "║   / ____| |                        |  __ \          (_)                ║"
app_title_03 = "║  | (___ | |_ ___  __ _ _ __ ___    | |__) |_____   ___  _____      __  ║"
app_title_04 = "║   \___ \| __/ _ \/ _` | '_ ` _ \   |  _  // _ \ \ / / |/ _ \ \ /\ / /  ║"
app_title_05 = "║   ____) | ||  __/ (_| | | | | | |  | | \ \  __/\ V /| |  __/\ V  V /   ║"
app_title_06 = "║  |_____/ \__\___|\__,_|_| |_| |_|  |_|  \_\___| \_/ |_|\___| \_/\_/    ║"
app_title_07 = "║    _____       _   _                              _______          _   ║"
app_title_08 = "║  / ____|     | | | |                             |__   __|        | |  ║"
app_title_09 = "║ | |  __  __ _| |_| |__   ___ _ __ ___ _ __          | | ___   ___ | |  ║"
app_title_10 = "║ | | |_ |/ _` | __| '_ \ / _ \ '__/ _ \ '__|         | |/ _ \ / _ \| |  ║"
app_title_11 = "║ | |__| | (_| | |_| | | |  __/ | |  __/ |            | | (_) | (_) | |  ║"
app_title_12 = "║  \_____|\__,_|\__|_| |_|\___|_|  \___|_|            |_|\___/ \___/|_|  ║"

arguments = "║ Current Arguments:                                                     ║"
commands = "║ Additional Commands:                                                   ║"
commands_gather = "║ Gather: Start gathering process                                        ║"
commands_reset = "║ Reset: Resets the arguments already entered                            ║"
commands_back = "║ Back: If entering an argument value, goes back to argument selection   ║"
commands_exit = "║ Exit: Stops process                                                    ║"

app_title_all = [app_title_01,
                 app_title_02,
                 app_title_03,
                 app_title_04,
                 app_title_05,
                 app_title_06,
                 app_title_07,
                 app_title_08,
                 app_title_09,
                 app_title_10,
                 app_title_11,
                 app_title_12]

arguments_types = ["preset", "id", "filter", "lang",
                   "range", "type", "purchase", "number"]


def calculateSpace(type, arg):
    space_width = len(
        "════════════════════════════════════════════════════════════════════════") - len(" " + type + " = " + arg + " ")
    space_str = ""
    for i in range(space_width):
        space_str += " "
    return space_str


def printAppTitle():
    for app_title in app_title_all:
        print(app_title)
    print(bar_empty)


def printArguments(arguments_entered):
    for i in range(0, 8):
        print("║ {} = {} {}║".format(arguments_types[i], arguments_entered[i],
                                     calculateSpace(arguments_types[i], arguments_entered[i])))


def printCommands():
    print(commands)
    print(bar_separator)
    print(commands_gather)
    print(commands_back)
    print(commands_reset)
    print(commands_exit)


def printAppBox(arguments_entered):
    clearConsole()
    print(bar_top)
    printAppTitle()
    print(bar_separator)
    print(arguments)
    print(bar_separator)
    printArguments(arguments_entered)
    print(bar_separator)
    printCommands()
    print(bar_bottom)
    print("")


def clearConsole():
    os.system('clear')
    os.system('cls')
