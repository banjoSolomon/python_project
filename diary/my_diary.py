from diary.entry import Entry
from diary.invalid_pin import InvalidPINError


class Diary:
    def __init__(self, user_name, password):
        self.entries = []
        self.locked = False
        self.password = password
        self.user_name = user_name

    def get_name(self):
        return self.user_name

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def is_locked(self):
        return self.locked

    def set_locked(self, locked):
        self.locked = locked

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_entries(self):
        return self.entries

    def unlock_diary(self, password):
        if password == password:
            self.locked = False
        else:
            raise InvalidPINError("Invalid PIN provided")

    def create_entry(self, title, body):
        new_entry = Entry(title, body)
        self.entries.append(new_entry)

    def delete_entry(self, entry_id):
        self.entries = [entry for entry in self.entries if entry.get_id() != entry_id]

    def find_entry_by_id(self, entry_id):
        for entry in self.entries:
            if entry.get_id() == entry_id:
                return entry
        return None

    def update_entry(self, entry_id, new_title, new_body):
        entry_to_update = self.find_entry_by_id(entry_id)
        if entry_to_update:
            entry_to_update.set_title(new_title)
            entry_to_update.set_body(new_body)




