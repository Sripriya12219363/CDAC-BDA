def main():
    st=input("Enter the string: ")
    ss=input("Enter the sub string: ")
    c=0
    l1=st.split(" ")
    l2=ss.split(" ")
    val=True
    for i in l1:
        for j in l2:
            if j==i:
                continue
            else:
                val=False
        if(val):
            c+=1
    print(c)
main()