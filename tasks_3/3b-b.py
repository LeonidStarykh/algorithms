arr = list(map(int, input().split()))
dict = {}

for i in range(len(arr)):
    if dict.get(arr[i]):
        print('YES')
    else:
        dict[arr[i]] = True
        print('NO')