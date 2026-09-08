products=[{"id":1,"name":"Laptop","category":"Electronics","price":55000,"quantity":10},
          {"id":2,"name":"SmartPhone","category":"Electronics","price":20000,"quantity":20},
          {"id":3,"name":"Chair","category":"Furniture","price":1500,"quantity":50},
          {"id":4,"name":"Notebook","category":"Stationary","price":50,"quantity":200},
          {"id":5,"name":"Bottle","category":"Accessories","price":300,"quantity":80}]
id_counter=5

def menu():
    m="""
    1. Add products
    2. View products
    3. Search products
    4. Update products
    5. Delete products
    6. Exit
     """
    print(m)
    ch=int(input("Enter your choice: "))
    return ch

def add_products():
    global id_counter
    try:
        name=input("Enter the name to add: ")
        category=input("Enter the category to add: ")
        price=float(input("Enter the price for adding: "))
        quantity=int(input("Enter the quantity of product to add: "))

        if(name==" "):
            print("Enter valid input")
        if(category==" "):
            print("Enter valid category")
        if(price==""):
            print("Enter valid price")
        if(quantity==""):
            print("Enter valid quantity")

        products.append({"id":id_counter,"name":name,"category":category,"price":price,"quantity":quantity})
        print("Product added successfully.")
    except:
        print("Enter a valid input as mentioned")

def view_products():
    display(products)

    # print("-"*80)
    # print(f'{"Id":^5}{"Name":<20}{"Category":<20}{"Price":<10}{"Quantity":<10}')
    # print("-"*80)
    # for i in products:
    #     pid,name,categ,price,quant=i.values()
    #     print(f'{pid:^5}{name:<20}{categ:<20}{price:<10}{quant:<10}')
    # print("-"*80)

def search_products():
    try:
        ch="""1. Search by id
        2. Search by name"""
        print(ch)
        c=int(input("Enter the choice to perform search: "))
        if(c==1):
            sid=int(input("Enter the id to search: "))
            search_by_id(sid)
        elif(c==2):
            search_by_name()
        else:
            print("Enter valid input")
    except:
        print("Enter valid input of the specified format only.")
    

def search_by_id(sid):
    try:
        res=[a for a in products if a['id']==sid]
        if res:
            print("Product Found")
        else:
            print("Product not found")
        return res
    except:
        print("Enter a valid input")
    
def search_by_name():
    try:
        name=input("Enter a name to search: ")
        res=[a for a in products if a['name']==name]
        if res:
            print("Product Found")
        else:
            print("Product not found")
        return res
    except:
        print("Enter a valid input")

def update_products():
    try:
        i=int(input("Enter id for which you need to perform updation: "))
        ans=search_by_id(i)
        if ans:
            n=input("Enter name to update: ")
            c=input("Enter category to update: ")
            p=float(input("Enter price to update: "))
            q=int(input("Enter quantity to update: "))
            ans[0].update({"id":i,"name":n,"category":c,"price":p,"quantity":q})
            print("Updation successful")
            display(products)
        else:
            print("Updation is not successful")
    except:
        print("Enter a valid type of input")

def delete_products():
    try:
        i=int(input("Enter the id to delete: "))
        ans=search_by_id(i)
        if ans:
            s=input("Are you sure want to delete the product (y/n): ").lower()
            if s=='y':
                products.remove(ans[0])
                print("Deleted successfully")
            else:
                print("Continue with other processess.")
    except:
        print("Enter valid form of input.")    

def display(p):
    print("-"*80)
    print(f'{"Id":^5}{"Name":<20}{"Category":<20}{"Price":<10}{"Quantity":<10}')
    print("-"*80)
    for i in p:
        pid,name,categ,price,quant=i.values()
        print(f'{pid:^5}{name:<20}{categ:<20}{price:<10}{quant:<10}')
    print("-"*80)

def main():
    while True:
        m=menu()
        match m:
            case 1:
                add_products()
            case 2:
                view_products()
            case 3:
                search_products()
            case 4:
                update_products()
            case 5:
                delete_products()
            case 6:
                break
            case _:
                print("Enter valid input")

main()
