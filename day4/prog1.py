def manage_bookstore_inventory(inventory, action, book_title, quantity=0):
    if action=="add":
        inventory[book_title]=quantity
        print(inventory)
    elif action=="sell":
        val=inventory.get(book_title)
        if(val):
            if quantity>val:
                print(f"Error: Insufficient stock for {book_title}. Available: {val}")
            else:
                val=val-quantity
                inventory[book_title]=val
                print(f"Result: {inventory}")
                
        else:
            print(f"Error: Book {book_title} not found in the inventory")   
    elif action=="lookup":
        ans=inventory.get(book_title)
        if ans:
            print(f'The book {book_title} is available and number of books available are: {inventory.get(book_title)}')
        else:
            print(f'The book {book_title} is not available')

def main():
    inventory = {"Python Basics": 10, "Learning AI": 5}
    while True:
        act=input("Enter the action to be performed on the inventory: ")
        if(act=="exit"):
            break
        else:
            b_title=input("Enter the book title: ")
            quan=int(input("Enter the quantity: "))
            manage_bookstore_inventory(inventory, act, b_title, quan)
main()
