n = int(input())
arr = list(map(int, input().split()))

s = 0
mx = arr[0]
for i in arr:
    s += i
    mx = max(mx, s)
    if s < 0:
        s = 0

print(mx)