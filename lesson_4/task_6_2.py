from itertools import cycle

source_list = 'итератор повторяющий элементы некоторого списка определенного заранее'.split(' ')
full_cycle_max_count = 2
counter = 0
for string in cycle(source_list):
    if full_cycle_max_count * len(source_list) == counter:
        break
    print(string)
    counter += 1
