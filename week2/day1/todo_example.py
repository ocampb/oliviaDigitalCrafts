
toDoList = []

def printTasks():
    indexNumber = 1
    for myTask in toDoList:
        print(str(indexNumber) + ' - ' + myTask.todo + ' - ' + myTask.priority)
        indexNumber = indexNumber + 1
   
        

class Task:
    def __init__(self, todo, priority):
        self.todo = todo
        self.priority = priority


userDecision = ''

while userDecision != 'q': 
    userDecision = input(
        "Press 1 to add task\n"
        "Press 2 to delete task\n"
        "Press 3 to view all tasks\n"
        "Press q to quit\n"
        )

    if userDecision == '1': 
        todo = input("Task description?\n")
        priority = input("High or low priority?\n")
        
        newTask = Task(todo, priority)
        
        toDoList.append(newTask)
    elif userDecision == '2':
        if len(toDoList) > 0:
            printTasks()
            indexToRemove = int(input("Which task do you want to delete?\n")) - 1
            toDoList.pop(indexToRemove)
        else:
            print("You need to create a task first.")
    elif userDecision == '3':
        printTasks()

