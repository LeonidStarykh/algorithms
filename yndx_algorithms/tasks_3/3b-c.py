arr = list(map(int, input().split()))
dict = {}

for i in range(len(arr)):
    if dict.get(arr[i]):
        dict[arr[i]] += 1
    else:
        dict[arr[i]] = 1

new_arr = []
for k,v in dict.items():
    if v == 1:
        new_arr.append(k)

print(*new_arr)