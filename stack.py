stack = []
a = input("Enter:")
while a != 'end':
    if a == 'undo':
        if len(stack) > 0:
            remove_stack = stack.pop()
            print("Remove:",remove_stack)
        else:
            print("Empty Stack")
    else:
        stack.append(a)
    
    print("Current:",stack)
    a = input("Enter:")
    
print("Final:",stack)