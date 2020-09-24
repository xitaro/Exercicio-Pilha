from Stack import Stack

myStack = Stack()

while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do?').split()

    operation = do[0].strip().lower()
    if operation == 'push':
        myStack.Push(int(do[1]))
    elif operation == 'pop':
        popped = myStack.Pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break