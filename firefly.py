import bisect

temp = list(map(int, raw_input().split()))
num, height = temp[0], temp[1]

g, g_hits, c, c_hits, hits = [], [], [], [], []

count = 0
while count < num:
    count += 2
    g.append(int(raw_input()))
    c.append(int(raw_input()))

if count > num:
    g.append(int(raw_input()))

g.sort()
c.sort()

for level in range(1, height + 1):
    g_hits.append(len(g) - bisect.bisect_left(g, level))
    c_hits.append(len(g) - bisect.bisect_left(c, level))

c_hits.reverse()

for i in range(len(g_hits)):
    hits.append(g_hits[i] + c_hits[i])

print(str(min(hits)) + ' ' + str(hits.count(min(hits))))
