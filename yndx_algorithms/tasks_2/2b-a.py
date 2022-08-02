arr = [0] * 10001
for i in range(10001):
    x = int(input())
    if x != 0:
        arr[i] = x
    else:
        stop = i
        break

arr = arr[:stop]

cnt = 1
max_i = 0
for i in range(1, len(arr)):
    if arr[max_i] == arr[i]:
        cnt += 1
    elif arr[i] > arr[max_i]:
        max_i = i
        cnt = 1
print(cnt)