def main():
    new_mv = input("Enter yourt choice of movie:")
    mov_lst = ["Inception","The Matrix","Intersteller"]
    if new_mv in mov_lst:
        print("Already existing!")
    else:
        mov_lst.append(new_mv)
        mov_lst.sort()
        print(mov_lst)
main()