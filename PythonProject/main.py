# todos = []

while True:
    user_action = input('Please Type Add , Show , Edit, Complete,  Exit:')
    user_action = user_action.strip()
    # Check các trường hợp có khả năng xảy ra
    match user_action.capitalize():
        # Thêm nội dung cần vào todo list
        case 'Add':
            user_todo = input('Enter a todo : ') + '\n'
            file = open('todos.txt', 'r')
            # Trả về kết quả là 1 list nên không cần tạo list rỗng cho todos ở trên nữa
            todos = file.readlines()   # Trả về 1 list todos = [...]

            file.close()  # Phải close thì mới hiển thị data trong file ra được

            todos.append(user_todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)      #  Lúc này todos đã được thêm data người dùng nhập vào
            file.close()  # Phải close thì mới hiển thị data trong file ra được

        # Show todo list
        case 'Show' | 'display':
            if not todos:
                print('Nothing todo here')
            else:
                file = open('todos.txt', 'r')
                todos = file.readlines()
                file.close()

                for index, item in enumerate(todos):
                    row = f"{index + 1}・{item}"
                    print(row)
        # Thay đổi nội dung có trong todo list
        case 'Edit':
            number_getting = int(input('Enter todo number: '))
            number_getting = number_getting - 1
            new_todo = input('Enter new todo: ')
            todos[number_getting] = new_todo
        # Complete todo
        case 'Complete':
            number = int(input('Number of the todo to complete: '))
            todos.pop(number - 1)
        # Thoát khỏi loop
        case 'Exit':
            break
        # Tương đương với else trong if else. Dùng cho trường hợp user nhập các string khác
        case _:
            print('Hey, you entered an unknown command')

print('Bye, See you again!')




