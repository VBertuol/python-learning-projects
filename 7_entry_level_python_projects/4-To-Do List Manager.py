lst = []
id_counter = 0

while True:
    print("\nWelcome to To-Do List Manager, please chose an option:")
    print("0 - Exit program")
    print("1 - List tasks")
    print("2 - Add task")
    print("3 - Remove Task")
    print("4 - Update Task Status\n")

    while True:
        try:
            option = int(input())
            if option >= 0 and option < 5:
                break
            else:
                print("Please select a valid option")
        except:
            print("Please select a valid option")
    
    if option == 0:
        print("Program terminated")
        break
    elif option == 1:
        print(lst)
    elif option == 2:
        task_name = str(input("Please enter the task name: "))
        task_description = str(input("Please enter the task description: "))
        lst.append({ 'id' : id_counter, 'name' : task_name, 'description' : task_description, 'status' : 'pending'  })
        id_counter += 1
        print("\n Task list successfully updated!\n")
    elif option == 3:
        print(lst)
        try:
            remove_id = int(input("Enter the ID of the task to be removed: "))
            flag = False
            for task in lst:
                if remove_id == task['id']:
                    lst.remove(task)
                    flag = True
                    print("\n Task successfully removed!\n")
                    break
            if flag == False:
                print("Id not found")
        except:
            print("Invalid input, try again...")
    elif option == 4:
        print(lst)
        try:
            update_id = int(input("Enter the ID of the task to be updated: "))
            flag = False
            for task in lst:
                if update_id == task['id']:
                    task['status'] = "completed"
                    flag = True
                    print("\n Task successfully updated!\n")
                    break
            if flag == False:
                print("Id not found")
        except:
            print("Invalid input, try again...")

