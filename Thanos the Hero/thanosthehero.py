import re

#num = int(raw_input())
#list = raw_input()

num = '3'
list = '5 2 3'

arr = [int(s) for s in re.findall(r'\b\d+\b', list)]
arr.reverse()
kill = 0

if arr.count(0) > 0:
    if arr.index(0) < (int(num) - 1):
        kill = 1

else:
    # [3, 2, 5]
    for i in range(int(num) - 1):
        if arr[i] <= arr[i + 1]:
            temp = arr[i] - 1
            kill += (arr[i + 1] - temp)
            arr[i + 1] = temp

print(kill)

