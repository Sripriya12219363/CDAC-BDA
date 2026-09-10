# def main():
#     s=input("Enter the string: ")
#     l=s.split(" ")
    
#     res=""
#     for i in range(0,len(l)):
#         num=0
#         for j in range(0, len(l)):
#             if(l[i]==l[j]):
#                 num+=1
#         res+=l[i]+str(num)
#     print(res)
# main()


inventory = {"apples": 10, "bananas": 24}

# View of keys
keys_view = inventory.keys()
print("Keys:", list(keys_view))  # Output: ['apples', 'bananas']


# View of values
values_view = inventory.values()
print("Values:", list(values_view))  # Output: [10, 24]

# View of key-value tuples
items_view = inventory.items()
print("Items:", list(items_view))  # Output: [('apples', 10), ('bananas', 24)]