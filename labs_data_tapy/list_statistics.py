number_of_line = int(input())
positive_number = []
negative_number = []
for n in range(number_of_line):
    numbers = int(input())
    if numbers >= 0:
        positive_number.append(numbers)
    else:
        negative_number.append(numbers)
print(positive_number)
print(negative_number)
print(f"Count of positives: {len(positive_number):.0f}")
print(f"Sum of negatives: {sum(negative_number):.0f}")