number_of_line = int(input())
list_positive = []
list_negative = []
list_odd = []
list_even = []

for num in range(number_of_line):
    current_number = int(input())
    if current_number >= 0:
        list_positive.append(current_number)
    else:
        list_negative.append(current_number)
    if current_number % 2 == 0:
        list_even.append(current_number)
    else:
        list_odd.append(current_number)
command = input()
if command == 'even':
    print(list_even)
elif command == 'odd':
    print(list_odd)
elif command == 'negative':
    print(list_negative)
elif command == 'positive':
    print(list_positive)
