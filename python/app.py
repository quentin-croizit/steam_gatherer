import os
import re

list_arguments_types = ["preset", "id", "filter", "lang",
                        "range", "type", "purchase", "number"]
list_arguments = ["", "", "", "", "", "", "", ""]
command = ""


os.system('clear')
os.system('cls')


def CalculateSpace(type, arg):
    space_width = len(
        "════════════════════════════════════════════════════════════════════════") - len(" " + type + " = " + arg + " ")
    space_str = ""
    for i in range(space_width):
        space_str += " "
    return space_str


def Welcome(type=""):
    arguments_entered = 0
    global list_arguments_types
    global list_arguments

    for arg in list_arguments:
        if arg != "":
            arguments_entered += 1

    if type == "gather":
        arguments_entered = 0

    os.system('clear')
    os.system('cls')

    print("╔════════════════════════════════════════════════════════════════════════╗")
    print("║    _____ _                          _____            _                 ║")
    print("║   / ____| |                        |  __ \          (_)                ║")
    print("║  | (___ | |_ ___  __ _ _ __ ___    | |__) |_____   ___  _____      __  ║")
    print("║   \___ \| __/ _ \/ _` | '_ ` _ \   |  _  // _ \ \ / / |/ _ \ \ /\ / /  ║")
    print("║   ____) | ||  __/ (_| | | | | | |  | | \ \  __/\ V /| |  __/\ V  V /   ║")
    print("║  |_____/ \__\___|\__,_|_| |_| |_|  |_|  \_\___| \_/ |_|\___| \_/\_/    ║")
    print("║    _____       _   _                              _______          _   ║")
    print("║  / ____|     | | | |                             |__   __|        | |  ║")
    print("║ | |  __  __ _| |_| |__   ___ _ __ ___ _ __          | | ___   ___ | |  ║")
    print("║ | | |_ |/ _` | __| '_ \ / _ \ '__/ _ \ '__|         | |/ _ \ / _ \| |  ║")
    print(
        "║ | |__| | (_| | |_| | | |  __/ | |  __/ |            | | (_) | (_) | |  ║")
    print("║  \_____|\__,_|\__|_| |_|\___|_|  \___|_|            |_|\___/ \___/|_|  ║")
    print("║                                                                        ║")
    print("╠════════════════════════════════════════════════════════════════════════╣")
    print("║ Current Arguments:                                                     ║")
    print("╠════════════════════════════════════════════════════════════════════════╣")
    for i in range(0, 8):
        print("║ {} = {} {}║".format(
            list_arguments_types[i], list_arguments[i], CalculateSpace(list_arguments_types[i], list_arguments[i])))
    print("╠════════════════════════════════════════════════════════════════════════╣")
    print("║ Additional Commands:                                                   ║")
    print("╠════════════════════════════════════════════════════════════════════════╣")
    print("║ Gather: Start gathering process                                        ║")
    print("║ Reset: Resets the arguments already entered                            ║")
    print("║ Back: If entering an argument value, goes back to argument selection   ║")
    print("║ Exit: Stops process                                                    ║")
    print("╚════════════════════════════════════════════════════════════════════════╝")

    if type == "preset":
        ChangePreset()
    elif type == "id":
        ChangeID()
    elif type == "filter":
        ChangeFilter()
    elif type == "lang":
        ChangeLang()
    elif type == "range":
        ChangeRange()
    elif type == "type":
        ChangeType()
    elif type == "purchase":
        ChangePurchase()
    elif type == "number":
        ChangeNumber()
    elif type == "gather":
        GatherDisplay()

    AddArgument()


def AddArgument(type=""):
    global arguments_entered
    global list_arguments_types
    global list_arguments

    if type == "":
        print("")
        print("What argument would like to modify?")
        arg_selected = input()
    else:
        arg_selected = type

    if arg_selected == "reset":
        list_arguments = ["", "", "", "", "", "", "", ""]
        Welcome()
    elif arg_selected == "exit":
        os._exit(0)
    elif arg_selected == "gather":
        CallDotnetCommand()
    elif arg_selected in list_arguments_types:
        Welcome(arg_selected)
    Welcome()


def ChangePreset():
    print("")
    print("What Preset would like to use?")
    preset = input()
    if preset != "back":
        list_arguments[0] = preset
    Welcome()


def ChangeID():
    print("")
    print("What GameID would like to use?")
    id = input()
    if id != "back":
        if re.fullmatch("[0-9]+", id) == None:
            Welcome("id")
        list_arguments[1] = id
    Welcome()


def ChangeFilter():
    print("")
    print("What Filter would like to use? (all, recent, updated)")
    filter = input()
    if filter != "back":
        if re.fullmatch("(all|recent|updated)", filter) == None:
            Welcome("filter")
        list_arguments[2] = filter
    Welcome()


def ChangeLang():
    print("")
    print("What Language would like to use?")
    lang = input()
    if lang != "back":
        if re.fullmatch("[a-z]+", lang) == None:
            Welcome("lang")
        list_arguments[3] = lang
    Welcome()


def ChangeRange():
    print("")
    print("What Range would like to use? (1-365)")
    range = input()
    if range != "back":
        if re.fullmatch("([0-9]{1,3}|all)", range) == None:
            Welcome("range")
        list_arguments[4] = range
    Welcome()


def ChangeType():
    print("")
    print("What Type of reviews would like to use? (all, positive, negative)")
    type = input()
    if type != "back":
        if re.fullmatch("(all|positive|negative)", type) == None:
            Welcome("type")
        list_arguments[5] = type
    Welcome()


def ChangePurchase():
    print("")
    print("What Purchase type would like to use? (all, non_steam_purchase, steam)")
    purchase = input()
    if purchase != "back":
        if re.fullmatch("(all|non_steam_purchase|steam)", purchase) == None:
            Welcome("purchase")
        list_arguments[6] = purchase
    Welcome()


def ChangeNumber():
    print("")
    print("How many reviews do you want? (Minimum 1)")
    number = input()
    if number != "back":
        if re.fullmatch("[0-9]+", number) == None:
            Welcome("number")
        list_arguments[7] = number
    Welcome()


def CallDotnetCommand():
    global list_arguments_types
    global list_arguments
    global command

    command = "dotnet run -- "
    command += list_arguments[0] + " "
    for i in range(1, len(list_arguments_types)):
        if list_arguments[i] != "":
            command += list_arguments_types[i] + "=" + list_arguments[i] + " "

    Welcome("gather")


def GatherDisplay():
    print("")
    print("Command sent:")
    print(command)
    os.system(command)
    os._exit(0)


Welcome()
