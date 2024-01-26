import json
from functions.get_settings import get_path


def set_db(db):
    json.dump(db, open(get_path("db"), "w"), indent=4, sort_keys=True)


def increment_cooldown(increment):
    db = json.load(open(get_path("db"), "r"))

    for key in db:
        data = db[key]
        data["add_cooldown"] = max(db[key]["add_cooldown"] - increment, 0)
        db[key] = data

    set_db(db)
