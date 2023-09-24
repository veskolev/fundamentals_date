number_of_line = int(input())
my_list = []
list_with_search_word = []
search_word = input()
for n in range(number_of_line):
    current_str = input()
    my_list.append(current_str)
    if search_word in current_str:
        list_with_search_word.append(current_str)
print(my_list)
print(list_with_search_word)

# print(my_list[search_word])
