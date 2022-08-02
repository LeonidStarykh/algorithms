arr1 = set(list(map(int, input().split())))
arr2 = set(list(map(int, input().split())))

cnt = 0
for i in arr1:
    if i in arr2:
        cnt += 1
print(cnt)