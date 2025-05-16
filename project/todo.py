# Welcome to todo project

def todo ():
    print("Welcome to todo project")
    todoList = []

    howTodo = int(input("How many todo list add : "))

    for i in range(1, howTodo+1) :
        todo = input(f"Enter your todo : {i} = ")

        todoList.append(todo)

    print(f"Your todo list \n {todoList}")

    while True :
        oparation = int(input("1-ADD\n2-Update\n3-Vew\n4-Delete\n5-Exit\ninter your number: "))
        # todo add
        if oparation == 1 :
            add = input("Enter your add todo : ")
            todoList.append(add)
            print(f"Todo add successfull : {add}")
        # update todo
        elif oparation == 2 :
            upTodo = input("update todo name :")
            if upTodo in todoList :
                up = input("new todo list name : ")
                ind = todoList.index(upTodo)
                todoList[ind]=up
                print(f"todo update successfull {up}")
            else :
                print("Invalid todo name")
        # All todo vew
        elif oparation == 3 :
            print(f"Your all todo\n{todoList}")
        # delete todo
        elif oparation == 4 :
            delTodo = input("Delete todo name : ")
            if delTodo in todoList :
                delIndex = todoList.index(delTodo)
                del todoList[delIndex]
                print(f"delete has successfull {delTodo}")
            else :
                print("Invalid todo name")
        # Exit todo
        elif oparation == 5 :
            print("End your todo list")
            break
        # Invalid
        else :
            print("Invalid number")

todo()