p = list(map(int, input().split()))

arr = [0] * len(p)
shop = -30

for i in range(len(p)):
    if p[i] == 2:
        shop = i
    if p[i] == 1:
        arr[i] = i - shop

shop = 30
ans = 0

for i in range(len(p) - 1, -1, -1):
    if p[i] == 2:
        shop = i
    if p[i] == 1:
        min_dist = min(shop - i, arr[i])
        ans = max(ans, min_dist)

print(ans)