def main():
    email = input("enter your email id: ")
    if "@" in email:
        new_email = email.split("@")
        print(new_email[-1])
    else:
        print("invalid email")
main()