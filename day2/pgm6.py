def main():
    res=" "
    s=input("Enter the string: ")
    for i in s:
        res+=chr(ord(i)+3)
    print(res)
main()