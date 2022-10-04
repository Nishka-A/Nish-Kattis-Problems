# Author: Nishka Awasthi
# It is ok to post my anonymized solution

import math

end = int(raw_input()) #5
toll = list(map(int, raw_input().split())) #[5, 4, 2, 8]
time = list(map(int, raw_input().split()))[1:] #[2, 4, 4, 8]

cost, wait, curr_min = 0, 0, toll[0]

for i in range(end - 1):
    # rewrite the current minimum
    if curr_min > toll[i]: curr_min = toll[i]

    # check wait time, pay desired dues
    wait += 1 # to get to next gate
    cost += toll[i]

    if wait < time[i]:
        temp = (time[i] - wait)
        temp = temp + temp % 2 / 2

    print('')
    #print(time[i] - wait)
    print(temp)
    count = 0

    while wait < time[i]: #if the time waited already is less than the time needed to cross
        # add the wait needed
        wait += 2
        # add the cost (from curr_min)
        cost += curr_min * 2
        count += 1
    print(count)

print(cost)



'''
gate, cost, wait = 0, 0, 0 # current gate and cost

while gate < (end - 1):
    # What is gate before next cheapest road?
    next = gate + 1
    while next < len(toll) and toll[gate] < toll[next]:    next += 1

    # What is the most time-consuming gate before next cheapest?
    most_time = max(time[gate:(next + 1)])

    # Change gate to next cheapest
    #   how many gates in between? + their cost
    in_between = next - gate
    wait += in_between
    for i in range(in_between): cost += toll[gate + i]

    #   how many times to loop inside current gate? + added cost
    while wait < most_time:
        wait += 2
        cost += 2 * toll[gate]
    gate = next
'''

