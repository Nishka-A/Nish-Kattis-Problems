temp = list(map(int, raw_input().split()))
n, m, a, c, xmin = temp[0], temp[1], temp[2], temp[3], temp[4]

lst = []
for i in range(n):
    xmin = ((a * xmin) + c ) % m
    lst.append(xmin)


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

count = 0
for i in lst:
    val = binary_search(lst, i)
    if val != -1:
        count += 1

print(count)
