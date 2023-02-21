# ---------------------------------------------------------------------------- #
# Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) #
# ---------------------------------------------------------------------------- #

import re

preset_filler = ["1245620", "all", "english", "5", "all", "all", "50"]
preset_regex = '"\S*"\s*{[0-9]{1,7},(all|recent|updated),[a-z]+,([0-9]{1,3}|all),(all|positive|negative),(all|non_steam_purchase|steam),[0-9]+,[\s\S]+}'

presets = []

def gatherPreset():
    config = open("config", "r")
    config_lines = config.readlines()
    for i in range(len(config_lines)):
        config_lines[i] = config_lines[i].strip()

    for line in config_lines:
        if re.fullmatch(preset_regex, line) != None:
            lineToPreset(line)
            print(line)

def lineToPreset(line):
    global presets
    preset_name = re.search("""(?<=").*(?=")""", line).group()
    preset_args = re.search("""(?<={).*(?=})""", line).group().split(",")
    preset_temp = [preset_name, preset_args]
    presets.append(preset_temp)

def preset_argument_format(preset_args):
    label_id = "ID: {id} / ".format(id=preset_args[0])
    label_filter = "Filter: {filter} / ".format(filter=preset_args[1])
    label_lang = "Lang: {lang} / ".format(lang=preset_args[2])
    label_range = "Range: {range} / ".format(range=preset_args[3])
    label_type = "Type: {type} / ".format(type=preset_args[4])
    label_purchase = "Purchase: {purchase} / ".format(purchase=preset_args[5])
    label_number = "Number: {number}".format(number=preset_args[6])
    return label_id + label_filter + label_lang + label_range + label_type + label_purchase + label_number