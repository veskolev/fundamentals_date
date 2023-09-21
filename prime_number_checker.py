number = int(input())
count_divisions = 0
while True:
    for division in range(2, number+1):
        if number % division == 0:
            count_divisions += 1
    break
if count_divisions == 1:
    print('True')
else:
    print('False')
