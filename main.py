todos = []

while True:
    user_action = input("Type add or show: ").strip()
    
    match user_action:
        case ("add" | "append"):
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'quit' | 'exit':
            break
        case whatever:
            print ('Command is unknown: ' + whatever)

print("Bye!")