appIsOpen = False
tasks = []
completedTasks = []

# VALIDATION
def isValidChoice(choice):
    try:
        choice = int(choice)
        if 1 <= choice <= 6:
            return True
        else: return False
    except ValueError:
        return False

def getIndexOfTask(task):
    task = int(task)
    return task - 1
    
def taskExists(task):
    try:
        taskIndex = getIndexOfTask(task)
        if taskIndex > 0:
            tasks[taskIndex]
        else:
            return False
    except (IndexError, ValueError):
        return False
    return True

# CHOICES
def addTask():
    print("Please type the task you want to add to your To-Do List")
    task = input()
    if not task:
        print("Your task can't be empty. Try again")
        addTask()
    else:    
        tasks.append(task)
        print(f"Okay, added '{task}' to your To-Do List!")

def viewTasks():
    if len(tasks) < 1:
        print("You haven't added any tasks yet!")
    else:
        print("Your To-Do List")
        print("*****************")
        for i, task in enumerate(tasks):
            print(i+1, task)

def completeTask():
    taskToComplete = input()
    if taskExists(taskToComplete):
        taskIndex = getIndexOfTask(taskToComplete)
        completedTasks.append(tasks[taskIndex])
        print(f"Marked '{tasks[taskIndex]}' as complete")
        del tasks[taskIndex]
    else:
        print("Please pick a valid task from your To-Do List")
        viewTasks()
        completeTask()

def deleteTask():
    taskToDelete = input()
    if taskExists(taskToDelete):
        taskIndex = getIndexOfTask(taskToDelete)
        print(f"Deleted '{tasks[taskIndex]}'")
        del tasks[taskIndex]
    else:
        print("Please pick a valid task from your To-Do List")
        viewTasks()
        deleteTask()

def viewCompletedTasks():
    if len(completedTasks) < 1:
        print("You haven't completed any tasks yet!")
    else:
        print("Your Completed Tasks")
        print("********************")
        # looping through the task so we can display them in an ordered list
        for i, task in enumerate(completedTasks):
            # add 1 to index so we cans tart the count from 1 instead of 0
            print(i+1, task)

def quitApp():
    global appIsOpen
    appIsOpen = False
    print("See ya!")

# RUNNING THE APP
def parseUserInput(choice):
    if isValidChoice(choice):
        choice = choice
        match choice:
            case "1":
                addTask()
            case "2":
                viewTasks()
            case "3":
                print("Enter the number for your completed task")
                completeTask()
            case "4":
                print("Enter the number for which task you would like to delete")
                deleteTask()
            case "5":
                viewCompletedTasks()
            case "6":
                quitApp()
            case _:
                print("Good choice!")
    else:
        print("Select a valid option by typing 1, 2, 3, 4, or 5")
        choice = input()
        parseUserInput(choice)

def startApp():
    global appIsOpen
    appIsOpen = True
    print(
        '''
        Welcome to the To-Do List App!

        1. add a task
        2. view tasks
        3. mark a task as complete
        4. delete a task
        5. view previously completed tasks
        6. quit
        '''
    )
    choice = input()
    parseUserInput(choice)

    while appIsOpen:
        print(
            '''
            Anthing else?

            1. add a task
            2. view tasks
            3. mark a task as complete
            4. delete a task
            5. view previously completed tasks
            6. quit
            '''
        )
        choice = input()
        parseUserInput(choice)
        

startApp()
