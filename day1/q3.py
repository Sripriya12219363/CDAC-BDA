def main():
    num = int(input("Enter a NUM: "))

    l=num//2
    for d in range(2,l+1):
        if(num%d==0):
            print("Not a prime number")
            return
    else:
        print("Prime Number")
main()