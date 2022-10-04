

values = raw_input().split(" ")
n = int(values[0])
k = int(values[1])


# OPTION 1: N/2 > K (Even Method)
if (n / 2) > k:
    print(k * 2)

# OPTION 2: N/2 = K (Equal Method)
elif (n / 2) == k:
    # n is even
    if ( n % 2 == 0 ):
        print(n)
    # n is odd
    else:
        print(n - 1)

# OPTION 3:  N/2 < K, parses through a boolean array (index represents num)
else:
    nums = [True for i in range(n - 1)]
    mult = 2
    current = mult
    i = 0
    while i < k:
        if current <= n and nums[current - 2]: # if the number is valid and true, inc and set
            nums[current - 2] = False
            i += 1
            if i == k:
                break
            current += mult

        elif current > n:
            mult += 1
            current = mult
        else:
            current += mult

    print(current)

