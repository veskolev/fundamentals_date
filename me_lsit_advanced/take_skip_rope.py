hidden_message = input()
alpha_str = []
digit_str = []
skip_list = []
take_list = []
taken_string = []
skipped_string = []
for string in hidden_message:
    if string.isdigit():
        string = int(string)
        digit_str.append(string)
    else:
        alpha_str.append(string)
index = 1
for digit in digit_str:

    if index % 2 == 0:
        skip_list.append(digit)
        index += 1
    else:
        take_list.append(digit)
        index += 1

while alpha_str:

    for strings in range(take_list[0]):
        taken_string.append(alpha_str.pop(0))

    n = take_list.pop(0)
    if not take_list or not skip_list:
        break
    for strings in range(skip_list[0]):
        skipped_string.append(alpha_str.pop(0))

    n = skip_list.pop(0)
    if not take_list or not skip_list:
        break
print(f'{"".join(taken_string)}')
