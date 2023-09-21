key = int(input())
number_of_lines = int(input())
massege = ''
for numb in range(number_of_lines):
    str = input()
    massege += chr(ord(str) + key)
print(massege)
