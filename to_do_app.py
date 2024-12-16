tasks=[]
print("Welcome to our App\n")
total_task=int(input("enter how many task you wanna add: "))
for i in range(1,total_task+1):
    new_task=input(f"Enter task {i}: ")
    tasks.append(new_task)

print(f"Your to-do-list has been created\nHere are the tasks:\n {tasks}")
operation=int(input("Enter 1 to add new task,2 to update the list,3 to view the list,4 to delete a task,5 to stop: "))
while(operation !=5):
    if(operation==1):
        new_task=input("Enter the new_task: ")
        tasks.append(new_task)
        print(f"{new_task} has been added")
    elif(operation==2):
        up=input("Enter the task you want to update: ")
        if up in tasks:
            up_task=input("Enter the new task in place of this task: ")
            index=tasks.index(up)
            tasks[index]=up_task
            print("The task has been updated")
        else:
            print("This task doesn't exist.")
    elif(operation==3):
        print(f"Here is your list:\n{tasks}")
    elif(operation==4):
        del_task=input("Enter the task you want to remove: ")
        tasks.remove(del_task)
        print(f"{del_task} has been removed from the list")
    else:
        break
    operation = int(
        input("Enter 1 to add new task,2 to update the list,3 to view the list,4 to delete a task,5 to stop: "))
print("List has been created,you can start your today's work")
