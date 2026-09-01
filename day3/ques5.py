def main():
    str=input("Enter the string: ")
    str1=str.split(" ")
    res=""
    for i in str1:
        res+=i[::-1]
        res+=" "
    print(f"Output: {res}")
main()
