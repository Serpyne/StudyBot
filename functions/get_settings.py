from pytz import timezone
import json
import os


def get_path(file=None):
    settings = json.load(open("./src/data/settings.json", "r"))
    paths = settings["paths"]
    if file:
        return paths[file]
    return paths


def get_settings(setting=None):
    settings = json.load(open(get_path("settings"), "r"))
    s = {
        "ADD_LIMIT": settings["add_limit"],
        "ADD_COOLDOWN": settings["add_cooldown"],
        "LEADERBOARD_MAX_DISPLAY": settings["leaderboard_max_display"],
        "TZINFO": timezone(os.getenv("TIMEZONE")),
        "BACKUP_INTERVAL": settings["backup_interval"],
    }
    if setting:
        return s[setting]

    return s


def load_settings_dict(type="basic"):
    return_dict = {}
    if type == "basic":

        for line in open(get_path("commands")).readlines():
            if len(line.split(": ")) >= 2 and "*" not in line:
                name = line.split(": ")[0]
                description = line.split(": ", 1)[1]
                return_dict[name] = description

    elif type == "admin":

        for line in open(get_path("commands")).readlines():
            if len(line.split(": ")) >= 2 and "*" in line:
                line = line.replace("*", "")
                name = line.split(": ")[0]
                description = line.split(": ", 1)[1]
                return_dict[name] = description

    return return_dict
