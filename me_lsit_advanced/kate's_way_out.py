number_rows = int(input())
rows = {}
row= []
columns = 1
strings = ''
index1 = 1
for i in range(number_rows):
    row = input()
    index2 = 1
    for strings in row:
        rows[f'x{index2}, y{index1}'] = strings
        index2 += 1
    index1 += 1
point = {i for i in rows if rows[i] == "k"}
if rows['x4, y2'] == ' ':
    print("Yes")

print(point)
print(rows)
