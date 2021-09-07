from prettytable import PrettyTable

print("\nTo-Do List Document")
print("")
print(
" 1: Enter add : for add new To-Do\n",
"2: Enter update : for update To-Do\n",
"3: Enter delete : for delete To-Do\n",
"4: Enter view : for view your To-Do\n",
"5: Enter exit : for exit the program\n"
)

list_to_do = []

x = PrettyTable()

def add():
    new_to_do = input("\nPlease Enter Your New To-Do: ").lower()
    list_to_do.append(new_to_do)
    print(f"\n--- Successfully add a {new_to_do} to your To-Do List --- \n")
    x.field_names = ["To-Do-List"]
    for i in list_to_do:
        x.add_row([i])
    print(x)    
    x.clear_rows()    
    
def update():
    try:
        item_update = input("\nPlease Enter Your To-Do For Update: ").lower()
        index_to_do = list_to_do.index(item_update)
        item_update_change = input(f"\nPlease Enter New update name For {item_update} To-Do: ").lower()
        list_to_do[index_to_do] = item_update_change
        print(f"\n--- Successfully Update To-Do to {item_update_change} --- \n")
        x.field_names = ["To-Do-List"]
        for i in list_to_do:
            x.add_row([i])
        print(x)    
        x.clear_rows()
    except:
        print("\n--To-Do is Not Found. try again--")

def delete():
    try:
        item_delete = input("\nPlease Enter Your To-Do For delete: ").lower()        
        list_to_do.remove(item_delete)
        print(f"\n--- Successfully Delete {item_delete} From To-Do List --- \n")
        x.field_names = ["To-Do-List"]
        for i in list_to_do:
            x.add_row([i])
        print(x)    
        x.clear_rows()
    except:
        print("\n--To-Do is Not Found. try again--")
    
def view():
    x.field_names = ["To-Do-List"]
    for i in list_to_do:
        x.add_row([i])
    print("")
    print(x)    
    x.clear_rows()

def exit():
    exit = input("\nAre You Sure To Exit? (Y/N): ").lower()
    if exit == "y":
        quit()
    elif exit == "n": 
        pass 
    else:        
        print("\n--Invalid mode. try again--")


while True:
    user_input = input("\nWhat do you want to do (add ,update ,delete ,view ,exit): ").lower()

    if user_input == "add":
        add()
    elif user_input == "update":
        update()
    elif user_input == "delete":
        delete()
    elif user_input == "view":
        view()
    elif user_input == "exit":
        exit()
    else:
        print("\n--Invalid mode. try again--")
        continue


# Made By Yasin Rezvani    