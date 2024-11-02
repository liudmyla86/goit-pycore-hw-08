
import pickle
        

class AddressBook:
    def __init__(self):
            self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact


    def find_contact(self, name):
        return  self.contacts.get(name)
        
def save_data(book, filename="addressbook.pk1"):
    with open(filename, "wb") as f:
        pickle.dump(book, f) 

def load_data(filename="addressbook.pk1"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():

    book = load_data()
    print("Welcome to the Address Book!")

    while True:
        command = input("Enter a command (add, find, exit):").strip().lower()

        if command in ("exit", "close"):
            save_data(book)
            print("Address book saved. Goodbye!")
            break

        elif command == "add":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            contact = contact(name, phone)
            book.add_contact(contact)
            print(f"Contact {name} added")

        elif command == "find":
            name = input("Enter name to find: ")
            contact = book.find_contact(name)
            if contact:
                print(f" Contact found: {contact}")
            else:
                print("Contact not found")