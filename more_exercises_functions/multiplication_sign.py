def multi_sing(numbers: list) -> str and int:
    negative_numbers = []
    positive_numbers = []
    if 0 in numbers:
        return 0
    for m in numbers:
        if m < 0:
            negative_numbers.append(m)
        else:
            positive_numbers.append(m)
    if len(negative_numbers) == 1 or len(negative_numbers) == 3:
        return 'negative'
    return 'positive'


numbers_multi = []
for n in range(3):
    number = int(input())
    numbers_multi.append(number)
result = multi_sing(numbers_multi)
print(result)
