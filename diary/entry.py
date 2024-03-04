import datetime


class Entry:
    _id_counter = 1

    def __init__(self, title, body):
        self.date_created = datetime.datetime.now()
        self.id = Entry._id_counter
        Entry._id_counter += 1
        self.title = title
        self.body = body

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_id(self):
        return self.id

    def set_title(self, new_title):
        self.title = new_title

    def set_body(self, body):
        self.body = body

    def get_date_created(self):
        return self.date_created
