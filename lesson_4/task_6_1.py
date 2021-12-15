from itertools import count

start_num = 15
end_num = 24
for num in count(start_num):
    if num == end_num:
        break
    print(num)
