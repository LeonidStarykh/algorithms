def binsearch(data, znach, left=True):
    l = 0
    r = len(data) - 1
    if left:
        while l < r:
            m = (l + r) // 2
            if data[m] >= znach:
                r = m
            else:
                l = m + 1
        if data[l] != znach:
            return -1
    else:
        while l < r:
            m = (l + r + 1) // 2
            if data[m] <= znach:
                l = m
            else:
                r = m - 1
        if data[l] != znach:
            return -1
    return l

n = int(input())
arr = list(map(int, input().split()))
M = int(input())
m_arr = list(map(int, input().split()))
ans = []

for val in range(M):
    left_search = binsearch(arr, m_arr[val])
    right_search = binsearch(arr, m_arr[val], left=False)
    ans.append((left_search + 1,right_search + 1))

for i in ans:
    print(*i)