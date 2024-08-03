import json

class ContactBook:
    def __init__(self):
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        try:
            with open('contacts.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def save_contacts(self):
        with open('contacts.json', 'w') as file:
            json.dump(self.contacts, file, indent=4)
    
    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Contact with name '{name}' already exists.")
            return
        self.contacts[name] = {'phone': phone, 'email': email}
        self.save_contacts()
        print(f"Contact '{name}' added successfully.")
    
    def view_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(f"Name: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print(f"No contact found with name '{name}'.")
    
    def update_contact(self, name, phone=None, email=None):
        contact = self.contacts.get(name)
        if contact:
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            self.save_contacts()
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"No contact found with name '{name}'.")
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"No contact found with name '{name}'.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for name, details in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print()

def main():
    book = ContactBook()
    while True:
        print("1. Add contact")
        print("2. View contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. List all contacts")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            book.add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter contact name to view: ")
            book.view_contact(name)
        elif choice == '3':
            name = input("Enter contact name to update: ")
            phone = input("Enter new phone number (leave empty to keep unchanged): ")
            email = input("Enter new email address (leave empty to keep unchanged): ")
            book.update_contact(name, phone if phone else None, email if email else None)
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            book.delete_contact(name)
        elif choice == '5':
            book.list_contacts()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
