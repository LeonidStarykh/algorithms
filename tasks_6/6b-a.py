def binsearch(data, ot, do, left=True):
    l = 0
    r = len(data) - 1
    if left:
        while l < r:
            m = (l + r) // 2
            if data[m] >= ot:
                r = m
            else:
                l = m + 1
    else:
        while l < r:
            m = (l + r + 1) // 2
            if data[m] <= do:
                l = m
            else:
                r = m - 1
    return l

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
ans = []
arr.sort()

for req in range(k):
    begin, end = map(int, input().split())
    if (begin > arr[-1]) or (end < arr[0]):
        ans.append(0)
    else:
        left_search = binsearch(arr, begin, end)
        right_search = binsearch(arr, begin, end, left=False)
        ans.append(right_search - left_search + 1)
print(*ans)