todos = []

while True:
    user_action = input("Type add, show, edit, or exit:\n")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a To Do:\n")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            number = int(input("Number of the To Do to edit:\n"))
            number = number - 1
            new_todo = input("Enter new To Do:\n")
            todos[number] = new_todo
        case "exit":
            break