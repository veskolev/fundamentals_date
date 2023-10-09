def data_types(command):

    if command == 'int':
        value = int(input())
        return value * 2
    elif command == 'real':
        value = float(input())
        return f'{value * 1.5:.2f}'
    elif command == 'string':
        value = input()
        return '$' + value + '$'
data_com = input()
print(data_types(data_com))
