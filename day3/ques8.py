def main():
    cart = ["apple", "banana", "apple", "orange", "banana","banana"]
    res=[]
    for i in cart:
        if(i not in res):
            res.append(i)
    print(res)
main()