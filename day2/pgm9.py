def main():
    s = input("Enter the string: ")
    longest = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]

            if sub == sub[::-1]:
                if len(sub) > len(longest):
                    longest = sub

    print(longest)


main()
