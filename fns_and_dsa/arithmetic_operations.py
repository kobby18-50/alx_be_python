def perform_operation(num1, num2, operation):
       
    match(operation):
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if(num2 == 0):
                return print('Cannot divide by zero')
            else:
                return num1/num2
        case _:
            return print('Invalid input, try again')
    