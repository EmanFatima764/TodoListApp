from task_manager import add_task, delete_task, mark_task_done, view_tasks
def main():
 while True:

    print("\n .... Todo List  Menu ...")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Tasks")
    print("5. Exit")

    # Get user choice
    choice =input("Enter your choice  :")
   
    #  add task
     
    if choice == "1":
     add_task()

    #  view task

    elif choice == "2":
        view_tasks()

     # mark as done

    elif choice == "3":
        mark_task_done()
            
# delete task

    elif choice == "4":
        delete_task()
#  Exiting Taskflow

    elif choice == "5":
        print("Exiting Taskflow ...GoodBye! 👋")
        break
    else:       
         print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    


