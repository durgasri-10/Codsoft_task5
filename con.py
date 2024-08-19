class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name, phone, email, address):
        if name in self.contacts:
            print(f"Contact with name '{name}' already exists.")
        else:
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            print(f"Contact '{name}' added")

    def view_contacts(self):
        if not self.contacts:
            print("Not found.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self, query):
        results = {name: details for name, details in self.contacts.items() if query.lower() in name.lower() or query in details['phone']}
        
        if not results:
            print("Not found.")
        else:
            print("\nSearch Results:")
            for name, details in results.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    def update_contact(self, name):
        if name in self.contacts:
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address

            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact with name '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact with name '{name}' not found.")

    def menu(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contact")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                query = input("Enter name or phone number to search: ")
                self.search_contact(query)
            elif choice == '4':
                name = input("Enter the name of the contact to update: ")
                self.update_contact(name)
            elif choice == '5':
                name = input("Enter the name of the contact to delete: ")
                self.delete_contact(name)
            elif choice == '6':
                print("Exiting Contact Book.")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()
