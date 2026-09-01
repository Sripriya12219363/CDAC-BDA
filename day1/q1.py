def main():

    num = int(input("Enter a year: "))

    if num % 400 == 0 or num%4 ==0 and num %100 !=0 :
        print("Leap year")
    else:
        print("not leap yaer")
main()