import datetime
import unittest

from diary import entry
from diary.diaries import Diaries
from diary.entry import Entry
from diary.invalid_pin import InvalidPINError
from diary.my_diary import Diary


class TestDiary(unittest.TestCase):
    def setUp(self):
        self.diary = Diary("Banjo Solomon", "12345")
        self.entry = Entry("SEMICOLON", "My stories", )
        self.created_entry = Entry("Enter name", "Enter password")
        self.diaries = Diaries()

    def test_diary_has_a_username(self):
        self.assertEqual("Banjo Solomon", self.diary.get_name())

    def test_diary_has_a_password(self):
        self.diary = Diary("Banjo Solomon", "12345")
        self.password = "12345"
        self.diary.set_password(self.password)
        actual_password = self.diary.get_password()
        self.assertEqual(actual_password, self.diary.get_password())

    def testDiary_Can_BeUnlocked_ByDefault_And_DiaryCan_BeLocked(self):
        self.diary = Diary("Banjo Solomon", "12345")
        self.assertFalse(self.diary.is_locked())
        self.diary.set_locked(True)
        self.assertTrue(self.diary.is_locked())

    def test_diary_entry(self):
        self.diary = Diary("Banjo Solomon", "12345")
        self.entry = Entry("SEMICOLON", "My stories")
        self.diary.add_entry(self.entry)
        entries = self.diary.get_entries()
        self.assertTrue(self.entry in entries)

    def test_unlock_diary(self):
        self.diary = Diary("Banjo Solomon", "12345")
        self.assertFalse(self.diary.is_locked())
        self.diary.set_locked(True)
        self.diary.unlock_diary("12345")
        self.assertFalse(self.diary.unlock_diary("1234"))

    def test_lock_diary(self):
        self.diary = Diary("Banjo Solomon", "12345")
        self.diary.set_locked(True)
        self.assertTrue(self.diary.is_locked())

    def test_to_create_an_entry(self):
        self.diary = Diary("Banjo Solomon", "12345")
        self.diary.create_entry("SEMICOLON", "My stories")
        entries = self.diary.get_entries()
        self.assertTrue(entries)
        created_entry = entries[0]
        self.assertEqual(created_entry.get_title(), "SEMICOLON")
        self.assertEqual(created_entry.get_body(), "My stories")

    def test_to_delete_entry(self):
        self.diary = Diary("Banjo Solomon", "12345")
        self.diary.create_entry("SEMICOLON", "My stories")
        entries_before_deletion = self.diary.get_entries()
        self.assertTrue(entries_before_deletion)
        created_entry = entries_before_deletion[0]
        self.diary.add_entry(created_entry)
        self.diary.delete_entry(created_entry.get_id())
        entries_after_deletion = self.diary.get_entries()
        self.assertFalse(entries_after_deletion)

    def test_to_find_entry_by_id(self):
        self.diary = Diary("Banjo Solomon", "12345")
        self.diary.create_entry("SEMICOLON", "My stories")
        entries = self.diary.get_entries()
        self.assertTrue(entries)

        created_entry = entries[0]
        found_entry = self.diary.find_entry_by_id(created_entry.get_id())
        self.assertEqual(found_entry, created_entry)

    def test_to_update_entry(self):
        self.diary = Diary("Banjo Solomon", "12345")
        self.diary.create_entry("SEMICOLON", "My stories")
        entries_before_update = self.diary.get_entries()
        self.assertTrue(entries_before_update)

        created_entry = entries_before_update[0]
        updated_title = "Software"
        updated_body = "Loving The Job"

        self.diary.update_entry(created_entry.get_id(), updated_title, updated_body)

        entries_after_update = self.diary.get_entries()
        self.assertTrue(entries_after_update)

        updated_entry = entries_after_update[0]
        self.assertEqual(updated_entry.get_title(), updated_title)
        self.assertEqual(updated_entry.get_body(), updated_body)

    def test_entry_has_a_title_and_body(self):
        self.diary.create_entry("SEMICOLON", "My stories")
        entries = self.diary.get_entries()
        self.assertTrue(entries)

        created_entry = entries[0]
        entry_title = created_entry.get_title()
        entry_body = created_entry.get_body()

        self.assertEqual(entry_title, "SEMICOLON")
        self.assertEqual(entry_body, "My stories")

    def test_date_created_in_entry(self):
        current_datetime = datetime.datetime.now()
        self.diary.create_entry("SEMICOLON", "My stories")
        entries = self.diary.get_entries()
        self.assertTrue(entries)

        created_entry = entries[0]
        entry_date = created_entry.get_date_created()
        self.assertLessEqual(current_datetime - entry_date, datetime.timedelta(seconds=1))

    def test_diaries_has_list_diary(self):
        self.diaries = Diaries()
        self.diary = Diary("Banjo Solomon", "12345")
        self.diaries.add_diary("Justin Parker", "12345")
        diary_list = self.diaries.get_diaries()
        self.assertIsInstance(diary_list, list)
        self.assertTrue(diary_list)

    def test_find_diary_by_user_name(self):
        self.diaries.add_diary("Banjo Solomon", "Id2468")
        self.diaries.add_diary("Sam Walker", "231")
        self.diaries.add_diary("Divine", "290")

        find_diary = self.diaries.find_diary_by_user_name("Sam Walker")
        self.assertIsNotNone(find_diary)
        self.assertEqual("Sam Walker", find_diary.get_name())
        self.assertEqual("231", find_diary.get_password())

    def test_to_delete_diary(self):
        self.diaries = Diaries()
        self.diaries.add_diary("Banjo Solomon", "Id2468")
        self.diaries.add_diary("Sam Walker", "231")
        self.diaries.add_diary("Divine", "290")

        diary_to_delete = self.diaries.find_diary_by_user_name("Divine")
        self.assertIsNotNone(diary_to_delete)
        self.diaries.delete_diary(diary_to_delete)


