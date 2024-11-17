l=[]
def list_functions(x):
    match x:
        
        case 1:
            s=int(input("enter the size of list"))
            for i in range(s):
                num=int(input("enter theelements of list"))
                l.append(num)
            return l;
        case _:
            print("wrong input")
            return

print("""1. Create a list of N integers
2. Display the list elements
3. Insert an element at a specific position
4. Delete an element at a given position
5. Exit""")
choice=int(input("enter your choice"))  
print("your sesired output is ",list_functions(choice))      

