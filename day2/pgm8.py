def main():
    s=input("Enter the input string: ")
    l=s.split(" ")
    l1=l.copy()
    del l1[-1]
    res=""
    for i in l1:
        res+=i[0].upper()
        res+=". "
    res+=l[-1]
    print(res)
main()