def main():
    sample_string = input("Enter your String: ")
    s=sample_string.split(" ")
    l=len(s)-1
    a=e=i=o=u=c=0
    for x in sample_string:
        if x == "a":
            a+= 1
        elif x == "e":
            e+= 1
        elif x == "i":
            i+= 1
        elif x == "o":
            o+= 1
        elif x == "u":
            u+= 1
        else:
            c+= 1
    print(a,e,i,o,u,c-l)
main()