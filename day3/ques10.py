def main():
    snake_pos=input("Enter the position of snake in the (x,y) format: ")
    snake_pos=tuple([int(n) for n in snake_pos.split(",")])
    food=(2,3)
    ch="  .  "
    for i in range(5):
        for j in range(5):
            if(i,j)==snake_pos:
                ch="  S  "
            elif (i,j)==food:
                ch="  F  "
            else:
                ch="  .  "
            print(ch,end="")
        print()
    if(snake_pos==food):
        print("Yum! The snake ate the food")
main()