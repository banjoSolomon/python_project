from diary.my_diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def add_diary(self, user_name, password):
        new_diary = Diary(user_name, password)
        self.diaries.append(new_diary)

    def get_diaries(self):
        return self.diaries

    def find_diary_by_user_name(self, user_name):
        for diary in self.diaries:
            if diary.get_name() == user_name:
                return diary
        return None

    def delete_diary(self, diary):
        if diary in self.diaries:
            self.diaries.remove(diary)
