import datetime
from diary.diaries import Diaries
from diary.entry import Entry
from diary.my_diary import Diary


def main():
    diaries = Diaries()

    while True:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("\nWelcome To My Diary Application:")
        print("1. Create Diary")
        print("2. Unlock Diary")
        print("3. Add Entry")
        print("4. View Entries")
        print("5. Exit")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_diary(diaries)
        elif choice == "2":
            unlock_diary(diaries)
        elif choice == "3":
            add_entry(diaries)
        elif choice == "4":
            view_entries(diaries)
        elif choice == "5":
            print("Exiting the Diary Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


def create_diary(diaries):
    username = input("Enter username for the new diary: ")
    password = input("Set a password for the diary: ")
    diaries.add_diary(username, password)
    print(f"Diary for {username} created successfully!")


def unlock_diary(diaries):
    username = input("Enter your diary username: ")
    password = input("Enter your diary password: ")

    diary = diaries.find_diary_by_user_name(username)
    if diary and diary.get_password() == password:
        diary.set_locked(False)
        print("Diary unlocked successfully!")
    else:
        print("Invalid username or password. Diary unlocking failed.")


def add_entry(diaries):
    username = input("Enter your diary username: ")
    diary = diaries.find_diary_by_user_name(username)

    if diary and not diary.is_locked():
        title = input("Enter entry title: ")
        body = input("Enter entry body: ")
        diary.create_entry(title, body)
        print("Entry added successfully!")
    elif diary.is_locked():
        print("Diary is locked. Unlock the diary to add entries.")
    else:
        print("Diary not found. Please create a diary first.")


1


def view_entries(diaries):
    username = input("Enter your diary username: ")
    diary = diaries.find_diary_by_user_name(username)

    if diary and not diary.is_locked():
        entries = diary.get_entries()
        if entries:
            print("\nEntries in your diary:")
            for entry in entries:
                print(f"{entry.get_title()}\n{entry.get_body()}\n")
        else:
            print("No entries found.")
    elif diary.is_locked():
        print("Diary is locked. Unlock the diary to view entries.")
    else:
        print("Diary not found. Please create a diary first.")


if __name__ == "__main__":
    main()
