#!/usr/bin/env python3
"""
Show directory specific notes.
"""
import os
import sys
import hashlib
import subprocess
from database import DumbDB


CONFIG_PATH = '~/.config/dirnotes.ini'
NOTE_FORMAT = 'id, date, text'
DELIMETER = '\n' + '-' * 78 + '\n'


def open_db():
    """Sqlite or json"""
    db = DumbDB()
    return db


def get_hash(path):
    "Calculate the hash of path (what about inode of the folder?)"
    return hashlib.sha1(path.encode()).hexdigest()


def get_notes(db, path):
    "Notes lookup in the database (Sqlite?)"
    path_hash = get_hash(path)
    return db.read(path_hash)


def main():
    args = sys.argv

    out = subprocess.check_output(["ls"] + args[1:], universal_newlines=True)
    db = open_db()
    path = os.path.abspath('.')
    notes = get_notes(db, path)
    print(out + DELIMETER)
    for note in notes:
        print(note.strip())


if __name__ == "__main__":
    main()
