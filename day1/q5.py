def main():
    num1=int(input("Enter num1: "))
    num2=int(input("Ënter num2: "))
    op=input("Enter operator: ")
    if op=='+':
        print(num1+num2)
    elif op=='-':
        print(num1-num2)
    elif op=='*':
        print(num1*num2)
    elif op=="/":
        print(num1/num2)
    else:
        print("Ënter valid operator")    
main()