def addition(a: int, b: int):
    return a + b


def subtraction(a: int, b: int):
    return a - b


def multiplication(a: int, b: int):
    return a * b


def division(a: int, b: int):
    return a / b


def modulo(a: int, b: int):
    return a % b


def main():
    while True:
        command = input(' 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Modulo\n 6.Quit the program :')
        if command == '6':
            exit('End')
        a = int(input())
        b = int(input())
        if command == '1':
            print(addition(a, b))
        elif command == '2':
            print(subtraction(a, b))
        elif command == '3':
            print(multiplication(a, b))
        elif command == '4':
            print(division(a, b))
        elif command == '5':
            print(modulo(a, b))
        else:
            print('Invalid command')

main()
