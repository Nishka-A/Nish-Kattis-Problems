num = int(raw_input())

lst = []

for i in range(num):
    lst.append(int(raw_input()))

lst.sort()

h = 0
while len(lst) > 0 and lst[-1] > h:
    lst.pop()
    h += 1

print(h)
