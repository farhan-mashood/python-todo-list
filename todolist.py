
todo_list = []
def add_task():
    while True:
        task = input("Enter a task ")
        if task.isdigit():
            print("Invalid task (Task must be not be numbers)")
            task = input("Enter a task ")
        else:
            todo_list.append(task)
            print("Task added")
            break
          

def view_task():
    if not todo_list:
        print("Task not found ")
    else:
        print("\nTASKS")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def completed():
    if not todo_list:
        print("Task not found ")
        return
    
    while True:
        index = input("Enter a number to mark as completed ")
        if not index.isdigit():
            print("Invalid input (Input must be a number)")
            
        else:
            index = int(index) - 1
            # Check if the index is within the range of the list
            if 0 <= index  < len(todo_list):
                completed_task = todo_list.pop(index)
                print(f"Task {completed_task} marked as completed")
                break
                
            else:
                print("Invalid task number try again ")
                

def delete():
    if not todo_list:
        print("Task not found ")
        return
    
    while True:
        delete_task = input("Enter a number to mark as completed ")
        if not delete_task.isdigit():
            print("Invalid input (Input must be a number)")
            
        else:
            delete_task = int(delete_task) - 1
            
            if 0 <= delete_task  < len(todo_list):
                deleted_task = todo_list.pop(delete_task)
                print(f"Task {deleted_task} has been deleted")
                break
                
            else:
                print("Invalid task number try again ")
        

def main():
    
    while True:
        print("********************")
        print("TODO LIST MENU 😊")
        print("1: Add task")
        print("2: View task")
        print("3: Mark task as completed")
        print("4: Delete task")
        print("5: Exit")
        print("********************")
        choice = input("Enter a choice ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            completed()
        elif choice == "4":
            delete()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()


