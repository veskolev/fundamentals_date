number_of_lines = int(input())
open_bracket = False
close_bracket = False
balanced = False
for num in range(number_of_lines):
    command = input()
    if command == '(':
        balanced = False
        open_bracket = True
        close_bracket = False
    if command == ')':
        if open_bracket:
            close_bracket = True
        else:
            break

    if open_bracket and close_bracket:
        balanced = True
        open_bracket = False

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')

