todo_list = []
#helper function
def get_valid_task_index(prompt):
    while True:
        index = input(prompt).strip()
        #checks if the index is not a number
        if not index.isdigit():
            print("Invalid input (Input must be a number)")
            
        else:
            index = int(index) - 1
            # Check if the index is within the range of the list
            if 0 <= index  < len(todo_list):
                return index
                
            else:
                print("Invalid task number try again ")
                
#let the user add new a new task
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
          
#shows the user how many task they currently have
def view_task():
    if not todo_list:
        print("Task not found ")
    else:
        print("\n TASKS")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

#mark a task as completed
def mark_task_completed():
    if not todo_list:
        print("Task not found ")
        return  
   
    index = get_valid_task_index("Enter a number to be marked as completed: ")
    completed_task = todo_list.pop(index)
    print(f"Task {completed_task} marked as completed")
                
#delete a task form the list
def delete_task():
    if not todo_list:
        print("Task not found ")
        return
    
    index = get_valid_task_index("Enter a number to be deleted ")
   
    deleted_task = todo_list.pop(index)
    print(f"Task {deleted_task} has been deleted")
               
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
        choice = input("Enter a choice ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("GOODBYE")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()


