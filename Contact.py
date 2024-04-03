class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                found_contacts.append(contact)
        if not found_contacts:
            print("No matching contacts found.")
        else:
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

    def update_contact(self, index, new_contact):
        if 0 < index <= len(self.contacts):
            self.contacts[index - 1] = new_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(Contact(name, phone, email, address))
            print("Contact added successfully.")

        elif choice == "2":
            print("\nContact List:")
            contact_book.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)

        elif choice == "4":
            index = int(input("Enter the index of the contact to update: "))
            if 0 < index <= len(contact_book.contacts):
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                contact_book.update_contact(index, Contact(name, phone, email, address))
            else:
                print("Invalid contact index.")

        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: "))
            contact_book.delete_contact(index)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
