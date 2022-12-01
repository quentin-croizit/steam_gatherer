import os
import re
import cli_visuals as visuals

arguments_types = [["preset", "What Preset would like to use?", "[\s\S]*"],
                   ["id", "What GameID would like to use?", "[0-9]+"],
                   ["filter", "What Filter would like to use? [all, recent, updated]", "(all|recent|updated)"],
                   ["lang", "What Language would like to use?", "[a-z]+"],
                   ["range", "What Range would like to use? [1-365]", "[0-9]+"],
                   ["type", "What Type of reviews would like to use? [all, positive, negative]", "(all|positive|negative)"],
                   ["purchase", "What Purchase type would like to use? [all, non_steam_purchase, steam]", "(all|non_steam_purchase|steam)"],
                   ["number", "How many reviews do you want? [1-∞]", "[0-9]+"]]

arguments_list = ["", "", "", "", "", "", "", ""]
command = ""

visuals.clearConsole()


def main():
    global arguments_list
    visuals.printAppBox(arguments_list)

    print("What would like to do/modify?")
    value = input()

    for i in range(0, len(arguments_types)):
        if value == arguments_types[i][0]:
            changeArgument(i)

    if value == "reset":
        arguments_list = ["", "", "", "", "", "", "", ""]
        main()

    elif value == "gather":
        callDotnetCommand()

    elif value == "exit":
        os._exit(0)

    main()


def changeArgument(argument_index):
    global arguments_list
    visuals.printAppBox(arguments_list)

    print(arguments_types[argument_index][1])  # Prints message based on type of argument changed
    value = input()  # Allow user to input value for type of argument selected
    if value != "back":  # Check for the 'back' command
        if re.fullmatch(arguments_types[argument_index][2], value) == None:  # Checks if the value is acceptable for the type of argument
            changeArgument(argument_index)
        arguments_list[argument_index] = value
    main()


def callDotnetCommand():  # Creates the command for the dotnet program using the inputed arguments
    command = "dotnet run -- "
    command += arguments_list[0] + " "
    for i in range(1, len(arguments_types)):
        if arguments_list[i] != "":
            command += arguments_types[i] + "=" + arguments_list[i] + " "
    gatherDisplay()


def gatherDisplay():  # Displays and calls the command sent to the CLI and exits the python program
    print("Command sent:")
    print(command)
    os.system(command)
    os._exit(0)


main()
