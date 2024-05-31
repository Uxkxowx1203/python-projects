from f import get_todos, write_todos
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    a=input("add or show or exit or edit or complete")
    a=a.strip()   
    
    if a.startswith('add'):
        todo= a[4:]
        
        todos=get_todos("todos.txt")

        todos.append(todo+'\n')
        write_todos('todos.txt', todos)
    elif a.startswith('show'):
        todos=get_todos('todos.txt')
        
        
        for index, item in enumerate(todos):
            item=item.strip('\n')
            print(f"{index+1}-{item}")
    elif a.startswith('edit'):
        try:
            n=int(a[5:])
            n=n-1
            todos=get_todos('todos.txt')
            new_todos=input("enter the new todo")
            todos[n]=new_todos + '\n'
            write_todos('todos.txt', todos)
        except ValueError:
            print("Command is not right")
            continue

    elif a.startswith('exit'):
        break

    elif a.startswith('complete'):
        try:
            n=int(a[9:])
            todos=get_todos('todos.txt')
            todos.pop(n)
            write_todos('todos.txt', todos)
        except IndexError:
            print("No items of thant number")
            continue
    else:
        print("Command not valid")
print("Bye")
    
    
