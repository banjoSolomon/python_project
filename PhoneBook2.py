class Contact:
    def __init__(self, name, number, email, address):
        self.name = name
        self.number = number
        self.email = email
        self.address = address


def search_contacts(contacts_list, search_term):
    matching_contacts = []
    for contact in contacts_list:
        if (search_term.lower() in contact.user_name.lower() or
                search_term in contact.number or search_term.lower() in contact.email.lower() or
                search_term.lower() in contact.address.lower()):
            matching_contacts.append(contact)
    return matching_contacts


def display_contacts(contact_list):
    if not contact_list:
        print("No MATCHING CONTACTS FOUND.")
    else:
        print("Loading Matching contacts>>>>>>>>>>>>:")
        for contact in contact_list:
            print("---------------------------")
            print("Name:", contact.user_name)
            print("Number:", contact.number)
            print("Address:", contact.address)
            print("Email:", contact.email)
            print("---------------------------")


def main():
    contacts_list = []

    print("Welcome to your PHONE BOOK. Enter YES to view your PHONEBOOK: ")
    option = input().strip()

    while option.lower() != "yes":
        print("INVALID INPUT. Please enter YES to view your PHONEBOOK: ")
        option = input().strip()

    add_more = "YES"
    while add_more.upper() == "YES":
        print("Enter a new contact  (YES/NO): ")
        add_more = input().strip()

        if add_more.upper() == "YES":
            name = input("Enter name: ").strip()
            number = input("Enter phone number: ").strip()
            address = input("Enter address: ").strip()
            email = input("Enter email: ").strip()

            my_contact = Contact(name, number, address, email)
            contacts_list.append(my_contact)

            print("Your New PHONEBOOK LIST: ")
            for contact in contacts_list:
                print("-----------------------------")
                print("Name:", contact.name)
                print("Number:", contact.number)
                print("Address:", contact.address)
                print("Email:", contact.email)
                print("-----------------------------")
        elif add_more.upper() == "NO":
            print("Thank you for using the PHONEBOOK...WE ARE STILL REFACTORING THE APP THANKS")
            print("INVALID input. Please enter YES or NO.")
            print("DO YOU WANT TO SEARCH FOR A CONTACT? (YES/NO): ")
            search_option = input().strip()
            if search_option.upper() == "YES":
                search_term = input("Enter search term: ").strip()
                matching_contacts = search_contacts(contacts_list,search_term)
                display_contacts(matching_contacts)
            else:
                print("INVALID input. please enter Yes or No.")



if __name__ == "__main__":
    main()
