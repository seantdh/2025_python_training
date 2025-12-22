# user_prompt = "Enter to don't : "
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)
#
# todos = [todo1, todo2, todo3, 5]
# print(todos)
# print(type(todos))

# Match case

Todos = []

while True:
    user_action = input("Type Show, Add or Exit : ")
    match user_action:
        case "Show":
            print(Todos)
        case "Add":
            todo = input("Enter here : ")
            Todos.append(todo)
        case "Exit":
            break
print("Bye Bye !")