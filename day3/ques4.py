def main():
    old_q = ['Guido', 'Esha', 'Rajan', 'Kishori']
    check=False
    while True:
        inp = input('Enter the guest name:')
        if(inp=="exit"):
            break
        else:
            index=0
            for i in range(0, len(old_q)):
                if(inp==old_q[i]):
                    check=True
                    index=i
            if(check):
                temp=old_q[index]
                while(index>=0):
                    old_q[index]=old_q[index-1]
                    index=index-1
                old_q[0]=temp
                print(f'{inp} moved to the front!')
            else:
                print("Access denied. Not on the VIP list.")
            print("Current VIP queue: ",old_q)
main()