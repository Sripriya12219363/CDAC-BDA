def main():
    n=int(input("Enter N value: "))
    k=int(input("Enter K value: "))

    l=[]
    for i in range(n):
        l.append(i+1)
    for j in range(1,k+1):
        for i in range(n):
            ind=i+k-j
            if ind<len(l):
                print(f"The value that will be deleted is: {l[ind]}    |   ",end=" ")
                del(l[ind])
                print(f"The remaining list is: {l}")


    print(f"The final remaining list: {l}")
main()