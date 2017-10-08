"""Database backends for holding notes"""
from collections import defaultdict

DUMB_TYPE = 'dumb'


class DB():
    def __init__(self, db_type):
        self.db_type = db_type

    def create(self, path_hash, notes):
        raise NotImplementedError

    def read(self, path_hash):
        raise NotImplementedError

    def update(self, path_hash, note_id, text):
        raise NotImplementedError

    def delete(self, path_hash, note_id=None):
        raise NotImplementedError

    def backup(self):
        raise NotImplementedError

    def debug(self):
        raise NotImplementedError


class DumbDB(DB):

    def __init__(self, db_type=DUMB_TYPE):
        self.notes = defaultdict(list)
        self.load()
        super(DumbDB, self).__init__(db_type)

    def create(self, path_hash, notes):
        for note in notes:
            self.notes[path_hash].append(note)
        return True

    def read(self, path_hash):
        return self.notes.get(path_hash, None)

    def update(self, path_hash, note_id, text):
        if len(self.notes.get(path_hash, [])) > note_id-1:
            self.notes[path_hash][note_id] = text
            return True
        else:
            return False

    def delete(self, path_hash, note_id=None):
        if len(self.notes.get(path_hash, [])) > note_id-1:
            res = self.notes.pop(note_id)
            if res:
                return True
            else:
                return False
        return False

    def dump(self):
        storage_file = open('sorage.txt', 'w')

        for path_hash in self.notes:
            storage_file.write(path_hash+';'+','.join(self.notes[path_hash])+'\n')

        storage_file.close()

    def load(self):
        storage_file = open('storage.txt', 'r')

        for line in storage_file.readlines():
            path_hash, notes = line.split(';')
            self.notes[path_hash] = notes.split(',')

        storage_file.close()
