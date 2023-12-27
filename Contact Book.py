class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name not in self.contacts:
            self.contacts[name] = phone
            print(f"Contact {name} added successfully.")
        else:
            print(f"Contact {name} already exists. Use update_contact to modify.")

    def update_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} does not exist. Use add_contact to add a new contact.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} does not exist.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            contact_book.add_contact(name, phone)
        elif choice == '2':
            name = input("Enter the name: ")
            phone = input("Enter the new phone number: ")
            contact_book.update_contact(name, phone)
        elif choice == '3':
            name = input("Enter the name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '4':
            contact_book.display_contacts()
        elif choice == '5':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()
