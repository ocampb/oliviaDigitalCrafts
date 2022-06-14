
toDoList = []
   
        

class Task:
    def __init__(self, todo, priority):
        self.todo = todo
        self.priority = priority
        

userDecision = ''

while userDecision != 'q': 
    userDecision = input(
        "Press 1 to add task"
        "Press 2 to delete task"
        "Press 3 to view all tasks"
        "Press q to quit")
    if userDecision == "1": 
        toDoInput = input("What is the name of your todo?")
        priorityInput = input("How important is this task high/low?")
        toDoList.append(
            Task(toDoInput, priorityInput)
        )
    if userDecision == "2":
        deleteTask = input("What is the numerical value of the task you would like to delete?")
        deleteTask = int(deleteTask) - 1
        del toDoList[deleteTask]

    if userDecision == "3": 
        numericOrder = 1
        for task in toDoList:
            print(str(numericOrder) + " - " + task.todo + " - " + task.priority)
            numericOrder = numericOrder + 1

