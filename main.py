#!/usr/bin/env python3
"""
Show directory specific notes.
"""
import os
import subprocess
from database import DB


CONFIG_PATH = '~/.config/dirnotes.ini'
NOTE_FORMAT = 'id, date, text'
DELIMETER = '\n' + '-' * 78 + '\n'


def open_db():
    """Sqlite or json"""
    db = DB()
    return db


def get_hash(path):
    "Calculate the hash of path (what about inode of the folder?)"
    return 123


def get_notes(path):
    path_hash = get_hash(path)
    "Notes lookup in the database (Sqlite?)"
    return '1) This is a first note'


def main():
    out = subprocess.check_output(["ls", "-la"], universal_newlines=True)
    db = open_db
    notes = get_notes(os.path.abspath('.'))
    print(out + DELIMETER)
    print(notes)


if __name__ == "__main__":
    main()
