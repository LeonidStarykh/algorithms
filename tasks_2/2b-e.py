N = int(input())
arr = list(map(int, input().split()))

def find_min(data):
    min_i = 0
    for i in range(1, len(data)):
        if data[i] < data[min_i]:
            min_i = i
    return min_i

new_arr = []

for i in range(len(arr)-1):
    min = find_min(arr)
    new_arr.append(arr.pop(min))

print(sum(new_arr))