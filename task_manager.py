from storage import load_tasks, save_tasks
task=load_tasks()
 #  add task
     
def add_task():

        task_name=input("Enter the task :")

        tasks={"task":task_name,"done":False}
        task.append(tasks)
        save_tasks(task)
        print("Task added successfully ✅")

        another = input("Add another task? (y/n): ")
        if another.lower() != "y":
            return

#  view task

def view_tasks():

    if len(task) == 0:
        print("⚠ No tasks to display ")
        return

    else:  
        print("\n ... Your Tasks ...")   
        for i, t in enumerate(task, start=1):
                status="✅" if t["done"] else "❌"
                print(f"- {i}. {t['task']} [{status}]")
                

# mark as done

def mark_task_done():

        if len(task) == 0:
            print("⚠ No tasks to mark as done.")
            return

        else:
            view_tasks() 
            try:
                task_num = int(input("Enter task number to be marked as done: "))
                if 1 <= task_num <= len(task):
                    task[task_num - 1]["done"] = True
                    save_tasks(task)
                    print(f"Task {task[task_num - 1]['task']} marked as {'Done ✅' if task[task_num - 1]['done'] else '❌'}")
                else:
                    print("Task not found ❌")
            except:
                print("Please enter a valid number.")
                another = input("Add another task? (y/n): ")
                if another.lower() != "y":
                    return


# delete task

def delete_task():
    view_tasks()
    if len(task )==0:
        print("⚠ No tasks to delete ")
        return
    else:
            try:
                task_num=int(input("Enter task num to be deleted :"))
                if 1<= int(task_num) <=len(task):
                    removed=task.pop((task_num)-1)
                    save_tasks(task)
                    print(f"Task deleted successfully ✅: {removed}")
                else:
                    print("Task not found ❌")
            except :
                print("Please enter a valid number.")

                another = input("Add another task? (y/n): ")
                if another.lower() != "y":
                    return


    


