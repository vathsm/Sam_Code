todos = []

while True:
    user_action = input("Type add, show, edit, completed or exit:\n")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a To Do:\n")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
        case "edit":
            number = int(input("Number of the To Do to edit:\n")) - 1
            new_todo = input("Enter new To Do:\n")
            todos[number] = new_todo
        case "completed":
            user_input = int(input("Enter completed item number:\n")) - 1
            todos.pop(user_input)
        case "exit":
            break

print("Thank You!")
print("This is Sam's branch")