import sqlite3


def get_db():
    db = sqlite3.connect('Books' ,detect_types=sqlite3.PARSE_DECLTYPES)
    return db