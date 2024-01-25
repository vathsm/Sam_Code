
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        todos.append(todo + "\n")

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        # file = open("todos.txt", "w")
        # file.writelines(todos)
        # file.close()

    elif user_action.startswith("show"):
        #  file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            # print(f"{index + 1}. {item}")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        # number = int(input("Number of the To Do to edit:")) - 1
        # new_todo = input("Enter new To Do:")
        # todos[number] = new_todo
        try:

            number = int(user_action[5:])
            print(number)

            number = number - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
            # user_input = int(input("Enter completed item number:")) - 1
            # todos.pop(user_input)
        try:
            number = int(user_action[9:])
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            index = number - 1

            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no to do with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print("Thank You!")
