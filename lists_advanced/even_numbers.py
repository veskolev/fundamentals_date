numbers_list = input().split(', ')
index_even = []
for index, number in enumerate(numbers_list):
    number = int(number)
    if number % 2 == 0:
        index_even.append(index)
print(index_even)

