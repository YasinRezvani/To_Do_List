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