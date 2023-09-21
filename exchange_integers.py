digit_first, digit_second = int(input()), int(input())
print(f'Before: \na = {digit_first} \nb = {digit_second}')
third_digit = digit_second
digit_second = digit_first
digit_first = third_digit
print(f'After: \na = {digit_first} \nb = {digit_second}')
