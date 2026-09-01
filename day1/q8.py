def main():
    n=int(input("Enter the value of n: "))
    if n>=90 and n<100:
        print("A")
    elif n>=80 and n<89:
        print("B")
    elif n>=70 and n<79:
        print("C")
    elif n>=60 and n<69:
        print("D")
    elif n<60:
        print("F")
    else:
        print("Enter valid number")
main()