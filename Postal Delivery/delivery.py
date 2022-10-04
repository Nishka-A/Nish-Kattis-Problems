# Author: Nishka Awasthi
# It is ok to post my anonymized solution

import math

temp = list(map(int, input().split()))
n = temp[0] # number of delivery addresses
k = temp[1] # carrying capacity
neg = []
pos = []
distance = 0
at_post = True

# take in negative input into one array
# positive input into another one
for i in range(n):
    temp = list(map(int, input().split()))
    if temp[0] < 0: neg.append(temp)
    else: pos.append(temp)

# sort the lists
neg.sort()
pos.reverse()
left = 0

for i in neg: i[0] *= -1

# ------------------ #

for i in neg:
    if left == 0:
        # number of trips i need to make
        trips = math.ceil((i[1] * 1.0) / k)
        # distance I need to travel
        distance += trips * 2 * i[0]
        # what are leftovers?
        left = (trips * k) - i[1]
    else: # we first need to subtract out leftover from the current value and then make the calculation

        trips =  math.ceil((1.0 * i[1] - left) / (k * 1.0))
        distance += trips * 2 * i[0]
        left = (trips * k) - (i[1] - left)

left = 0

for i in pos:
    if left == 0:
        # number of trips i need to make
        trips = math.ceil(i[1] / (k * 1.0))
        # distance I need to travel
        distance += trips * 2 * i[0]
        # what are leftovers?
        left = (trips * k) - i[1]
    else: # we first need to subtract out leftover from the current value and then make the calculation
        trips =  math.ceil((i[1] - left) / (k * 1.0))
        distance += trips * 2 * i[0]
        left = (trips * k) - (i[1] - left)

print(distance)
