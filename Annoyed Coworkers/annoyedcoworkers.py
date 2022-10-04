# Author: Nishka Awasthi
# It is ok to post my anonymized solution

import heapq

# Get input
inp = list(map(int, raw_input().split()))
help_needed = inp[0]
num = inp[1]
coworkers = []
max = 0

# make my priority queue
for i in range(num):
    temp = list(map(int, raw_input().split()))
    if max < temp[0]:
        max = temp[0]
    temp[0] += temp[1]
    heapq.heappush(coworkers, temp)

# as long as we need help
for i in range(help_needed):
    # get the best person to ask for help
    coworker = heapq.heappop(coworkers)
    if coworker[0] > max:
        max = coworker[0]
    coworker[0] += coworker[1]
    # return them to the list
    heapq.heappush(coworkers, coworker)

print(max)


