
while True:
    user_action = input("Type add, show, edit, completed or exit:")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a To Do:") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}. {item}")

        case "edit":
            number = int(input("Number of the To Do to edit:")) - 1
            new_todo = input("Enter new To Do:")
            todos[number] = new_todo

        case "completed":
            user_input = int(input("Enter completed item number:")) - 1
            todos.pop(user_input)

        case "exit":
            break

print("Thank You!")
