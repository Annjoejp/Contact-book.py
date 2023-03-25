# Contact-book.py
contacts = {}

def add_contact(name, phone_number, email):
    contacts[name] = {'phone_number': phone_number, 'email': email}
    print(f"Contact {name} added successfully.")

def search_contact(name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone Number: {contacts[name]['phone_number']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"No contact found with the name {name}.")

def update_contact(name, phone_number=None, email=None):
    if name in contacts:
        if phone_number:
            contacts[name]['phone_number'] = phone_number
        if email:
            contacts[name]['email'] = email
        print(f"Contact {name} updated successfully.")
    else:
        print(f"No contact found with the name {name}.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"No contact found with the name {name}.")

# Example usage
add_contact('John', '555-1234', 'john@example.com')
search_contact('John')
update_contact('John', email='new_email@example.com')
search_contact('John')
delete_contact('John')
search_contact('John')
