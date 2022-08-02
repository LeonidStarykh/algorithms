n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

left = 0
right = x[-1] - x[0]

while left < right:
    l = (right + left) // 2
    cnt = 0
    maxright = x[0] - 1
    for nowx in x:
        if nowx > maxright:
            cnt += 1
            maxright = nowx + l
    if cnt > k:
        left = l + 1
    else:
        right = l
print(left)
