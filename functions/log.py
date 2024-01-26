from functions.get_settings import get_settings, get_path
import datetime


def log_message(message):
    TZINFO = get_settings("TZINFO")
    date_time = datetime.datetime.now(
        tz=TZINFO).strftime("| %d/%m/%y %H:%M:%S |")
    with open(get_path("log"), "a") as f:
        f.write(f"{date_time}        {message}\n")
