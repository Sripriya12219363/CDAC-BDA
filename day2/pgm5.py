def main():
    s=input("Enter the string: ")
    s1=s.split(" ")
    res=""
    for i in s1:
        for j in range(0,len(i)):
            if(j==0):
                res+=i[j].upper()
            else:
                res+=i[j].lower()
        res+=" "
    print(res)
main()