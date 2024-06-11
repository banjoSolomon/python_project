from diary.diaries import Diaries
from diary.my_diary import Diary

if __name__ == "__main__":
    diaries = Diaries()
    print("WELCOME TO SEMICOLON DIARY")

    try:

        user_name1 = input("Enter UserName for Diary 1: ")

        password1 = ""
        while len(password1) != 4:
            password1 = input("Enter Password for Diary 1 (4 characters long): ")

        diary1 = Diary(user_name1, password1)
        diaries.add_diary(diary1)

        user_name2 = input("Enter UserName for Diary 2: ")

        password2 = ""
        while len(password2) != 4:
            password2 = input("Enter Password for Diary 2 (4 characters long): ")

        diary2 = Diary(user_name2, password2)
        diaries.add_diary(diary2)

        diary_list = diaries.get_diaries()
        for diary in diary_list:
            print("Diary Details:")
            print("UserName:", diary.get_user_name())
            print("Password:", diary.get_password())
            print("Is Locked:", diary.is_locked())

            lock_choice = input("Do you want to lock this diary? (yes/no): ")
            if lock_choice.lower() == "yes":
                diary.lock_diary()
                print("Diary is now locked.")

            entry_title = input("Enter Title for the new entry: ")
            entry_body = input("Enter Body for the new entry: ")

            new_entry = diary.create_entry(entry_title, entry_body, len(diary.get_entries()) + 1)
            print("New Entry Created with ID:", new_entry.get_id())

            # Display Entries
            entries = diary.get_entries()
            for entry in entries:
                print("Entry ID:", entry.get_id())
                print("Entry Title:", entry.get_name())
                print("Entry Body:", entry.get_body())
            print("THANK U FOR USING SEMICOLON DIARY>>>>>>>>>APP STILL UNDER REFACTORING")

    except Exception as e:
        print("An error occurred:", e)
