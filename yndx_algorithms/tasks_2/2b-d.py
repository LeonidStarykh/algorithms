L, K = map(int, input().split())
arr = list(map(int, input().split()))
lavka = [0] * L

for i in arr:
    lavka[i] = 1

left = None
right = None
if (L % 2 == 1) and (lavka[L // 2] == 1):
    print(L // 2)
else:
    for i in range(L // 2):
        if lavka[i] == 1:
            left = i
    for i in range(L - 1, (L // 2) - 1, -1):
        if lavka[i] == 1:
            right = i
    print(left, right)