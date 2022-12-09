# ---------------------------------------------------------------------------- #
# Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) #
# ---------------------------------------------------------------------------- #

import os
import re
import cli_visuals as visuals
import presets

arguments_types = [["id", "What GameID would like to use?", "[0-9]{1,7}"],
                   ["filter", "What Filter would like to use? [all, recent, updated]", "(all|recent|updated)"],
                   ["lang", "What Language would like to use?", "[a-z]+"],
                   ["range", "What Range would like to use? [1-365]", "[0-9]+"],
                   ["type", "What Type of reviews would like to use? [all, positive, negative]", "(all|positive|negative)"],
                   ["purchase", "What Purchase type would like to use? [all, non_steam_purchase, steam]", "(all|non_steam_purchase|steam)"],
                   ["number", "How many reviews do you want? [1-∞]", "[0-9]+"]]

arguments_list = ["", "", "", "", "", "", ""]

presets.gatherPreset()
visuals.clearConsole()


def main():
    global arguments_list
    visuals.printAppBox(arguments_list)

    if visuals.current_page == "arguments":
        print("What would like to do/modify?")
        value = input("> ")

    elif visuals.current_page == "commands" or visuals.current_page == "help":
        print("Press enter to go back to the arguments page")
        value = input("> ")
        visuals.current_page = "arguments"

    for i in range(0, len(arguments_types)):
        if value == arguments_types[i][0]:
            changeArgument(i)

    if value == "preset":
        applyPreset()

    elif value == "help":
        visuals.current_page = "help"

    elif value == "commands":
        visuals.current_page = "commands"

    elif value == "reset":
        arguments_list = ["", "", "", "", "", "", ""]
        main()

    elif value == "gather":
        if "" in arguments_list:
            argumentFiller()
        callDotnetCommand()

    elif value == "exit":
        os._exit(0)

    main()


def changeArgument(argument_index):
    global arguments_list
    visuals.printAppBox(arguments_list)

    print(arguments_types[argument_index][1])  # Prints message based on type of argument changed
    value = input("> ")  # Allow user to input value for type of argument selected
    if value != "back":  # Check for the 'back' command
        if re.fullmatch(arguments_types[argument_index][2], value) == None:  # Checks if the value is acceptable for the type of argument
            changeArgument(argument_index)
        if argument_index == 3 and int(value) > 365:  # Prevents a range superior than 365 (API can't go further)
            value = "365"
        arguments_list[argument_index] = value
    main()


def applyPreset():
    global arguments_list
    replace = 0
    visuals.printAppBox(arguments_list)

    print("What Preset would like to use?")  # Prints message based on type of argument changed
    value = input("> ")  # Allow user to input value for type of argument selected
    if value != "back":  # Check for the 'back' command
        if re.fullmatch("[\s\S]*", value) == None:  # Checks if the value is acceptable for the type of argument
            applyPreset()
        if value[-1] == "*":  # Checks if the preset name has a star at the end to not clear already entered values
            replace = 1
            value = value.rstrip(value[-1])  # Removes the *
        for preset in presets.presets:
            if preset[0] == value:  # Finds the given preset
                for i in range(len(preset[1])):
                    if (not (replace == 1 and not (arguments_list[i] == ""))):
                        arguments_list[i] = preset[1][i]
                main()
        applyPreset()

    main()


def argumentFiller():  # Fills empty arguments if there is any
    global arguments_list
    for i in range(len(arguments_list)):
        if arguments_list[i] == "":
            arguments_list[i] = presets.preset_filler[i]


def callDotnetCommand():  # Creates the command for the dotnet program using the inputed arguments
    command = "dotnet run -- "
    for i in range(len(arguments_list)):
        if arguments_list[i] != "":
            command += arguments_list[i] + " "
    gatherDisplay(command)


def gatherDisplay(cli_command):  # Displays and calls the command sent to the CLI and exits the python program
    visuals.printAppBox(arguments_list)
    print("Command sent:")
    print(cli_command)
    os.system(cli_command)
    os._exit(0)


main()
