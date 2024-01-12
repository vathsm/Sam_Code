
while True:
    user_action = input("Type add, show, edit, completed or exit:")
    user_action = user_action.strip()

    if "add" in user_action:
        todo = user_action[4:]

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        todos.append(todo)

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # file = open("todos.txt", "w")
        # file.writelines(todos)
        # file.close()

    elif "show" in user_action:
        #  file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif "edit" in user_action:
        number = int(input("Number of the To Do to edit:")) - 1
        new_todo = input("Enter new To Do:")
        todos[number] = new_todo

    elif "completed" in user_action:
        user_input = int(input("Enter completed item number:")) - 1
        todos.pop(user_input)

    elif "exit" in user_action:
        break

print("Thank You!")
