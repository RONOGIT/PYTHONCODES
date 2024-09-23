contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")

def view_contacts():
    print("\nContacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

# Example 
number = int(input("Enter number of contacts to save: "))
for i in range(number):
    name = input(f"Enter name {i + 1}: ")  # Using f-string to include i + 1
    num = input("Enter phone number: ")
    add_contact(name, num)

view_contacts() 
