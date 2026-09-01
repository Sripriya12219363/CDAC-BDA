def main():
    inp_str = input("Ënter the string: ")
    print("Portal transition activated")
    lst = ["staff","potion","spellbook"]
    print(f'the oldest ejected item is: {lst[0]}')
    del lst[0]
    lst.append(inp_str)
    #for i in lst:
    #    print(i)
    print(lst)
main()