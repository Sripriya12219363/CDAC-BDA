def main():
    s = input("Enter the string: ")
    res = ""
    count = 1

    for i in range(0, len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            res += s[i] + str(count)
            count = 1

    if len(res) < len(s):
        print(res)
    else:
        print(s)


main()
