arr = list(map(int, input().split()))

mark_i = []
houses_i = []
m_d = 0

for i in range(len(arr)):
    if arr[i]==2:
        mark_i.append(i)
    if arr[i]==1:
        houses_i.append(i)

for h in houses_i:
    min_dist = 10
    for m in mark_i:
        dist = abs(h-m)
        if dist < min_dist:
            min_dist = dist
    if min_dist > m_d:
        m_d = min_dist
print(m_d)