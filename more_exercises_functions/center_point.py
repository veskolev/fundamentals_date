def center_point(value1, value2) -> int:
    if value1 < value2:
        return int(value1)
    return int(value2)

x1 = input()
y1 = input()
x2 = input()
y2 = input()
x = center_point(x1, x2)
y = center_point(y1, y2)
print(f'({x}, {y})')

