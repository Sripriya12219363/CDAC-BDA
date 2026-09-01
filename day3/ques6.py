def main():
    str=input("Enter space seperated integers: ")
    l=str.split(" ")
    l1=[]
    for i in l:
        l1.append(int(i))
    res=[x+10 if x<50 else (100 if x>95 else x+5) for x in l1]
    print("Original: ",l1)
    print("Curved: ",res)
main()