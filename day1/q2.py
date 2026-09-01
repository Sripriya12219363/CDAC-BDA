def main():
    n=int(input("Enter a number: "))
    a=0
    b=1
    print(a,b, end=" ")
    for i in range(n-2):
        sum=a+b
        print(sum, end=" ")
        temp=a
        a=b
        b=sum

main()