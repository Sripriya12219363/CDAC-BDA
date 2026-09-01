def main():
    inp = input("Enter the resource: ")
    res_lst = ["coal", "iron", "gold", "coal","timber", "coal"]
    if inp in res_lst:
        print(f'no of counts: {res_lst.count(inp)}')
        for i in range(0,len(res_lst)):
            if inp == res_lst[i]:
                print(f"found at index: {i}")
                break
    else:
        print("Resource not found!")
    

main()