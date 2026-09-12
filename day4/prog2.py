import re

class InvalidPhoneNumberError(Exception):
    pass

phone_book = {}

def register_contact(phone_book, name, phone_input):
    name_val = r"[A-Za-z ]+"
    ans = re.fullmatch(name_val, name)

    if not name or not ans:
        raise ValueError("Contact name must be a non-empty alphabetic string.")

    try:
        phone = int(phone_input)
    except ValueError:
        raise InvalidPhoneNumberError("Phone number must contain digits only.")

    phone_book[name] = phone_input
    return phone_book

def main():
    global phone_book

    try:
        name = input("Enter name: ")
        phone_input = input("Enter phone number: ")
        a1 = register_contact(phone_book, name, phone_input)
        print(a1)
    except InvalidPhoneNumberError as e:
        print(e)
    except ValueError as e:
        print(e)

main()
