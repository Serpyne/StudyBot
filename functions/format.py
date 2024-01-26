
def format_seconds(seconds, verbose=False):
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return_string = ""
    if not verbose:
        for i, v in enumerate((days, hours, minutes, seconds)):
            if v > 0:
                return_string += f"{v}{"dhms"[i]} "

    else:
        for i, v in enumerate((days, hours, minutes, seconds)):
            if v > 0:
                return_string += f"{v} {
                    ("days hours minutes seconds".split())[i]} "
    return return_string
