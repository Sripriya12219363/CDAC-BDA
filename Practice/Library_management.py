def menu():
    menu="""
    1. Add Book
    2. View Catalog
    3. Search Books
    4. Update Details
    5. Delete Book
    6. Save to file
    7. Load from file
    8. Exit
    """
    print(menu)
    choice=int(input("Enter the operation you want to perform: "))
    return choice
    
    
ls=[]
next_id=0

def add_book():
    global next_id
    try:
        title=input("Enter the title: ")
        author=input("Enter the author: ")
        genre=input("Enter the genre: ")
        price=float(input("Enter the price: "))
        copies=int(input("Enter number of copies: "))
        next_id+=1
        ls.append({"id":next_id,"title":title,"author":author,"genre":genre,"price":price,"copies":copies})

        print("Data added successfully!!!")

    except:
        print("Enter valid inputs")

    

def render_catalog():
    print("-"*90)
    print(f'{"ID":<10}{"Title":<20}{"Author":<20}{"Genre":<20}{"Price":<10}{"Copies":<10}')
    print("-"*90)
    for i in ls:
        bid,t,a,g,p,c=i.values()
        print(f'{bid:<10}{t:<20}{a:<20}{g:<20}{p:<10}{c:<10}')
    print("-"*90)


def query_books():
    try:
        op="""1. Search by id
        2. Search by title
        3. Search by author"""
        print(op)
        inp=int(input("Enter the search operation you need to perform: "))
        if inp==1:
            sid=int(input("Enter the input you want to search: "))
            search_by_id(sid)
        elif inp==2:
            search_by_title()
        elif inp==3:
            search_by_author()
        else:
            print("Enter valid input")
    except:
        print("Input should be specifed format")

def search_by_id(sid):
    res=[a for a in ls if a['id']==sid]
    if res:
        print("Record found successfully")
    else:
        print("Record not found")

    return res

def search_by_title():
    st=input("Enter the title to search")
    res=[a for a in ls if a['title']==st]
    if res:
        print("Record found")
    else:
        print("Record not found")

def search_by_author():
    st=input("Enter the title to search")
    res=[a for a in ls if a['author']==st]
    if res:
        print("Record found")
    else:
        print("Record not found")

def modify_book_details():
    uid=int(input("Enter the id which you want to update: "))
    val=search_by_id(uid)
    p=int(input("Enter the price to update: "))

def delete_book():
    try:
        inp=int(input("Enter the id for which you want to delete: "))
        ans=search_by_id(inp)
        if ans:
            c=input("Are you sure want to delete the entry(y/n): ").lower()
            if c=='y':
                ls.remove(ans[0])
                print("Deletion successful")
            else:
                print("Continue with next function then")
    except:
        print("Enter valid input")

def sync_catalog_to_file():
    try:
        filename=input("Enter the name of the file to store: ")
        with open(filename,"wt") as f:
            for c in ls:
                cid,title,author,genre,price,copies=c.values()
                f.write(f'{cid} | {title} | {author} | {genre} | {price} | {copies}\n')
    except:
        print("Enter valid entries")

def load_catalog_from_file():
    try:
        inp=input("Enter the filename to load: ")
        with open(inp,"r") as f:
            a=f.read()
            print(a)
    except:
        print("Enter valid inputs")

def main():
    while True:
        m=menu()
        
        match m:
            case 1:
                add_book()
            case 2:
                render_catalog()
            case 3:
                query_books()
            case 4:
                modify_book_details()
            case 5:
                delete_book()
            case 6:
                sync_catalog_to_file()
            case 7:
                load_catalog_from_file()
            case 8:
                break
            case _:
                print("Enter valid input")
main()
