def main():
    st = input("Enter the string: ")
    ss = input("Enter the sub string: ")
    c = 0
    for i in range(0, len(st) - len(ss) + 1):
        val = True

        for j in range(0, len(ss)):
            if st[i + j] != ss[j]:
                val = False
                break

        if val:
            c += 1

    print(c)
main()
