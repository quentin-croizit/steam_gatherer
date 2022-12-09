# ---------------------------------------------------------------------------- #
# Source code by Antimatter/Quentin     (http://www.quentin-croizit.github.io) #
# ---------------------------------------------------------------------------- #

import re

preset_filler = ["1245620", "all", "english", "5", "all", "all", "50"]
preset_regex = '"\S*"\s*{[0-9]{1,7},(all|recent|updated),[a-z]+,([0-9]{1,3}|all),(all|positive|negative),(all|non_steam_purchase|steam),[0-9]+}'

presets = []


def gatherPreset():
    config = open("config", "r")
    config_lines = config.readlines()
    for i in range(len(config_lines)):
        config_lines[i] = config_lines[i].strip()

    for line in config_lines:
        if re.fullmatch(preset_regex, line) != None:
            lineToPreset(line)

    print(presets)


def lineToPreset(line):
    global presets
    preset_name = re.search("""(?<=").*(?=")""", line).group()
    preset_args = re.search("""(?<={).*(?=})""", line).group().split(",")
    preset_temp = [preset_name, preset_args]
    presets.append(preset_temp)


gatherPreset()
