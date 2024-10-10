from decorations import input_error

@input_error
def add_contact(args, contacts):
    name, phone_number = args
    if name in contacts:
        raise KeyError
    else:   
        contacts[name] = phone_number

    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone_number = args
    if name not in contacts:
        raise IndexError
    else:
        contacts[name] = new_phone_number

    return "Contact updated."


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    
    if name not in contacts:
        raise IndexError
    else:
        return f"{name} has the following phone number: {contacts[name]}."


def show_all(contacts):
    if any(contacts):
        for contact in contacts.keys():
            print(f"{contact} has phone number: {contacts[contact]}")
    else:
        print(f"Contact list is empty")
