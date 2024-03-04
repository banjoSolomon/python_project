class Contact:
    def __init__(self, name, number, email, address):
        self.name = name
        self.number = number
        self.email = email
        self.address = address

def main():
    contacts_list = [
        Contact("Dayo", "08145783126", "TemiDayo@gmail.com", "24 Sabo Yaba Lagos"),
        Contact("Ken", "09036785489", "KenDon@Gmail.com", "7 Adebare Street Lagos"),
        Contact("Solomon", "08164556912", "Ayomidebanjo02@gmail.com", "21 Ogudu road Lagos"),
        Contact("Kelly", "08145457812", "Kellytem@gmail.com", "12 Gbagada lagos"),
        Contact("Mr Chibuzor", "09065790643", "IAM@gmail.com", "15 lasa Lagos")
    ]

    print("Welcome to your PHONE BOOK. Enter YES to view your PHONEBOOK: ")
    option = input().strip()

    while option.lower() != "yes":
        print("INVALID INPUT. Please enter YES to view your PHONEBOOK: ")
        option = input().strip()

    print("These are your PHONEBOOK LIST: ")
    for contact in contacts_list:
        print("-----------------------------")
        print("Name:", contact.name)
        print("Number:", contact.number)
        print("Address:", contact.address)
        print("Email:", contact.email)
        print("-----------------------------")

    add_more = "YES"
    while add_more.upper() == "YES":
        print("Would you like to add another contact? (YES/NO): ")
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
            print("Thank you for using the PHONEBOOK")
        else:
            print("INVALID input. Please enter YES or NO.")

if __name__ == "__main__":
    main()
