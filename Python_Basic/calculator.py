def get_variable(order: int) -> int:
    variable = ''
    if order == 1:
        print_text = 'Choose a number:\n'
    else:
        print_text = 'Choose another one:\n'

    try:
        variable = int(input(print_text))

    except:
        while type(variable) != int:
            print('Please Enter the Number')
            try:
                variable = int(input(print_text))
            except:
                pass

    return variable


def add(v1: int, v2: int) -> int:
    """ Add Function"""
    return v1 + v2


def minus(v1: int, v2: int) -> int:
    """ Minus Function"""
    return v1 - v2


def multiply(v1: int, v2: int) -> int:
    """ Multiply Function"""
    return v1 * v2


def devide(v1: int, v2: int) -> float:
    """ Devide Function"""
    return v1 / v2


def get_formula(v1: int, v2: int, operation: str, result: float) -> str:
    """ Get formula Function"""
    return f"{v1} {operation} {v2} = {result}."


def print_result(result: float):
    """ Print result Function"""
    print(f"Result: {result}")


playing = True
system_operator = ['exit']
default_operator = ['+', '-', '*', '/']
history = []

while playing:
    system_operation = input(
        "Choose an System Menu (enter : calculate, exit: exit): ")

    if system_operation.lower() == 'exit':
        playing = False
        break
    else:
        pass

    a = get_variable(1)

    operation = input(
        "Choose an operation:\n    Options are: + , - , * or /.  : ")

    b = get_variable(2)
    if operation in default_operator:
        if operation == '+':
            result = add(a, b)
            print_result(result)
            formula = get_formula(a, b, operation, result)
            history.append(formula)

        elif operation == '-':
            result = minus(a, b)
            print_result(result)
            formula = get_formula(a, b, operation, result)
            history.append(formula)

        elif operation == '*':
            result = multiply(a, b)
            print_result(result)
            formula = get_formula(a, b, operation, result)
            history.append(formula)

        elif operation == '/':
            while b == 0:
                print('You can\'t devide by 0')
                b = int(input("Choose another one:\n"))
                if b != 0:
                    break
            result = devide(a, b)
            print_result(result)
            formula = get_formula(a, b, operation, result)
            history.append(formula)

    else:
        print(f"Invalid operation : {operation}. Try Again")
print("History:")
for entry in history:
    print(entry)
