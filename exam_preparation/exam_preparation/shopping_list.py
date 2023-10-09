def urgent(item, items):
    if item in items:
        return False
    else:
        items.append(item)
        return items


def unnecessary(item, items):
    if item in items:
        items.remove(item)
        return items
    else:
        return False


def correct(item1, item2, items):
    if item1 in items:
        index = items.index(item1)
        items[index] = item2
        return items
    else:
        return False

def rearrange(item, items):
    if item in items:
        item1 = items.pop(item)
        items.append(item1)
        return items
    else:
        return False


initial_list = (input()).split('!')
item_change = []
shop_list = []
while True:
    command = input()
    if command == 'Go Shopping!':
        break
    shop_list.append(command)
for item_in_list in shop_list:
    if 'Urgent' in item_in_list:
        item_change = item_in_list.split(' ')
        initial_list = urgent(item_change[1], initial_list)
    elif 'Unnecessary' in item_in_list:
        item = item_in_list.split(' ')
        initial_list = unnecessary(item_change[1], initial_list)
    elif 'Correct' in item_in_list:
        initial_list = correct(item_in_list[1], item_in_list[1], initial_list)
    elif 'Rearrange' in item_in_list:
        initial_list = rearrange(item_in_list[1], initial_list)
print(initial_list)

