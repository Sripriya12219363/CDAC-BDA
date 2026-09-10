import re
class InvalidPhoneNumberError(Exception):
    print("Phone number must contain digits only.")
phone_book={}
def register_contact(phone_book, name, phone_input):
    phone=int(phone_input)
    name_val=r"[A-Za-z ]"
    ans=re.fullmatch(name_val,name)
    if ans:
        raise ValueError("Contact name must be a non-empty alphabetic string.")

    ph_val=r"^[0-9]+$"
    ans1=re.match(ph_val,phone)
    if ans1:
        raise InvalidPhoneNumberError()
    phone_book['name']=phone_input
    return phone_book
def main():
    global phone_book
    try:
        name=input("Enter name: ")
        phone_input=input("Enter phone number: ")
        a1=register_contact(phone_book,name,phone_input)
        print(a1)
    except InvalidPhoneNumberError as e:
        print(e)
main()



#half done