numbers_wagons = [0] * int(input())

while True:
    common = input().split(' ')
    if common[0] == 'End':
        break
    elif common[0] == 'add':
        people = int(common[1])
        numbers_wagons[-1] += people

    elif common[0] == 'insert':
        wagon = int(common[1])
        people = int(common[2])
        numbers_wagons[wagon] += people
    elif common[0] == 'leave':
        wagon = int(common[1])
        people = int(common[2])
        numbers_wagons[wagon] -= people
print(numbers_wagons)
