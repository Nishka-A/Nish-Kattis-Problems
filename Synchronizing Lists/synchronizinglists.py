n = int(raw_input())
while n != 0:
    l1 = []
    og_list = []
    for i in range(n):
        temp = int(raw_input())
        l1.append(temp)
        og_list.append(temp)

    l1.sort()

    l2 = []
    for i in range(n):
        l2.append(int(raw_input()))

    l2.sort()

    key = {}

    for i in range(n):
        key[l1[i]] = l2[i]

    print('')
    for i in og_list:
        print(key[i])

    n = int(raw_input())
