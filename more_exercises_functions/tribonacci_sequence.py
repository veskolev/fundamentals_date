def tribonacci_sequence(number: int) -> str:
    sequence = []
    if number == 1:
        sequence.append(1)
        return sequence
    elif number == 2:
        sequence.append(1)
        sequence.append(1)
        return sequence
    elif number == 3:
        sequence.append(1)
        sequence.append(1)
        sequence.append(2)
        return sequence
    else:
        sequence.append(1)
        sequence.append(1)
        sequence.append(2)
        for i in range(3, number):
            sequence.append(sequence[i-1] + sequence[i-2] + sequence[i-3])
        return sequence


number_interactions = int(input())
result = tribonacci_sequence(number_interactions)
final_sequence = ''
for i in range(len(result)):
    final_sequence += str(result[i]) + ' '
print(final_sequence)

# print(f"{' '.join(map(str, result))}")
