n, q = map(int, input().split())
arr = list(map(int, input().split()))

prefsum = [0] * (len(arr) + 1)

for i in range(1, len(arr) + 1):
    prefsum[i] = prefsum[i-1] + arr[i-1]

for _ in range(q):
    l, r = map(int, input().split())
    print(prefsum[r] - prefsum[l-1])