names_list = input().split(', ')
sorted_list = sorted(sorted(names_list, key=str, reverse=False), key=len, reverse=True)
print(sorted_list)
